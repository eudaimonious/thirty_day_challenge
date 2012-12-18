# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Margaret Scott

'''
Exercise 3.1

repeat_lyrics()
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

NameError: name 'repeat_lyrics' is not defined
'''

# Exercise 3.2

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

'''
The programs prints print_lyrics (the two strings) twice, for a total of four strings:
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.

'''

#Exercise 3.3

def right_justify(s):
    print " "*(70-len(s)) + s

right_justify('allen')

#Exercise 3.4

'''
#Part 1
def do_twice(f):
    f()
    f()
    
def print_spam():
    print 'spam'
    
do_twice(print_spam)
'''
#Part 2
def do_twice(f, v):
    f(v)
    f(v)
    
#Part 3
def print_twice(x):
    print x
    print x
'''    
#Part 4
do_twice(print_twice, 'spam')
'''
#Part 5
def do_four(a, b):
    do_twice(a, b)
    do_twice(a, b)

do_four(print_twice, 'Hello world!')

