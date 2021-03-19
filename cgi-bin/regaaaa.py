#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os, sqlite3
#xren
from _wall import Wall
wall = Wall()
registr1 = """
		<div class="col-md-9">
		  {alerttext}
          <h3 class="mb-4">Register</h3>
          <form action="/cgi-bin/regaaaa.py" method="post">
           

            <div class="form-group">
              <label for="email-input">Email</label>
              <input type="email" id="email-input" class="form-control" name = "login" autofocus required>
            </div>
            <div class="form-group">
              <label for="password-input">Password</label>
              <input type="password" id="password-input" class="form-control" name = "password" required>
            </div>
            <div class="form-group">
              <label for="confirm-password-input">ConfirmPassword</label>
              <input type="password" id="confirm-password-input" class="form-control" name = "password2" required>
            </div>
            <div class="d-flex">
              <input type="hidden" name="action" value="login">
              <button type="submit" class="btn btn-primary">Register</button>
              <a href="/cgi-bin/loooogin.py" class="btn btn-link">I have an account</a>
            </div>
          </form>
        </div>
"""
registr = """
        <div class="collapse navbar-collapse" id="navbarNavigation">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a href="/cgi-bin/loooogin.py" class="nav-link">Login</a>
            </li>
            <li class="nav-item">
              <a href="/cgi-bin/regaaaa.py" class="nav-link">Register</a>
            </li>
          </ul>
        </div>
"""
with open("css/bootstrap.min.css") as f:
	csspatt = f.read()
with open("js/bootstrap.min.js") as f:
	jspattboot = f.read()
with open("js/jquery.min.js") as f:
	jspattjquery = f.read()
with open("js/popper.min.js") as f:
	jspattpoper = f.read()
#/xren
#start code
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session = cookie.get("session")
form = cgi.FieldStorage()
action = form.getfirst("action", "")
user = wall.find_cookie(session)  
alert = ""

if action == "login":
	login = form.getfirst("login", "")
	login = html.escape(login)
	password = form.getfirst("password", "")
	password = html.escape(password)
	password2 = form.getfirst("password2", "")
	password2 = html.escape(password2)	
	if wall.find(login):
		alert = """<h3 class="mb-4" style = "color: Red;">login zanyat</h3>"""
	elif(password != password2):
		alert = """<h3 class="mb-4" style = "color: Red;">parroli ne sovpadayut</h3>"""		
	else:
		wall.register(login, password)
		cookie = wall.set_cookie(login)
		print('Set-cookie: session={}'.format(cookie))
		user = login
        
pattern = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Contester</title>
  <style>
 	{css}
  </style>
</head>
<body>
  <div class="layout">
    <div class="navbar navbar-dark bg-warning navbar-expand-lg">
      <div class="container">
        <a href="/cgi-bin/indeeeex.py" class="navbar-brand">Contester</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavigation" aria-controls="navbarNavigation" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        {rega}
      </div>
    </div>
    <div class="container py-5">
      <div class="row">
        <div class="col-md-3">
          <ul class="nav flex-column">
            <li class="nav-item">
              <a href="/cgi-bin/indeeeex.py" class="nav-link">Home</a>
            </li>
            <li class="nav-item">
              <a href="/cgi-bin/tasks.py" class="nav-link">Tasks</a>
            </li>
          </ul>
        </div>
        {rega1}
      </div>
    </div>
  </div>
  <script>{js1}</script>
  <script>{js2}</script>
  <script>{js3}</script>

</body>
</html>
'''

if user != None:
	registr = ""
	registr1 = """
	<div class="col-md-9">
        	<h3>vi zashli {username}</h3>
        <div>
    """
	

print('Content-type: text/html\n')

print(pattern.format(rega = registr,rega1 = registr1.format(alerttext = alert, username = user), css = csspatt, js1 = jspattboot, js2 = jspattjquery, js3 = jspattpoper))
#print(pattern.format(publish=pub.format(alerttext = alert, username = user)))