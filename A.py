print "while loop example"
a=0
while a<10:
  a=a+1
  print a


#if {conditions to be met}:
#    {do this}
#    {and this}
#    {and this}
#{but this happens regardless}
#{because it isn't indented}
print "if loop example 1"
y = 1
if y == 1:
    print "y still equals 1, I was just checking"


print "if loop example 2"
print "We will show the even numbers up to 20"
n = 1
while n <= 20:
    if n % 2 == 0:
        print n
    n = n + 1
print "there, done."

#if {conditions}:
#    {run this code}
#elif {conditions}:
#    {run this code}
#elif {conditions}:
#    {run this code}
#else:
#    {run this code}
print "if-else"
a = 1
if a > 5:
    print "This shouldn't happen."
else:
    print "This should happen."


print "#else if--elif"
z = 4
if z > 70:
    print "Something is very wrong"
elif z < 7:
    print "This is normal"


#function_name(parameters)
#calculator program

#this variable tells the loop whether it should loop or not.
# 1 means loop. anything else means don't loop.

loop = 1

#this variable holds the user's choice in the menu:

choice = 0

while loop == 1:
    #print what options you have
    print "Welcome to calculator.py"

    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"

    print "3) Multiplication"

    print "4) Division"
    print "5) Quit calculator.py"
    print " "

    choice = input("Choose your option: ")
    if choice == 1:
        add1 = input("Add this: ")
        add2 = input("to this: ")
        print add1, "+", add2, "=", add1 + add2
    elif choice == 2:
        sub2 = input("Subtract this: ")
        sub1 = input("from this: ")
        print sub1, "-", sub2, "=", sub1 - sub2
    elif choice == 3:
        mul1 = input("Multiply this: ")
        mul2 = input("with this: ")
        print mul1, "*", mul2, "=", mul1 * mul2
    elif choice == 4:
        div1 = input("Divide this: ")
        div2 = input("by this: ")
        print div1, "/", div2, "=", div1 / div2
    elif choice == 5:
        loop = 0
	
print "Thankyou for using calculator.py!"


