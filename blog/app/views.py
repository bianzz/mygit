# -*- coding: utf-8 -*-
#!/usr/bin/env python

from app import app
from flask import render_template, url_for

#@app.route('/')
#def index():
#    return "Hello World!"
#
@app.route('/')
def index():
    return render_template('welcome.html', title="Welcome")

@app.route('/home')
def home():
    return render_template('base.html', title="Home")
