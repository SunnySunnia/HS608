>>> type('hello, world')
<type 'str'>

>>> type("hello")
<type 'str'>

>>> type(17)
<type 'int'>

>>> type(3.3)
<type 'float'>

>>> print 1,000,000
1 0 0

>>> print 100,000,000
100 0 0

>>> message = "What's up, Doc?"
>>> n = 17
>>> pi = 3.14159

>>> print message
What's up, Doc?
>>> print n
17
>>> print pi
3.14159


Python has thirty-one keywords:

and	as	assert	break	class	continue
def	del	elif	else	except	exec
finally	for	from	global	if	import
in	is	lambda	not	or	pass
print	raise	return	try	while	with
yield

>>> 'Fun'*3
'FunFunFun'
>>> "Fun"*3
'FunFunFun'

>>> raw_input("Please enter your name: ")
Please enter your name:
''
>>> raw_input("Please enter your name: ")
Please enter your name: Sunny
'Sunny'
>>> raw_input("Please enter your name: ")
Please enter your name: 3
'3'
>>> raw_input("Please enter your name: ")
Please enter your name: 3*5
'3*5'

>>> input("Enter a numerical expression: ")
Enter a numerical expression: 3**5
243
>>>


>>> input("Enter a numerical expression: ")
Enter a numerical expression: Sunny

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    input("Enter a numerical expression: ")
  File "<string>", line 1, in <module>
NameError: name 'Sunny' is not defined

>>> input("Enter a numerical expression: ")
Enter a numerical expression: 3
3
>>> input("Enter a numerical expression: ")
Enter a numerical expression: "sunny"
'sunny'
>>> 

