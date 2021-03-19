file = open("in", 'r')
string = file.read()
file.close()
file = open("out2", 'w')
a, b = string.split(" ")
if a < b:
	file.write("<")
elif a > b:
	file.write(">")
else:
	file.write("=")
file.close()
