#funksjonen plusser (a,b) og returnerer verdien
def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b
#funksjonen trekker fra (a,b) og returnerer verdien
def substract(a,b):
	print "SUBSTRACTING %d - %d" % (a,b)
	return a - b
#funksjonen ganger (a,b) og returnerer verdien
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b
#funksjonen deler (a,b) og returnerer verdien
def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b

print "la oss gjore litt matte funksjoner!"

alder = add(20,2)
hoyde = substract(78, 5)
vekt = multiply(49, 19)
iq = divide(100, 2)

print "alder: %d, hoyde: %d, vekt: %d, iq: %d" % (alder, hoyde, vekt, iq)

print "her er et puzzlespill."

what = add(alder, substract(hoyde, multiply(vekt, divide(iq, 2))))

print "det blir: ", what, "kan du gjore det?"


