#CHEAT SHEET
x = 3 #No need to declare types in python!
y = -1500
z = 13.4

exampleArray = [x, y, 27, 89, z]

exampleArray.append() #add something to the end of an array
len(exampleArray) #find how many items are in an array!
exampleArray[3] #index into an array (REMEMBER indexing starts at 0!)

def foo(a, b, c): #declare a method like this.
	blah = a - b #do stuff in the method.
	return blah / c

foo(x, y, z) #calling a method is easy!

if 7 > 4: #options: <, >, <=, >=, ==
	alpha = 50 / 4 #no brackets in python. Just tab everything that's supposed to be in the if statement
	if x == y: #remember you can nest if statments! 
		print "blah blah"
	else:
		print "hello!"

for number in exampleArray: #for each number in the example array
	print number

for number in range(0, 10): #for each number between 0 and 10
	if exampleArray[number] < 15000:
		print ":)"

#Pixels are between 0 and 255. (red, green, blue) 
#(255, 0, 0) is red    (0, 255, 0) is green      (0, 0, 255) is blue
#(255, 255, 0) is yellow        (0, 255, 255) is cyan         (255, 0, 255) is purple
 