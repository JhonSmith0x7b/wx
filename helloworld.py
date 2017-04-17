# -*- coding:utf-8 -*-
import sys;reload(sys);sys.setdefaultencoding('utf-8')
from flask import Flask, request, render_template, g
import wx_manager as wx
app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['get'])
def helloworld():
	return wx.request_bridge()

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5001)