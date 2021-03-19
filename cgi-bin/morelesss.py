import cgi, time, os, http.cookies, sqlite3

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

form = cgi.FieldStorage()
action = form.getfirst("action", "")

ansa =""
ans = ""

if action == "login":
	text1 = form.getfirst("TEXT_1", "")
	file1 = open("a2.py", "w")
	file1.write(text1)
	file1.close()
	os.system("gg2.py")
	file1 = open("ans2", "r")
	ans = file1.read()
	file1.close()
	ansa = """ <h3>rezalt = {ans1} </h3> """
		
	
check = ""
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

pattern = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>PyContester: A+B</title>
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
			<div>
				<a href="/cgi-bin/tasks.py" class="nav-link">Back</a>
			</div>
          <h3 class="mb-4">More-less</h3>
          <p style = "margin-left: 20px">One of the main operations with numbers is their comparison. We suspect that you are fluent in this operation and can compare any numbers, including whole numbers. In this problem it is necessary to compare two integers.</p>
		  <div>
				<h3>INPUT</h3>
				<p style = "margin-left: 20px">The two lines of the input file INPUT.TXT contain the numbers A and B, not exceeding in absolute value 2*10<sup>9</sup>.</p>
		  </div>
		  <div>
				<h3>OUTPUT</h3>
				<p style = "margin-left: 20px">Write in the output file OUTPUT.TXT one character "<", if A < B, ">", if A > B and "=" if A = B.</p>		
		  </div>

		  <br>
		  <br>
		  {checktext}
		  {ansatext}
		  
        </div>
      </div>
    </div>
  </div>
  <script> {js1}</script>
  <script> {js2}</script>
  <script> {js3}</script>
</body>
</html>
"""
if user is not None:
	registr = ""
	check = """
		<form action="/cgi-bin/ABtasks.py">
	<div class = "textcode">
		  
				<textarea rows="10" cols="80" name="TEXT_1" placeholder="Enter your code" wrap ="soft | hard" style = "resize: none;"></textarea>
		  </div>
	
			<input type="hidden" name="action" value="login">
        	<input type="submit">
		  </form>	  
		 """

print("Content-type: text/html\n")
print(pattern.format(ansatext = ansa.format(ans1 = ans),checktext = check, rega = registr, css = csspatt, js1 = jspattboot, js2 = jspattjquery, js3 = jspattpoper))