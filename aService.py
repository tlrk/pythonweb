#!/usr/bin/env python

import MySQLdb
import sys
import config

class AService(object):
    def getA(self, sno):
      conn = MySQLdb.connect(host=config.host,user=config.user,passwd=config.password,port=config.port,db=config.database,charset=config.charset)
      result=[]
      try:
        cursor = conn.cursor();
        cursor.execute("select * from student where sno='%d'"%(sno))
        result = cursor.fetchone()
      except Exception,e:
        print "System error: ",e
        result = "error"
      finally:
        cursor.close()
        conn.close()
      return result
