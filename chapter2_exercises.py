# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Margaret Scott
'''
Exercise 2.1
The interpreter is evaluating the integers as octal numbers due to the leading zero.
'''

'''
Exercise 2.2
The script has no output without a print statement.
'''
print 5
x=5
print x
print x+1

'''
Exercise 2.3
1. 8
2. 8.5
3. 4.0
4. 11
5. '.....'
'''

#Exercise 2.4
print (4.0/3.0) * 3.1415 * (5**3)
print "Answer to 1 is 523.58333..."
print (24.95 * .6) *60 + (3 + .75 *59)
print "Answer to 2 is 945.44999..."
start_in_seconds = (6*60+52)*60
easy_pace_in_seconds = 8 * 60 + 15
tempo_in_seconds =  7 * 60 + 12
finish_in_seconds = start_in_seconds + 2 * easy_pace_in_seconds + 3 * tempo_in_seconds
finish_hour = finish_in_seconds / 60**2
finish_minutes = (finish_in_seconds % 60 **2) / 60
print finish_hour,":",finish_minutes
print "Answer to 3 is 7:30"