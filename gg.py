import os, sys, time, subprocess

number_task = 1
col = 1
filein = open("in", 'w')
filein.write("")
filein.close()

fileans = open("ans", "w")
filetask = open("task" + str(number_task), "r")
tests = filetask.read().split("""###\n""")
for i in tests:
	filein = open("in", 'w')
	filein.write(i)
	filein.close()
	os.system("a.py")
	os.system("b.py")
	file1 = open("out", 'r')
	file2 = open("out2", 'r')
	if file1.read() != file2.read():
		fileans.write("WA TEST " +  str(col))
		fileans.close()
		sys.exit()
	file1.close()
	file2.close()
	col+=1
fileans.write("OK")
fileans.close() 