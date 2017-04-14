# -*- coding:utf-8 -*-
from flask import request, g, render_template
import common, hashlib, utils
def request_bridge():
	if request.method == 'GET':
		manage = wx_manage()
		signature = request.args.get('signature', '')
		timestamp = request.args.get('timestamp', '')
		nonce = request.args.get('nonce', '')
		echostr = request.args.get('echostr', '')
		response = manage.check(signature, timestamp, nonce, echostr)
		return render_template('helloworld.htm', response = response)
		pass
	elif request.method == 'POST':
		return 'fatal.'
		pass
	pass


class wx_manage:
	def __init__(self):
		pass

	def check(self, signature, timestamp, nonce, echostr):
		if signature == '' or timestamp == '' or nonce == '' or echostr == '':
			return 'various is empty'
		token = common.TOKEN
		various = [token, nonce, timestamp]
		various.sort()
		sha1 = hashlib.sha1()
		map(sha1.update, various)
		hashcode = sha1.hexdigest()
		if hashcode == signature:
			return echostr
		else:
			print hashcode
			return 'check fatal.'
		pass
