import sys
import os
import subprocess
import re

gruppe = { 'student1': 'Asim Tariq', \
			'student2': 'Jaron Larsen', \
}

#Oppgave 1
def lab3_scripts():
	subprocess.call (['Scripts/test1.pl']) #henter perl filen
	subprocess.call (['Scripts/test1.sh']) #henter bash filen
	subprocess.call (['Scripts/test1.py']) #henter python filen
print lab3_scripts()

#Oppgave 2
def min_sys_info():
	print "her kommer min sys.info"
	print "byteorder: " + sys.byteorder
	print "os data: "
	print os.uname()
	print "os bruker: " + os.getlogin()
min_sys_info() #kaller opp funksjonen

#Her er output:
#('Linux', 'Asim', '2.6.32-431.3.1.el6.x86_64', '#1 SMP Fri Jan 3 21:39:27 UTC 2014', 'x86_64')
#os bruker: root

#Oppgave3
#Oppgave 3
def initialer(name):
	l = name.split()
	#for word in l:
		#print word     

	return ("%s.%s") %(l[0][0], l[1][0])

#Oppgave 4
#def infix_to_prefix(infix):



	print 5*"-" + " Studenter: " + 5*"-"
	for s in gruppe.values():
		if s is not "-":
			print s

print 5*"-" + " mysysinfo() " + 5*"-"
print min_sys_info.__doc__
min_sys_info()

print 5*"-" + " initialer() " + 5*"-"
print initialer("Asim Tariq")

print 5*"-" + " infix_to_prefix() " + 5*"-"
print infix_to_prefix("2/3")

# Kalle opp din lab3_scripts() funksjon her
print 5*"-" + " lab3_scripts() " + 5*"-"


