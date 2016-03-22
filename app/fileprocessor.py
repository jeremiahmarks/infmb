#!/c/Users/jeremiah.marks/AppData/Local/Continuum/Anaconda2/python
# Yay! I think it will work better now!



#####################################
# This file exists solely to house
# one point of logic, matching the
# data between the files.
# it will use the following bits of data:
    # location of Account.csv
    # location of Attachment.csv
    # location of a recent export of the
        # Infusionsoft company records, to
        # include the company name, the company
        # id, the main contact first/last name
    # some form of api connection with a
        # getallrecords method
        # .connection.FileService.uploadFile method
    # location of the folder that contains all of the
    # files that need to be uploaded.
#
#
#
#
#
#####################################
import csv
import os
import sys
import base64

import ISServer
print 'a'
DEFAULT_CONTACT_TO_ATTACH_TO = 1

class FileLogician(object):
    """docstring for FileLogician
    FileLogician will handle various methods
    needed to match the data as needed.
    Some methods that it will include, though,
    will be the ability to get the first or all
    rows that match criteria.
    Additionally, it will probably implement a v-lookup procedure.
        Like seriously, why have I not done that yet?
    """
    def __init__(self, apiConnection=None, logger=True):
        super(FileLogician, self).__init__()
        self.svr = apiConnection
        self.acctidToContact={}
        self.Accountpath = None
        self.AttachmentCSVpath = None
        self.exportpath = None
        self.logger=logger
        self.uploadedcsvfile='uploaded.csv'
        self.logfile='logfile.txt'
        self.htmlfile='uploadedfiles.html'

    def logdata(self, stringtowriteout):
        if self.logger:
            with open(self.logfile, 'a+') as outfile:
                outfile.write(stringtowriteout + '\n')


    def writecsvfile(self, dicttoupload):
        with open(self.uploadedcsvfile, 'a+') as outfile:
            outfile.write(','.join([str(dicttoupload[x]) for x in sorted(dicttoupload.keys())]) + '\n')

    def addtohtmlfile(self, filename, contactid, fileidininfusionaoft):
        if not os.path.exists(self.htmlfile):
            with open(self.htmlfile, 'w+') as outfile:
                outfile.write("""<html>\n<body>\n<table>\n""")
        with open(self.htmlfile, 'a+') as outfile:
            outfile.write("""
                    <tr><td><a href="https://xo263.infusionsoft.com/Download?Id=%i">%s</a></td><td>%i</td></tr>
                    """ %(fileidininfusionaoft, filename, contactid))

    def setAccount(self, newAccount):
        self.Accountpath=newAccount
        self.logdata("FileLogician Set account to " + str(newAccount))
    def setAttachment(self, newAttachment):
        self.logdata("FileLogician Set Attachment.csv to " + str(newAttachment))
        self.AttachmentCSVpath=newAttachment
    def setexport(self, newexport):
        self.logdata("FileLogician Set company export.csv to " + str(newexport))
        self.exportpath=newexport
    def setfilefolder(self, pathtofolder):
        self.logdata("FileLogician Set path to the files folder to " + str(pathtofolder))
        self.filefolder = pathtofolder

    def startToProcess(self):
        if not all([self.Accountpath, self.AttachmentCSVpath, self.exportpath]):
            raise ValueError("There are not enough values")
        else:
            thisAccountFile = CSVFileActions(self.Accountpath)
            thisexportfile = CSVFileActions(self.exportpath)
            with open(self.AttachmentCSVpath, 'rUb') as infile:
                thisreader = csv.DictReader(infile)
                for eachrow in thisreader:
                    if eachrow['AccountId'] not in self.acctidToContact:
                        thisfileupload={}
                        thisfileupload['currentfilename']=eachrow['Id']
                        thisfileupload['AccountId'] = eachrow['AccountId']
                        thisfileupload['filename'] = eachrow['Name']
                        searchcriteria={}
                        searchcriteria['Id'] = thisfileupload['AccountId']
                        companyreturns = thisAccountFile.getlineswith(searchcriteria)

                        if type(companyreturns) == type(list()):
                            # This will test if a list was returned.  If a list was returned
                            # then there were no results found. (In this implementation,
                            # that method could return a list if "First" is not selected)
                            self.logdata("FileLogician was unable to find the company with ID = " + str(thisfileupload['AccountId'] +
                                                " in the Account.csv file"))
                            continue

                        thisfileupload['companyName'] = companyreturns['Name']
                        thisfileupload['Contact'] = {}

                        searchcriteria = {}
                        searchcriteria['Company'] = thisfileupload['companyName']
                        matchingrow = thisexportfile.getlineswith(searchcriteria)
                        if len(matchingrow) == 0:
                            # Basically this is here for the same reason I check to see if
                            # the list came back empty for the same reasons as above.
                            self.logdata("FileLogician was unable to find the company named " + str(searchcriteria['Company']) +
                                                " in the export from Infusionsoft.")
                            continue


                        thisfileupload['Contact']['FirstName']=matchingrow['Main Contact First Name']
                        thisfileupload['Contact']['LastName'] = matchingrow['Main Contact Last Name']
                        thisfileupload['Contact']['CompanyID'] = int(matchingrow['Id'])

                        self.logdata("FileLogician is about to do a search for " + str(thisfileupload['Contact']))

                        allmatching = self.svr.getallrecords('Contact', searchcriteria= thisfileupload['Contact'])
                        if len(allmatching) == 0:
                            thisfileuploadd['conid'] = DEFAULT_CONTACT_TO_ATTACH_TO
                        else:
                            thisfileupload['conid'] = allmatching[0]['Id']
                        self.acctidToContact[eachrow['AccountId']] = thisfileupload['conid']
                        self.logdata("FileLogician matched these values " + str(thisfileupload))
                    self.uploadfile(self.acctidToContact[eachrow['AccountId']],
                        eachrow['Name'],
                        os.path.abspath(os.path.join(self.filefolder, eachrow['Id'])))

    def uploadfile(self, contactid, filename, filepath):
        # print contactid
        thisfileid = self.svr.connection.FileService.uploadFile(self.svr.infusionsoftapikey, contactid, filename, base64.b64encode(open(filepath, 'rb').read()))
        logstr = "FileLogician uploaded file %s to contact id %s . " %(filename, str(contactid))
        self.logdata(logstr)
        print logstr
        self.writecsvfile({'contactid': contactid, 'filename': filename, 'filepath': filepath})
        self.addtohtmlfile(filename, contactid, thisfileid)


