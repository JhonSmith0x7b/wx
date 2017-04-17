# -*- coding:utf-8 -*-
from flask import request, g, render_template
import common, hashlib, utils
import xml.etree.ElementTree as et
def request_bridge():
	if request.method == 'GET':
		manage = wx_manage()
		signature = request.args.get('signature', '')
		timestamp = request.args.get('timestamp', '')
		nonce = request.args.get('nonce', '')
		echostr = request.args.get('echostr', '')
		response = manage.check(signature, timestamp, nonce, echostr)
		return response
		pass
	elif request.method == 'POST':
                manage = wx_manage()
                signature = request.args.get('signature', '')
                timestamp = request.args.get('timestamp', '')
                nonce = request.args.get('nonce', '')
                echostr = request.args.get('echostr', '')
                check_result = manage.check(signature, timestamp, nonce, echostr)
		utils.print_log('check succ')
		response = manage.deal_text_msg(request.data)
		return response
		pass
	pass


class wx_manage:
	def __init__(self):
		pass

	def check(self, signature, timestamp, nonce, echostr):
		if signature == '' or timestamp == '' or nonce == '':
			utils.print_log('some empty')
			return ''
		token = common.TOKEN
		various = [token, nonce, timestamp]
		various.sort()
		sha1 = hashlib.sha1()
		map(sha1.update, various)
		hashcode = sha1.hexdigest()
		utils.print_log(hashcode)
		if hashcode == signature:
			return echostr
		else:
			print hashcode
			return '1'
		pass
	def deal_text_msg(self, data):
		root = et.fromstring(data)
		response_content = """
		<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime><![CDATA[%s]]></CreateTime>
        <MsgType><![CDATA[%s]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        </xml>
		""" % (root.findall('FromUserName')[0].text, root.findall('ToUserName')[0].text, root.findall('CreateTime')[0].text, 'text', 'hello world')
		utils.print_log(response_content)
		return response_content
		pass
