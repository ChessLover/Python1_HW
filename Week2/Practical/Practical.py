#--------------------------------------------------------
# Problem 1

import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

print(yesterday)

#--------------------------------------------------------
# Problem 2

t1 = datetime.date(2021, 9, 11)
t2 = datetime.date(1999, 4, 26)

sub = t1 - t2
# This is the age of person born in April 26, 1999 in days. 
print(sub)
# This is the age of person born in April 26, 1999 in seconds. 
print(sub.total_seconds())

#--------------------------------------------------------
# Problem 3 

curr = datetime.datetime.now()
print(curr)
print(curr.year)
print(curr.month)
print(curr.isoweekday())

curr_sub_5 = curr - datetime.timedelta(days=5)
curr_add_5 = curr + datetime.timedelta(days=5)

print(curr_sub_5)
print(curr_add_5)

#--------------------------------------------------------
# Problem 4

import calendar

bd = datetime.date(1999, 4, 26)
print(bd)
print(bd.year)
print(bd.month)
print(bd.day)
print(bd.isoweekday())

days_left = datetime.date(2022, 4, 26) -  datetime.date.today()
print(days_left)

cal = calendar.month(2017, 5)
print(cal)

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

print(yesterday)

add_2 = yesterday + datetime.timedelta(days=2)
print(add_2)

sub_3 = yesterday - datetime.timedelta(days=3)
print(sub_3)

#--------------------------------------------------------