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
#create BD
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()
#create table user
		c.execute("""create table if not exists User(mail text, password text)""")
		c.execute("insert into User values('name', 'name')")
		conn.commit()
#create table cookie
		c.execute("""create table if not exists Cookie(mail text, cookie text)""")
		c.execute("insert into Cookie values('cookie', 'cookie')")
		conn.commit()
#create table Text
		c.execute("""create table if not exists Text(mail text, code text)""")
		c.execute("insert into Text values('text', 'text')")
		conn.commit()
        #Создаём начальные файлы, если они не созданы"""
#        try:
#            with open(self.USERS, 'r', encoding='utf-8'):
#                pass
#        except FileNotFoundError:
#            with open(self.USERS, 'w', encoding='utf-8') as f:
#                json.dump({}, f)

#        try:
#            with open(self.WALL, 'r', encoding='utf-8'):
#                pass
#        except FileNotFoundError:
#            with open(self.WALL, 'w', encoding='utf-8') as f:
#               json.dump({"posts": []}, f)
#
#       try:
#            with open(self.COOKIES, 'r', encoding='utf-8'):
#                pass
#        except FileNotFoundError:
#           with open(self.COOKIES, 'w', encoding='utf-8') as f:
#                json.dump({}, f)
		conn.close()
	def register(self, user, password):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()

        #Регистриует пользователя. Возвращает True при успешной регистрации"""

		try:
			if self.find(user):
				return False  # Такой пользователь существует
			c.execute("insert into User values (?, ?)", (user, password))
			c.commit()
#        with open(self.USERS, 'r', encoding='utf-8') as f:
#            users = json.load(f)
#        users[user] = password
#        with open(self.USERS, 'w', encoding='utf-8') as f:
#            json.dump(users, f)
			conn.close()
			return True
		except: 
			list1 = []
			conn.close()
			return False
	def set_cookie(self, user):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()

        #Записывает куку в файл. Возвращает созданную куку."""
#        with open(self.COOKIES, 'r', encoding='utf-8') as f:
#            cookies = json.load(f)
		cookie = str(time.time()) + str(random.randrange(10**14))  # Генерируем уникальную куку для пользователя
		try:
			c.execute("insert into cookie values(?, ?)", (user, cookie))
		except: print("didn't insert")
#        cookies[cookie] = user
#        with open(self.COOKIES, 'w', encoding='utf-8') as f:
#            json.dump(cookies, f)
		conn.close()
		return cookie

	def find_cookie(self, cookie):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()

       	#По куке находит имя пользователя"""
#        with open(self.COOKIES, 'r', encoding='utf-8') as f:
#            cookies = json.load(f)
		try:
			name = c.execute("select mail from User where cookie = {}".format(cookie)).fetchall()
			name =  str(name)
			conn.close()
			return name
		except: 
			list__ = []
			conn.close()
			return None

	def find(self, user, password=None):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()

        #Ищет пользователя по имени или по имени и паролю"""
#        with open(self.USERS, 'r', encoding='utf-8') as f:
#            users = json.load(f)
		try:
			c.execute("select mail from User")
			user_check = str(c.fetchall())
			c.execute("select password from User")
			password_check = str(c.fetchall())
		
			if user is user_check and (password is None or password == password_check):
				conn.close()
				return True
			conn.close()
			return False
		except: 
			list_ = []
			conn.close()
			return False
		
	def publish(self, user, text):
		conn = sqlite3.connect("Contester.db")    
		c = conn.cursor()

        #Публикует текст"""
#        with open(self.WALL, 'r', encoding='utf-8') as f:
#            wall = json.load(f)
		c.execute("insert into Text values (?, ?)", (user, text))
#        wall['posts'].append({'user': user, 'text': text})
#        with open(self.WALL, 'w', encoding='utf-8') as f:
#            json.dump(wall, f)
		conn.close()
	def html_list(self):
        #Список постов для отображения на странице"""
#        with open(self.WALL, 'r', encoding='utf-8') as f:
#            wall = json.load(f)
		c.execute("select * from Text")
		posts = c.fetchall()
		posts = str(posts)
#		for post in wall['posts']:
#			content = post['user'] + ' : ' + post['text']
#			posts.append(content)
		return '<br>'.join(posts)