print("Wellcome to Icode guru")
print(20 + 30)
# print two or more thing once
print("wellcome icode guru" , 50)
print("hello","world",121)
# check comperision through print
print(3>2)
# Variabl in python
"""
python make address of value other language like c ,cpp ,java make the address of varialble name 
in python a = 10 ,b = 10 its store in same address other store in different adress

variable not start with number or special char , not allow space in variable name , under score use in 
variable name
"""
a = 10
b = 10
print(a,b)
# how to check address
print("address of a",id(a))
print("address of b",id(b))
b = "hello"
print(id(a),id(b))
# String concatenation of string
# all must be string to concatenate
a = "hello"
b = "students"
print(a+b)
# for space
print(a +" "+b)
# Operator in python
# 1.Arithmetic operators
a = 15
b = 2
# addition
print(a+b)
# multiplication
print(a*b)
# subtraction
print(a-b)
# division
print(a/b)
# modulus  , give reminder
print(a%b)
# exponent
print(a**b)
# floor division , division without decimal
print(a//b)
# assignment operators
a = 10
print(a)
a += 3 # same as a = a + 3
print(a)
a -= 5 #same as a = a - 5
print(a)
# comparison operators , compare the values
x = 10
y = 10
z = 11
a = 9
# ==  , equal
print(x==y)
print(y==z)
# != , not equal
print(x!=y)
print(x!=z)
# >  , greater than
print(x>y)
print(z>y)
# <  , less than
print(x<y)
print(x<a)
# >=  , greater than or equal to
print(x>=y)
print(x>=z)
# <=  , less than or equal to
print(x<=y)
print(x<=z)
print(y<=a)
# logical operators  , used for more than one condition
x = 10
y = 20
# and(&) , all condition true give true
print(x==10 and y>x and y==20)
print(x==10 and y>x and y==x)
# or(|) , at least one condition true give true
print(x==10 or y>x or y==x)
print(x==50 or y<x or y==21)
# not  , reverse the condition result
print(not(x==50 or y<x or y==21))
# membership operators
string = 'ARSLAN'
A = [12,3,9,5]
# in   , returns true if a sequence with the specified value is present in the object
print(1 in A)
print(12 in A)
print("A" in string)
# not in  , returns true if a sequence with the specified value is not present in the object
print("for not in")
string = 'ARSLAN'
A = [12,3,9,5]
print(1 not in A)
print(12 not in A)
# identity operator
x = 10
y=10
z = 2
# is  , returns true if both variables are the same object
print(x is y)
print(x ==y )
print(z is y)
# is not  , returns true if both variables are not the same object
print(x is not y )
print(x!=y)
print(x is not z)

# bitwise operators (work on binary digit (also used truth table ))  (0 = fa1se , 1 = true , )

x = 10
y = 8
# to find binary use bin() function.
print(bin(x))
print(bin(y))
# & (and) give true when both side have 1.
print(bin(x&y),x&y)
# | (or) give true when at least one side have 1.
print(bin(x|y),x|y)
# ^ (xor) give true when one side have 1 and other have 0.
print(bin(x^y),x^y)

# python data types
# 1.numeric
# i.integer
# ii.float
# iii.complex numbers
# 2.sequence type
# i.string
# ii.list
# iii.tuple
# 3.dictionary
# 4.set

# python divide the datatypes in two catagories

# 1.mutable object : can change its state or contents
# list
# dictionary
# byte array  (make it in numpy libraries)

# 2.immutable objects : cannot change its state or contents
# int
# float
# complex
# string
# tuple
# set

# integer (int)
a = 3
print(a,"is of type" ,type(a))
# float
a = 3.01
print(a,"is its tpye",type(a))
# complex
a = 3 + 5j
print(a,"ist type is",type(a))

# string: string is a collection of one or more characters put in a single quote, double quote or triple quote
# multi-line strings can be denoted using triple quotes, """or"""

s = 'hello#12'
print(s, "its type" , type(s))
s = "hello @ 23"
print(s, "its type is", type(s))
s = """
    hello 
    wellcome in i_code guru family 
    
"""
print(s,"its type", type(s))
# list : is an ordered sequence of items.
# it is one of the most used datatype in python and in very flexible.
# it is hettrogneous: store any type of value
# it is mutable
# []
l = [1,2,"ab",2.2]
print(l, "its tpye",type(l))
l[1]= "icode guru"
print(l,type(l))

# tuple : is an ordered sequence of items as a list
# it is defined within parentheses () where items are separated by commas
# it have more than one values
# it is also hetrogneous
# it is fast than list
# it is immutable object

t = (1,32,"hello")
print(t,type(t))
# dictionary is an unordered collection of key-value pairs.
# in python , dictionaries are defined within braces {} with each item being a pair in the form of key : value
# it has uniqe key
# it is mutable

d = {
    "course_name" : "python for biggner",
    "course_duration" : "2  months"
}
print(d,type(d))
print(d[ "course_duration"])

# set : is an unordered collection of items.
# every set element is unique and must be immutable
# {}  (without key-values pairs)

s = {2,3,3,3,3,3,4,5,4,4,5,56,4}
print(s,type(s))

# user input and type casting
# user input have only string value we type cast it
# i = input("enter your number:-")
# i1 = input("enter your second number:-")
# print(i + i1) # it use as string and concatinate it

# int() it type cast integer value, float() it type cast float value, eval() it type cast every numeric value

# i = int(input("enter your number:-"))
# i1 = int(input("enter your second number:-"))
# print(i + i1)
#
# i = eval(input("enter your number:-"))
# i1 = float(input("enter your second float number:-"))
# print(i + i1)

# python conditional statement ( used to manage outputs)
# if condition expression:
#   statement(s) to execute

a = 10
if a%2==0:
    print(a,"even number")


# b = int(input("enter your number:-"))
#
# if b%2 == 0:
#     print(b,"even number")
# else:
#     print(b,"odd number")


# when more than one condition is required
"""
if condition1 expression:
    statement(s) 
elif condition2 expression:
    statement(s)
elif condition3 expression:
    statement(s)
else:
    statement(s)
    
so on
"""

# per = int(input("enter your number:-"))
# if per >= 50:
#     print("first condition")
# elif per >= 30:
#     print("second condition")
# elif per >= 20:
#     print("third condition")
# elif per >=10:
#     print("fourth condition")
# else:
#     print("fail")

######*** project: How to Bulid simple calculator in python ****#######
#
# print('''
# + ADD
# - SUBSTRACT
# * MULTIPLY
# / DIVIDE
# ''')

# num1 = int(input("Enter the first value:-"))
# num2 = int(input("Enter the second value:-"))
# opr = input("Enter the operation(+,-,*,/):-")
# if opr == "+" :
#     print(num1 + num2)
# elif opr == "-" :
#     print(num1 - num2)
# elif opr == "*" :
#     print(num1 * num2)
# elif opr == "/" :
#     print(num1 / num2)
# else:
#     print("invalid operation....")

# we make it with only with if but that is slow w.r.t this

# loop in python

# for loop with range function (used most in to iterate the datatype and repeat the statement(s))

# range(start,end+1,increment) by defalt it start from zero and increment with +1

# reverse order of range function
# range (start , end , decrement) i.e range(10,0,-2)

# range(5)
# range(1,6)
# range(1,6,2)


# one parameter in range()
for i in range(5):
    print(i)

# two parameter in range()
for i in range(1,5):
    print(i)

# three parameter in range()
for i in range(1,7,2):
    print(i)

# only in python for , else

for i in range(1,3):
    print(i)
else:
    print(i,"for loop end")

# print(the table of any number)
# tb_n = int(input("enter which number table you want:-"))
# for i in range(1,11):
#     print(tb_n,"*",i,"=",tb_n*i)

"""
start
while condition:
    statement(s)
    increment/decrement

in python only 
while ,else exist

start
while condition:
    satement(s)
    increment/decrement
else:
   do any thing when while condition is false

"""


i = 1
while i <= 10:
    print(i,"wellcome to icode guru")
    i += 1

# while in reverse order

i = 5
while i >= 1:
    print(i)
    i -= 1

i = 3
while i >=1:
    print(i)
    i -= 1
else:
    print(i,"while loop end")

"""
string indexing and slicing 

string :  is a sequence of characters.

index by default  start form zero . in reverse order start from -1
"""

i = "wellcome to icodeguru"

#from left
print(i[6])

# from right
print(i[-12])

# slicing of string i[start:end+1:step_size]
print(i[1:2])
print(i[1:5:2])
print(i[1:])
print(i[:9:3])

# reverse slicing (step_size is negative)

print(i[-1::-1])

# string iteration in python

g = "wellcome to IcodeGuru"
t = len(g)
print(t)

for i in range(t):  # t = 21 , it give index number of each character of sttring

    print(g[i])

# reverse iteration

for i in range(t-1,-1,-1):

     print(g[i])

# reverse withm                                                                                                          out len() function

for i in g:
    print(i)

"""
string function in python

lower()
upper()
title()
capitalize()

# basic use when we want matching
# in database we search some thing that are in mix latter we convert it and apply our condition 
"""

g = "wellcome to IcodeGuru"

# convert into lower case
print(g.lower())
# convert into upper case
print(g.upper())
# convert each word first latter in upper case other  into lower case
print(g.title())
# convert first word first latter into upper case other into lower case
print(g.capitalize())

"""
string more function in python

find()
index()
isalpha()
isdigit()
isalnum()

"""

# find character index number in string (only first latter index give) , we give starting index i.e g.find("u",6)

print(g.find("I"))
print(g.find("u",19))
print(g.find("n"))  # if not found return -1

# same as find()
print(g.index("I"))
print(g.index("u",19))
# print(g.index("n"))  # if not found return error

# give true only when all is alphabet
s ="icodeguru"
print(g.isalpha())
print(s.isalpha())

# give true only when all is digit
a = "1223412"
a1 = "1223 412"
print(g.isdigit())
print(a.isdigit())
print(a1.isdigit())

# give true when all is digit or alphabet
a2 = "1243fff"
a3 = "2332 adfas"
a4 = "2332,dsfjas"
print(a.isalnum())
print(s.isalnum())
print(a1.isalnum())
print(a2.isalnum())
print(a3.isalnum())
print(a4.isalnum())

"""
string function in python (work on ascii number)

chr()   # take digit and give ascii character 
ord()  # take character give ascii digit(number) use one latter in single quotation 

"""

a=65
print(chr(a))

a = 'A'
ord(a)

"""
 string formating : set any placeholder in string
 
 the format() method formats the specified value(s) and insert them inside the string's placeholder.
 the placeholder is defined using curly brackets : {}.

"""

g = "wellcome {} to icodeguru {}".format("students",".")
print(g)
g = "wellcome {1} to icodeguru {0}".format("students",".") # use index for placeholder
print(g)
g = "wellcome {a} to icodeguru {b}".format(a="students",b=".") # use name for placeholder
print(g)
g = "wellcome {a:15} to icodeguru {b:8}".format(a="students",b=".")  # tell how many space you use
print(g)
g = "wellcome {a:<15} to icodeguru {b:8}".format(a="students",b=".")  # tell how many space you use , where character palce < (right)
print(g)
g = "wellcome {a:>15} to icodeguru {b:8}".format(a="students",b=".")  # tell how many space you use , where character palce > (left)
print(g)
g = "wellcome {a:^20} to icodeguru {b:8}".format(a="students",b=".")  # tell how many space you use , where character palce ^ (middle)
print(g)

"""
list in python - []
list is hatrogenous , any type of data 
list is mutable  , list is comma separated  
indexing and slicing same as string
"""
l = [1,2,3,4,"hello",3.0]
l1 = ["student" , 1 , 3 , [2,4] , {"A":"hello" , 3:7} , {2,3,3,42,3} , (23,23,42,12)]

# indexing in list start from 0 end n-1
print(l[0])
print(l[3])
print(l1[1])
print(l1[0])
# indexing of nested list
print(l1[3][1])

# slicing in list l[start:end+1:step]

l = [2,3,5,6,8,"hello","student"]

print(l[1:])
print(l[2:5])
print(l[1:6:2])

# reverse order of slicing

print(l[-1: :-1])
print(l[-1:-7:-3])

# list iteration

l = [10,20,30,40,50,60,70]

for i in range(len(l)):
    print(i ," - " , l[i])

for a in l:
    print(a)

# reverse iteration in list

for i in range(len(l)-1 ,-1,-1):
    print(l[i])

for i in range(-1 , - (len(l) +1) , -1):
    print(l[i])

"""
list function 
 function for delete list element
     1. del 
     2. pop()
     3. remove()
     4. clear()
     
 function for update element from list
   1. insert()
   2. append()
   3. extends()
 
 more function of list
  1. count()
  2. max()
  3. min()
  4. sort()
  5. reverse()
  6. index  
 
"""

# del
l = [10,20,30,40,50,60]
print(l)
del l[3]
print(l)

# pop() use index , it tell which value is deleted
print(l)
print(l.pop(1))
print(l)

# remove() use value
l.remove(30)
print(l)

# clear() remove all element of list
l.clear()
print(l)

# how to replace (or update value in list)  l[index]=value

l = [10,20,30,40]
l[0] = 99
print(l)

# insert value in any index l.insert(index,value)
l.insert(1,55)
print(l)

# append add any thing last of the list l.append(value)
l.append([3,5,7])
print(l)
l.append(2)
print(l)

# extend extend the list it enrape every thing list,tuple,set,dictionary etc and append into list l.extend(argument)
l1 = 3,5
l = [2,3,4,5,[2,3,5]]
l.extend(l1)
print(l)

# count() tell how many time a particular value repete in list (string etc) l.count()
a = [10, 10, 10,20,42,23 ,10 ,123,10]

b=a.count(10)
print(b)

# max give maximum number (in string according to alphabet)  , max(l)
print(max(a))

# min give minimum number  (in string according to alphabet ) , min(l)
print(min(a))

# sort  arrange the value in asscending order default l.sort()
a.sort()
print(a)

# reverse  the element last in first place and so on  l.reverse()
a.reverse()
print(a)
l= ["hello","world"]
l.reverse()
print(l)

# index tell the index of value l.index(value)
c = l.index("world")
print(c)

"""
list comprehension elegant way to create lists
  1.list comprehension is elegant way to define and create lists based on existing lists
  2.list comprehension is generally more compact and faster than normal functions and loops for creating list.
  
  [expression for item in list]
"""
# normal way
l = []
for a in range(1,101):
    l.append(a)
print(l)

# list comprehension method
l1 = [a for a in range(1,101)]
print(l1)
# also used condition (filter)
l1 = [a for a in range(1,101) if a%2==0 ]
print(l1)

# convert string into list

s = "icode guru"
l = [i for i in s]
print(l)

# how to iterate 2+ lists at the same time
# with zip() function (all lists have same elements otherwise it ignore the remaing elements)
l = [10,20,30,40,50]
l1 = [2,4,7,6,77]

for a,b in zip(l,l1):
    print(a,b)

# with range function

t = len(l)
for i in range(t):
    print(l[i],l1[i])

# convert string into list

# n = input("enter the value")
# print(n)
# l = n.split()
# print(l)

# user give more than one inputs

# l = []
# for a in range(1,4):
#     n = input("enter the value"+str(a)+":-")
#     l.append(n)
# print(l)

# implement a stack and queue using list data type

"""
stack in python
    the stack is a linear data structure.
    stores items in a last-in/first-out (LIFO) or first-in/last-out(FILO) manner.
    
 stack operation
    1. push => inserting an element
    2. pop => deletion an element(last element)
    3. peek => display the last element
    4. display => display list
"""

# l = []
# while True:
#     c = int(input("""
#     chose your opr
#     1 push elements
#     2 pop elements
#     3 peek element
#     4 display stack
#     any other int exit
#
#     """))
#
#     if c == 1:
#         n = input("enter the value:-")
#         l.append(n)
#         print(l)
#     elif c == 2:
#         if len(l) == 0:
#             print("empty stack:-")
#         else:
#             p=l.pop()
#             print(l)
#
#     elif c == 3:
#         if len(l) == 0:
#             print("empty stack")
#         else:
#             print("last stack value:-",l[-1])
#     elif c == 4:
#         print("display stack: ",l)
#     else:
#         break

"""
queue in python 
    the queue is linear data structure.
    stores items in first in first out (FIFO) manner
    
 queue operations.
    1. enqueue : adds an item
    2. dequeue : removes an item from the queue
    3. front : get the front item from queue
    4. rear : get the last item form queue
"""


# l = []
# while True:
#     c = int(input("""
#     1 push element
#     2 pop first element
#     3 front element
#     4 last element
#     5 display queue
#     6 exit
#      chose your opr...
#     """))
#     if c == 1 :
#         n = input("enter the value:-")
#         l.append(n)
#         print(l)
#     elif c == 2:
#         if len(l) == 0:
#             print("empty queue")
#         else:
#             del l[0]
#             print(l)
#     elif c == 3:
#         if len(l) == 0:
#             print("empty queue")
#         else:
#             print("first element of queue: ",l[0])
#     elif c == 4:
#         if len(l) == 0:
#             print("empty queueL:")
#         else:
#             print("last element of queue: ",l[-1])
#     elif c == 5:
#         print("display queue: ",l)
#     elif c == 6:
#         break
#     else:
#         print("invalid opr...")

"""
dictionary 

    unordered data type
    key value pair 
    define in {}
    key must me unique
    mutable
    exp d = {
        "name":"python" , "fees": "free" , "duration":"2 months"
    }
    
function of dictionary

    1. get()
    2. keys()
    3. values()
    4. items()
    5. del
    6. pop()
    7. dict()
    8. update()
    9. clear()
"""

# how to get value from dic   d[key]

d = {
        "name":"python" , "fees": "free" , "duration":"2months","platform":"icodeguru"
    }
print(d["name"])

# get all keys than value
for i in d:
    print(i ,d[i] )

# get() give value take argument key
n = d.get("name")
print(n)

# keys() extract all keys
for i in d.keys():
    print(i)

# values() extract all values

for i in d.values():
    print(i)

# items() give the pair of key and value
for a,b in d.items():
    print(a,b)

# deletes the values of dic  del and pop() use both take key
# del
del d["fees"]
print(d)
# pop() delete the value  and tell what delete
a = d.pop("duration")
print(a)
print(d)

# dict() use to make dictionary d = dict(name = python , duration= "2month" )

d = dict(name= "python", duration = "2month" )
print(d)

# update() replace the exiting value or add new values
d.update({"name":"dsa"})
print(d)

# other way
d[123]=1345
print(d)

# clear()

d.clear()
print(d)

# insert the new element in dictionary
d[123] = 123
print(d)

# nested dictionary
course = {"python":{"duration":'2month' , "platform":'icodeguru'},
          "java":{'duration':'3month' , 'platform':'icodeguru'},
          "php":{"duration":'1month' , "platform":'icodeguru'}
          }
print(course)
print(course['php'])
print(course['php']['duration'])

# iterate using for loop

for k,v in course.items():
    print(k,v,v['duration'])

# update and delete in dict
del course['java']['duration']
print(course)
course['php'].pop('duration')
print(course)

course['php'].update({"fees":'free'})
print(course)
course['java']['duration']="5month"
print(course)

d = {
        "name":"python" , "fees": "free" , "duration":"2months","platform":"icodeguru"
    }

# in this method we also make emojis converter

# ip = input("> ")
#
# word = ip.split()
# n = ""
# for i in word:
#     n += d.get(i,i) + " "
# print(n)

"""
tuple 
    order data type
    define ()
    hettrogenuous ( take all type of data)
    immutable
    it take more than one value with comma separated ( other wise not tuple)
     
    function of tuple
        min()
        max()
        count()
        index()
        sum()    only work on numbers
"""

t = (2,3,4,5,"hello",False,True,2.3,3.5)
print(t)
print(type(t))  # type() use to find the type of variable
# iteration same as list


"""
set
    unorder 
    unindex
    set() or {} like {2,3,4,'hello'}
    no repeated element show
    any individual  value of set is not change it may be delete 
    function in set
        sets()
        add()
        pop()        # remove random element and we print what value delete
        remove()  # remove element butt if element not available give error
        clear()
        discard()    # remove element butt if element not available not raise error
        update()     # to add list in set
"""

l = [1,2,3,4,5]
s = set(l)
print(s)

s.remove(2)
print(s)

s.discard(3)
print(s)

s.add(3)
print(s)

s.pop()
print(s)

l = [3,4,56,7]
s.update(l)
print(s)

s.clear()
print(s)

"""
user define function
    a function is a block of statements which can be used repetitively in a program. 
    it saves the time of a developer. in python concept of function is same as other languages 
    you can pass data, kown as parameters, into a function.
    # creating a function .
    in  python a function is defined using the def keyword.

     def    # word use to define function def function_name(parameters):

    simple function 
    function with argument
    return function
    
"""
# creating a function
def data():
    print("welcome to icode guru")
# calling a function
data()

# function with arguments
# information can be passed to function as parameter
def sum(a,b):
    print(a+b)
sum(10,29)

# default parameter value
def sum(a,b=1):
    print(a+b)

sum(20)
sum(23,3)

# return values
# to let a function return a value, use the return statement

def square(x):
    return x*x

f = square(3)
print(f)
print(square(2))

# multiple return
def square(x):
    return x*x , x*2

f = square(3)
print(f)
print(square(2))

"""
module in python
    module have two type
        1. predefine
        2. user define 
    module use for to reuse class , variable and function 
    
    first module create(file of .py)
    then import
    for calling the name of file is module name 
"""
# 2. user define module
import module

print(module.sum(12,3))
print(module.mul(12,23))

import module as m

print(m.sum(12,3))
print(m.mul(12,23))


# to use specific function of module
from module import sum
print(sum(2,3))

from module import *    # * import all function of the module

print(mul(3,4))

print(dir(module))   # print the name of function of module

# 1. predefine( inbuilt ) module
# math module in python
import math
x = 10.5
print(math.ceil(x))   # ceiling function : least integer that is greater or equal to x

x = -10
print(math.fabs(x)) # absolute functon: give positive value

x = 3
print(math.factorial(x))   # factorial function : 3! = 3*2*1 , 0! = 1

x = 5.6
print(math.floor(x))   # floor function : greatest integer that less  or equal x

l = [2,3,5,5,3.3333]
print(math.fsum(l))   # return an accurate floating point sum of value in the iterable

x = 36
print(math.sqrt(x))  # return the under root

# random module in python
# generate the random value of float, int, or list element ,or shuffle the list element

# randint() method: return a number between 5 and 10 (both include)
import random
n = random.randint(5,10)
print(n)

# randrange() method: return a number between 5(include) and 10(not include)
n1 = random.randrange(2,4)
print(n1)

# choice() method: return a  random number  form a list (most useable)
l = [10,20,30,40]
n2 = random.choice(l)
print(n2)

# random() returns a random float number between 0 and 1
r = random.random()
print(r)

# shuffle takes a sequence and return the sequence in random order
l = [1,2,3,4,5,6,7]
random.shuffle(l)
print(l)

# uniform() return a random float number between two given parameters
u = random.uniform(2,8)
print(u)

# date and time module
import datetime

# datetime.now() system date and time ; the date contains year , month , day , hour, minute, second, and microsecond
x = datetime.datetime.now()
print(x)

# create date and time object      datetime.datetime()
# x =  datetime.datetime(2018,4,5)
# print(x)

"""
strftime()
    takes in parameter,format, to specify the format of the returned string:
        %b month name , short version dec
        %B month name , full version december
        %m month as number 01-12        12
        %y year , short version, without century 22
        %Y year , full version 2022
        %H hour 00-23       13
        %I hour 00-12   03
        %p am/pm    pm
        %M minute 00-99
        %S second 00-59  08       
"""
s = x.strftime("%S")
print(s)

#####**** project: random number guessing number game(using random module)  ****#####

# import random as r
# count = 1
# chance = 3
# while count <= chance :
#     computer_number = r.randrange(1,51)
#     user_input = int(input("Enter your number between 1 and 50:> "))
#     if computer_number>user_input:
#         print("Computer Number: ",computer_number)
#         print("Your Number is to low: ")
#     elif computer_number<user_input:
#         print("Computer Number: ", computer_number)
#         print("Your Number to high: ")
#     else:
#         print("Computer Number: ", computer_number)
#         print("Yes! You Won! :)")
#         break
#     count += 1
# else:
#     if count == 4 :
#         print("Your chance is ended:")


#####**** project: Rock Paper Scissors game (using random module) ****#####

# import random
# l = ["rock" , "scissor" , "paper"]
#
# """
# Winning Rules as follows:
#     Rock vs paper -> paper wins.
#     Rock vs scissor -> Rock wins.
#     paper vs scissor -> scissor wins.
# """
# while True:
#     uc = int(input('''
# Game start....
# 1 Yes
# 2 No | Exit
#     '''))
#
#     if uc == 1:
#         ucount = 0
#         ccount = 0
#         for i in range(1,6):
#             userInput = int(input('''
# 1 Rock
# 2 Scissor
# 3 Paper
#             '''))
#
#             if userInput == 1:
#                 uchoice = "rock"
#             elif userInput == 2:
#                 uchoice = "scissor"
#             elif userInput == 3:
#                 uchoice = "paper"
#             else:
#                 print("Invalid choice")
#                 continue
#
#             Cchoice = random.choice(l)
#
#             if uchoice == Cchoice:
#                 print("Computer Value: " , Cchoice)
#                 print("User Value: ", uchoice)
#                 print("Game Draw!")
#                 ucount += 1
#                 ccount += 1
#             elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
#                 print("Computer Value: " , Cchoice)
#                 print("User Value: ",uchoice)
#                 print("You Win! :) ")
#                 ucount += 1
#             else:
#                 print("Computer Value: ", Cchoice)
#                 print("User Value: ", uchoice)
#                 print("Computer Win! :( ")
#                 ccount += 1
#
#         if ucount == ccount:
#                 print("Final Game is Draw....")
#                 print("User Number ",ucount)
#                 print("Computer Number ",ccount)
#         elif ucount > ccount:
#                 print("Final Game You Won!....")
#                 print("User Number ", ucount)
#                 print("Computer Number ", ccount)
#         else:
#                 print("Final Game Computer Won :( ....")
#                 print("User Number ", ucount)
#                 print("Computer Number ", ccount)
#     else:
#         break

# pickle module
import pickle
l = [10,20,30,30,40]
file = open("write.txt" , "wb")    # "wb" write in binary mode
pickle.dump(l,file)

file = open("write.txt","rb")     # "rb" read binary mode
l = pickle.load(file)
print(l)


'''
json (javascript object notation)
it is mainly used for storing and transferring data between the browser and the server.
json is text written with javascript object notation
python too support jason with a built-in package called json.
json support mainly 6 data types:
    1. string
    2. number
    3. boolen
    4. null 
    5. object
    6. array
    
in python, json exists as a string.for example
p = '{"name":"icode" , "language" : ["python" , "java"]}'
'''
import json
d = {
    'course_name':'python' ,
    'fees':'free' ,
    'platform':' icodeguru'
}

f = json.dumps(d)
print(type(f))
print(f)

# converting json to python objects
# if you have json string you can parse it by the json.loads() method.
d = '{"cname":"python" , "fees":"free" , "duration":"2M"}'
print(type(d))

x = json.loads(d)
print(x)
print(type(x))
for i,j in x.items():
    print(i,j)

# writing and reading(convert into python object) json file

with open("demo.json" , "w+") as file:

   file.write(f)
   file.close()

data = open("demo.json","r")
file = data.read()
finalFile = json.loads(file)
print(finalFile)

"""
object oriented programing (class and object)
    class word used to declearing class
    we give the name camel(first letter of each word capital) case to class
    function inside class is known as method
"""

class DemoClass:
    a=19

    def sumvalue(self):
        print(29+1)
demoobject = DemoClass()  # make as many object as you want
print(demoobject.a)
demoobject.sumvalue()

# method (we make and call it to take output) and constructor(we make by python keyword and not call to take output)
class Democlass:
    def __init__(self):
        print("hello, this is constructor")
    a = 10
    def showvalue(self):              # method
        self.c = self.a * self.a
        print(self.c)

    def showvalue1(self):
        print("wellcome to icodeguru")

    def sum(self,a,b):
        print(a+b)

obj1 = Democlass()
obj1.showvalue()
obj1.showvalue1()

#   inheritance (parent to child) in python: in this way we use all the method and variable in our child class
class A:
    def displayA(self):
        print("class A display method")

class B(A):
    def displayB(self):
        print("class B display")

obj1 = B()
obj1.displayA()

# multiple level inheritance
class C(B):
    def displayC(self):
        print('class c display method')
obj1 = C()
obj1.displayB()
obj1.displayA()
obj1.displayC()

class D:
    def displayD(self):
        print('display d class')

# multiple inheritance
class E(A,D):
    def displayE(self):
        print('e class display')

obj2 = E()
obj2.displayA()
obj2.displayD()
'''
 encapsulation: (hide the implementation)
 
 an objects variables should not always be directly accessible
 
 the methods can ensure the correct values are set. if an incorrect value is set, the method can return an error.
 
     make your variable and method private  (use into inside class not in object)
    
  
'''
class Student:
    __name = "Ahmed"   # __ mean private
    def __init__(self):   # constructor
        print(self.__name)  # use private inside the class
    def __displayinfo(self):
        print("private method")
    def info(self):
        print(self.__displayinfo())
obj = Student()
obj.info()


# encapsulation (getter and setter)
class Student:
    def __init__(self):
        self.__name = ""          # __ mean private variable
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name

obj3 = Student()
obj3.setname("Arslan")
print(obj3.getname())

'''
 polymorphism
     polymorphism means same function name but different signatures being uses for different types
     
     1. function overloading  (depend on parameter)
        method overloading is one concept of polymorphism
        it comes under the elements of oops
        it is worked in the same methid names and different arguments
        arguments different will be based on a number of argument and types of arguments
         # in same function we use parameter the output is change
     2. function overriding 
        method overriding is the methid having the same name with the same arguments
        it is implemented with inheritance also.
        it mostly used for memory reducing processes
      #  if function are same name in two class  and inherit parent  to child
        it overwrite the parent class function with child class function 

'''
# exp
l = [1,3,4,5,6]
print(len(l))
s = "string"
print(len(s))

# overloading
class Icode:
    def display(self,name = ""):
        print("welcome to icode guru"+" "+name)
obj=Icode()
obj.display()
obj.display("Ahmed")

class Area:
    def find_area(self,a = None , b = None):
        if a!=None and b!=None:
            print("area of rectangle: ",(a*b))
        elif a!=None:
            print("area of square: ", (a*a))
        elif b!=None:
            print("area of square: " , (b*b))
        else:
            print("nothing")

obj = Area()
obj.find_area()
obj.find_area(3)
obj.find_area(2,4)

# overriding
class ICG:
    def display(self):
        print("from icg")
class A(ICG):
    def display(self):
        print("from A")
obj=A()
obj.display()


# you want to use parent class function than use super().function_name()
class ICG:
    def display(self):
        print("from icg")
class A(ICG):

    def display(self):
        super().display()
        print("from A")
obj=A()
obj.display()


#####****  project:  A Bike Rental System ****#####

# class BikeShop:
#
#     def __init__(self,stock):
#         self.stock = stock
#
#     def displaybike(self):
#         print("Total Bikes: " , self.stock)
#
#     def rentForbike(self,quantity):
#         if quantity<=0:
#             print("Enter the quantity positive or greater than Zero:")
#         elif quantity>self.stock:
#             print("Enter the quantity less then stock: ")
#         else:
#             self.stock = self.stock-quantity
#             print("Total price:" , 100*quantity)
#             print("Total Bikes:", self.stock)
#
# while True:
#     obj = BikeShop(100)
#     uc = int(input('''
# 1. Display Stock
# 2. Rent a Bike
# 3. Exit
#     '''))
#     if uc == 1:
#         obj.displaybike()
#     if uc == 2:
#         n = int(input("Enter The Quantity..."))
#         obj.rentForbike(n)
#     else:
#         break


"""
python errors and built in Exception
python errors can be broadly classified into two classes:
1. syntax errors  (it can never be handle we correct it)
2. logical errors (exception)
"""
# python syntax errors
# print("ab)

# logical errors ( Exception )
# print(1/0)  # Zero division error: division by zero
# l = [1,2,3,4]
# print(l[6])  # index error

"""
python Exception handling
1. ZeroDivisionError
    print(10/0)
2. NameError
    use variable that not decleared
3. TypeError
    print(10 + "10")
4. ValueError
    a = int(input())
    user give the string it give valueError
5. IndexError
    l = [1,2,3,4]
    print(l[6]) index out of range
    it give indexerror
6. KeyError
    d = {"a": 199, 18:12 , "b':23}
    print(d['c']
    give key error
7. ModuleNotFoundError
    make module of icodestudent name
    import icode
    it give module not found error
8. ImportError
    make module of cal and make sum method in it
    from cal import sum1
    it give import error
    
"""
try:
    l = [1,2,3,4,5,6]
    print(l[5])
except Exception as e:
    print(e)
finally:
    print("execute every time")

