#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jlmarks
# @Date:   2016-02-19 10:45:00
# @Last Modified 2016-02-19Marks - Jeremiah@JLMarks.org
# @Last Modified time: 2016-02-19 10:46:52

from flask import Blueprint

api=Blueprint('api', __name__)

from . import Client
