##Define a function:
##Define a function:
def function_name(parameter_1,parameter_2):
     {this is the code in the function}
     {more code}
     {more code}
     return {value to return to the main program}
{this code isn't in the function}
{because it isn't indented}
remember to put a colon ':' at the end of the line that starts with 'def'

def Area(a,b):
  area=a*b"
  return area

Area(4,6)
print "Area(4,6)=", Area(4,6)


##Tuple: ()
#define a tuple:

months = ('January','February','March','April','May','June',\
'July','August','September','October','November','December')

print months


##List: []
cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']

#direct index at #-1
print cats[2]

#range index i starts with 0.
print cats[0:2]

cats.append('Catherine')
print cats

del cats[0]
print cats

##Dictionary: {}
#Make the phone book:
phonebook = {'Andrew Parson':8806336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345}

#Add the person 'Gingerbread Man' to the phonebook:
phonebook['Gingerbread Man'] = 1234567
print phonebook

#delect 'Andrew Parson':
del phonebook['Andrew Parson']
print phonebook
 

###A few examples of a dictionary

#First we define the dictionary
#it will have nothing in it this time
ages = {}

#Add a couple of names to the dictionary
ages['Sue'] = 23
ages['Peter'] = 19
ages['Andrew'] = 78
ages['Karren'] = 45

#Use the function has_key() - 
#This function takes this form:
#function_name.has_key(key-name)
#It returns TRUE
#if the dictionary has key-name in it
#but returns FALSE if it doesn't.
 
print ages.has_key('Sue')
#Remember - this is how 'if' statements work -
#they run if something is true
#and they don't when something is false.
if ages.has_key('Sue'):
    print "Sue is in the dictionary. She is", \
ages['Sue'], "years old"

else:
    print "Sue is not in the dictionary"


#Use the function keys() - 
#This function returns a list
#of all the names of the keys.
#E.g.
print "The following people are in the dictionary:"
print ages.keys()

#You could use this function to
#put all the key names in a list:
keys = ages.keys()
print keys

#You can also get a list
#of all the values in a dictionary.
#You use the values() function:
print "People are aged the following:"
print ages.values()

#Put it in a list:
values = ages.values()

#You can sort lists, with the sort() function
#It will sort all values in a list
#alphabetically, numerically, etc...
#You can't sort dictionaries - 
#they are in no particular order
print keys
keys.sort()
print keys

print values
values.sort()
print values

#You can find the number of entries
#with the len() function:
print len(ages)
print "The dictionary has", \
len(ages), "entries in it."
