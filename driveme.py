#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

__version__ = '0.01-dev'
GOOGLE_MAPS_API_KEY = 'AIzaSyAMIfbGGZMum1-DoktxySiVNVR2vFhMe2g'

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', version=__version__, GOOGLE_MAPS_API_KEY=GOOGLE_MAPS_API_KEY)

if __name__ == '__main__':
	app.run(debug=True)