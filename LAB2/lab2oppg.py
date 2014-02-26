import sys

#Oppgave 1
Gruppe = { 'student1': 'Asim Tariq', \
	   'student2': 'Jaron Larsen', \
 	  }

print "  \/_ "
print " \,   /( ,/ "
print "  \\\' /// "
print "   \_ /_/"
print "   (./"
print "    '`"


def ascii_fugl():
	pass



#oppgave 2

x=20
y=14

def bitAnd(x,y):    
	return x&y
print bitAnd(x,y)

#oppgave 3
# er identisk med oppg2

#oppgave 4


def bitXor (x,y):
	return x^y
print bitXor (x,y)

#oppgave 5


def bitOR (x,y):
	return x|y
print bitOR (x,y)

#oppgave 6

def ascii8Bin(a):
	bokstav=ord(a)
	bokstav="{0:08b}".format(bokstav)
	print (bokstav)
ascii8Bin("a")

#oppgave 7

def transferBin(string):
	l= list(string)
	a="{0.06b}".format("hi")
	for c in l: print (string)
ascii8Bin("hi")



#oppgave 8

def ascii2hex(x):
	aaa=ord(x)
	ascii2x= "{0:02x}".format(aaa)
	print (ascii2x)
ascii8Bin("x")




