#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

__version__ = '0.01-dev'

app = Flask(__name__)

@app.route('/')
def index():
	return "Drive me version %s" % __version__

if __name__ == '__main__':
	app.run(debug=True)