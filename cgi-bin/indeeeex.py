#!/usr/bin/env python3
import cgi, time, os, http.cookies
import random, base64, sqlite3
from PIL import Image, ImageDraw

form = cgi.FieldStorage()
with open("css/bootstrap.min.css") as f:
	csspatt = f.read()
with open("js/bootstrap.min.js") as f:
	jspattboot = f.read()
with open("js/jquery.min.js") as f:
	jspattjquery = f.read()
with open("js/popper.min.js") as f:
	jspattpoper = f.read()
from _wall import Wall
wall = Wall()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session = cookie.get("session")
if session is not None:
    session = session.value
user = wall.find_cookie(session)

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
	
pattern = """<!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Home</title>
  <style> {css}</style>
</head>
<body>
  <div class="layout">
    <div class="navbar navbar-dark bg-warning navbar-expand-lg">
        <div class="container">
        <a href="#" class="navbar-brand">Contester</a>
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
        <div class="col-md-9">
          <h3 class="mb-4">Home page</h3>
          <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Harum, officia officiis, veniam distinctio fugiat fugit excepturi perferendis sit exercitationem ullam ut eveniet sequi dolorum molestias totam illo consequuntur, eum dolore.</p>
        </div>
      </div>
    </div>
  </div>

  <script>{js1}</script>
  <script>{js2}</script>
  <script>{js3}</script>
</body>
</html>"""

if user is not None:
	registr = ""

print("Content-type: text/html\n")
print(pattern.format(rega = registr, css = csspatt, js1 = jspattboot, js2 = jspattjquery, js3 = jspattpoper))

