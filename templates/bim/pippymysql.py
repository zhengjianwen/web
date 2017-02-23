#!/usr/bin/env python
# -*- coding=utf-8 -*-
# Time: 2017/2/22 PM9:30
# Filename: pippymysql.py
# blog:www.hairuinet.com
# Version: 1.0
__author__ = "HaiRui"

import pymysql

conn = pymysql.connect(host='127.0.0.1',\
                       port=3306,user='root',\
                       passwd='123456',db='work',\
                       charset='utf8')

cour=conn.cursor(cursor=pymysql.cursors.DictCursor)#创建游标

# cour.execute('INSERT INTO course (cname, tid) VALUES ("python",6)')

cour.execute('select * from course')
cour.executemany()
ret = cour.fetchall()
ret1 = cour.fetchmany(4)

print(ret)

# conn.commit()#确认执行 只在 增删改 需要

cour.close()#关闭游标
conn.close()#关闭连接