class FileActions(object):
    """docstring for FileActions
    FileActions is basically a static class
    which will perform tasks on a file"""
    def __init__(self, filepath, *args, **kwargs):
        super(FileActions, self).__init__()
        self.fpath = filepath
        self.logfile = None
        if 'logfile' in kwargs.keys():
            self.logfile=kwargs['logfile']

    def getlineswith(self, searchcriteria):
        returnfile=[]
        with open(self.fpath, 'r') as infile:
            for eachline in infile:
                if eachline.count(searchcriteria) > 0:
                    returnfile.append(eachline)
        return returnfile

class CSVFileActions(FileActions):
    """docstring for CSVFileActions"""
    def __init__(self, *args, **kwargs):
        super(CSVFileActions, self).__init__(*args, **kwargs)

    def splitfile(self, maxsize=9961472):
        """This method will take the original
        file, split it, and then return a list
        of CSVFileActions full of the child
        files.
        """
        pass
        currentsize=0
        returnfiles=[]
        with open(self.fpath, 'rb') as infile:
            thisreader = csv.DictReader(infile)

    def getlineswith(self,
                     searchcriteria,
                     first=True,
                     sorting=False,
                     desiredColumns=False):
        """getlineswith accepts a dict of
        columnName->value pairs to search for.
        If first is True and sorting is none
        it will stop the first time it finds
        a matching row and return it. sorting
        will be done via whatever method is
        passed to sorting. Basically, it will
        need to accept two dictionaries (rows
        in the csv file) and return whichever
        is the one that is now in "first".
        If first is false, the method will
        return all rows that match in a list.

        edit to add: desired columns is there
        if you only need one or two columns.
        """
        returnlist = []
        with open(self.fpath, 'rb') as infile:
            thisreader = csv.DictReader(infile)
            if not any([x for x in searchcriteria.keys() if x not in thisreader.fieldnames]):
                for eachrow in thisreader:
                    whatmatches = []
                    for eachkey in searchcriteria:
                        if searchcriteria[eachkey] == eachrow[eachkey]:
                            whatmatches.append(True)
                        else:
                            whatmatches.append(False)
                    if all(whatmatches):
                        if desiredColumns:
                            paredInfo = {columnname: eachrow[columnname] for columnname in desiredColumns}
                        else:
                            paredInfo = dict(eachrow)
                        if sorting:
                            if first:
                                returnlist[0] = sorting(returnlist[0], paredInfo)
                            else:
                                returnlist.append(paredInfo)
                        else:
                            if first:
                                return paredInfo
                            else:
                                returnlist.append(paredInfo)
        if len(returnlist)==0:
            return returnlist
        else:
            if first:
                return returnlist[0]
            else:
                if sorting:
                    return sorting(returnlist)
                else:
                    return returnlist





