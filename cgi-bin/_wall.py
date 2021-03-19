#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import json
import random
import time


class Wall:
#    USERS = 'cgi-bin/users.json'
#    WALL = 'cgi-bin/wall.json'
#    COOKIES = 'cgi-bin/cookies.json'

	def __init__(self):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()
		c.execute("""create table if not exists User(mail text, password text)""")
		c.execute("""create table if not exists Cookie(mail text, cookie text)""")

		conn.commit()
		conn.close()
	def register(self, user, password):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()
		c.execute("insert into User values (?, ?)", (user, password))		
		conn.commit()
		conn.close()
	def set_cookie(self, user):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()
		cookie = str(random.randrange(10**14))  # √енерируем уникальную куку дл€ пользовател€
		c.execute("insert into Cookie values (?, ?)", (user, cookie))
		conn.commit()
		conn.close()
		return cookie

	def find_cookie(self, cookie):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()
		cookie = str(cookie)
		c.execute('select mail from Cookie where cookie = ?', (cookie, ))
		name = c.fetchall()
		if len(name) != 0:
			conn.close()
			return name[0]
		conn.close()
		return None
	def prall(self):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()
		c.execute('select * from User')
		print("VV")
		for row in c.fetchall():
			print(row)
		print("^^")
		
		conn.close()
		
	def find(self, user, password = None):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()
		user = str(user)
		if (password == None):
			c.execute("select * from User where mail = ?", (user, ))
			name = c.fetchall()
			print("VV")
			print(name)
			print("^^")
			conn.close()
			if len(name) != 0:
				return True
			else:
				return False
		else :
			c.execute("select * from User where mail = ?, password = ?", (user, password))
			name = c.fetchall()
			conn.close()
			if len(name) != 0:
				return True
			else:
				return False
			
			
			
			
			
			