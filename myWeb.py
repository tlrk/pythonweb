#!/usr/bin/env python

# coding=utf-8

import aService
import sys
import web

urls = ("/ServiceA","hello")
app = web.application(urls,globals())

class hello:
	def GET(self):
		mservice = aService.AService()
		result = mservice.getA(1002)
		json = ""
		json += "{"
		json += '"sno":"'  + str(result[0]) + '",'
		json += '"sname":"'  + str(result[1]) + '"'
		json += "}"
		return json

if __name__=="__main__":
	app.run()
