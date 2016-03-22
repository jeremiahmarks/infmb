#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-06-21 15:00:03
# @Last Modified 2015-10-08
# @Last Modified time: 2015-10-08 21:43:46
import os
import xmlrpclib
import csv
from dataStructures import tables


class ISServer(object):

    def __init__(self, infusionsoftapp, infusionsoftapikey):
        self.curdir = os.path.abspath(os.path.curdir)
        self.infusionsoftapp = infusionsoftapp
        self.infusionsoftapikey = infusionsoftapikey
        self.appurl = "https://" + self.infusionsoftapp + \
            ".infusionsoft.com:443/api/xmlrpc"
        self.baseurl = 'https://' + self.infusionsoftapp + '.infusionsoft.com/'
        self.connection = xmlrpclib.ServerProxy(self.appurl)

    ########################################################
    # ## Methods to get records from various tables
    ##
    ##
    def getmatchingrecords(self, tablename, criteria, desiredfields=None,
                           orderedby=None):
        """Search at table by criteria
        """
        return self.getallrecords(tablename, searchcriteria=criteria,
                                  interestingdata=desiredfields,
                                  orderedby=orderedby)

    def gettagcats(self):
        return self.getallrecords("ContactGroupCategory")

    def getalltags(self):
        return self.getallrecords("ContactGroup")

    def getallproductcats(self):
        return self.getallrecords("ProductCategory")

    def getallproducts(self):
        return self.getallrecords("Product")

    def getallrecords(self, tablename, interestingdata=None,
                      searchcriteria=None, orderedby=None):
        if interestingdata is None:
            interestingdata = tables[tablename]
        if searchcriteria is None:
            searchcriteria = {}
        if orderedby is None:
            orderedby = interestingdata[0]
        records = []
        p = 0
        while True:
            listofdicts = \
                self.connection.DataService.query(self.infusionsoftapikey,
                                                  tablename,
                                                  1000,
                                                  p,
                                                  searchcriteria,
                                                  interestingdata,
                                                  orderedby,
                                                  True)
            for each in listofdicts:
                thisrecord = {}
                for eachbit in interestingdata:   # this should be
                    # records.append(zip(interestingdata, each)) perhaps
                    if eachbit not in each:   # TODO: research THIS
                        each[eachbit] = None
                    thisrecord[eachbit] = each[eachbit]
                records.append(thisrecord)
            if not(len(listofdicts) == 1000):
                break
            p += 1
        return records

    def incrementlygetrecords(self,
                              tablename,
                              interestingdata=None,
                              searchcriteria=None,
                              orderedby=None):
        if interestingdata is None:
            interestingdata = tables[tablename]
        if searchcriteria is None:
            searchcriteria = {}
        if orderedby is None:
            orderedby = interestingdata[0]
        records = []
        p = 0
        while True:
            print tablename, p
            print "trying!"
            try:
                listofdicts = \
                    self.connection.DataService.query(self.infusionsoftapikey,
                                                      tablename,
                                                      1000,
                                                      p,
                                                      searchcriteria,
                                                      interestingdata,
                                                      orderedby,
                                                      True)
            except Exception, e:
                print e, p
            for each in listofdicts:
                thisrecord = {}
                for eachbit in interestingdata:   # this should be
                    # records.append(zip(interestingdata, each)) perhaps
                    if eachbit not in each.keys():   # TODO: research THIS
                        each[eachbit] = None
                    thisrecord[eachbit] = each[eachbit]
                records.append(thisrecord)
            if not(len(listofdicts) == 1000):
                break
            p += 1
            if p % 10 == 0:
                fname = tablename + "%010d" % (p) + ".csv"
                print 'writing', p, fname
                with open(fname, 'wb') as outfile:
                    thiswriter = csv.DictWriter(outfile, records[0])
                    thiswriter.writeheader()
                    thiswriter.writerows(records)
                records = []
        fname = tablename + "%010d" % (p) + ".csv"
        print 'writing', p, fname
        with open(fname, 'wb') as outfile:
            thiswriter = csv.DictWriter(outfile, records[0])
            thiswriter.writeheader()
            thiswriter.writerows(records)

    def incgetfiles(self, browser):
        self.curdir = os.path.abspath(os.path.curdir)
        p = 0
        while True:
            print "Doing page " + str(p)
            try:
                listofdicts = \
                    self.connection.DataService.query(self.infusionsoftapikey,
                                                      'FileBox',
                                                      1000,
                                                      p,
                                                      {},
                                                      tables["FileBox"],
                                                      'Id',
                                                      False)
                for eachfile in listofdicts:
                    try:
                        downloadurl = self.baseurl + "/Download?Id=" + \
                            str(eachfile['Id'])
                        browser.open(downloadurl)
                        # folderpath = \
                        # os.path.abspath(os.path.join(self.curdir,
                        # 'files', str(eachfile['ContactId']) ))

                        # This is one of those places that I do not understand
                        # linters.
                        # please tell me a way to appease the linting function
                        # but not have this
                        # stupid mess.  Or can I ignore the linter for things
                        # like this?  Or is there
                        # a better way to do this?
                        fileoutpath = \
                            os.path.abspath(
                                os.path.join(
                                    self.curdir,
                                    'files',
                                    str(eachfile['ContactId']),
                                    eachfile['FileName']))
                        if not os.path.exists(os.path.dirname(fileoutpath)):
                            os.makedirs(os.path.dirname(fileoutpath))
                        fout = open(fileoutpath, 'wb')
                        fout.write(browser.response.content)
                        fout.close()
                    except Exception, e:
                        print eachfile, '\n', e
            except Exception, e:
                print p, e
            finally:
                if not (len(listofdicts) == 1000):
                    break
                else:
                    p += 1

    def getfile(self, browser, eachfile):
        while True:
            try:
                downloadurl = \
                    self.baseurl + "/Download?Id=" + str(eachfile['Id'])
                browser.open(downloadurl)
                fileoutpath = \
                    os.path.abspath(os.path.join(self.curdir,
                                                 'files',
                                                 str(eachfile['ContactId']),
                                                 eachfile['FileName']))
                if not os.path.exists(os.path.dirname(fileoutpath)):
                    os.makedirs(os.path.dirname(fileoutpath))
                fout = open(fileoutpath, 'wb')
                fout.write(browser.response.content)
                fout.close()
            except Exception, e:
                print eachfile, '\n', e

    def cnp(self, productvalues):
        return self.createnewrecord('Product', productvalues)

    def createnewrecord(self, table, recordvalues):
        return self.connection.DataService.add(self.infusionsoftapikey,
                                               table,
                                               recordvalues)
    ########################################################
    # # Methods to updating existing records
    ##

    def updaterecord(self, tablename, recordid, updatevalues):
        return self.connection.DataService.update(self.infusionsoftapikey,
                                                  tablename,
                                                  recordid,
                                                  updatevalues)

    def deleterecordsontable(self, tablename):
        alltableids = self.getallrecords(tablename, ["Id"])
        for eachid in alltableids:
            try:
                self.connection.DataService.delete(tablename, eachid)
            except:
                print "Cannot Delete " + str(eachid)
    ########################################################
    # # Method to create a new contact record, or updates an existing
    # # potential values for checktype are
    # # ['Email', 'EmailAndName', 'EmailAndNameAndCompany']

    def dupecreate(self, contactdata={}, checktype='Email'):
        return self.connection.ContactService.addWithDupCheck(self.infusionsoftapikey,
                                                              contactdata,
                                                              checktype)
    ########################################################
    # # Methods to get meta-data about records

    def getcount(self, tablename, query):
        return self.connection.DataService.count(self.infusionsoftapikey,
                                                 tablename,
                                                 query)

    def verifyconnection(self):
        try:
            self.connection.DataService.query(self.infusionsoftapikey,
                                              "User",
                                              1000,
                                              0,
                                              {},
                                              ["Email"],
                                              "Email",
                                              True)
            return True
        except:
            return False

    def applytag(self, contactid, tagid):
        return self.connection.ContactService.addToGroup(self.infusionsoftapikey,
                                                         contactid,
                                                         tagid)
