#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jlmarks

# @Date:   2016-02-19 10:47:10
# @Last Modified 2016-03-21
# @Last Modified time: 2016-03-21 12:43:39

import datetime
import ClientService
from flask import jsonify, request, current_app, url_for
from . import api
from flask import render_template, session, redirect, url_for, current_app, request, flash
# from .forms import AppApiForm, GetCompCSV, SelectCompCSV, MainForm

clientcalls = ClientService.ClientServiceCalls()

def addClient(id, FirstName='', LastName='', Email='', BirthDate=None):
    if BirthDate is None:
        BirthDate = str(datetime.date.today())
    thisclient = dict(ID = str(id), FirstName = FirstName, LastName = LastName, BirthDate = BirthDate, Email=Email)
    return clientcalls.AddOrUpdateClients(updateAction='AddNew', clients=dict(Client=thisclient))


@api.route('/mb/add/', methods=['GET', 'POST'])
def index():
    fname = "None"
    if 'FirstName' in request.form:
        fname = request.form['FirstName']
    lname = "None"
    if 'LastName' in request.form:
        lname = request.form['LastName']
    email = "None"
    if 'Email' in request.form:
        email = request.form['Email']
    conid = "None"
    if 'Id' in request.form:
        conid = "InfId" + str(request.form['Id'])
    result = addClient(conid, fname, lname, email)
    print conid
    print fname
    print lname
    print email
    print "hello!"
    print result
    return render_template('allonepage.html')
