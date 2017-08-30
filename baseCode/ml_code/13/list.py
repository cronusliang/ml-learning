# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?

# list1 = [1,2,3,4]
# list2 = [1,2,3,4]
#
# list1 = list1 + [5, 6]
# list2.append([5, 6])
#
# # to check, you can print them out using the print statements below.
#
# print "showing list1 and list2:"
# print list1
# print list2

# What is the difference between these two pieces of code?
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

def proc(mylist):
    mylist = mylist + [6, 7]

def proc2(mylist):
    mylist.append(6)
    mylist.append(7)

# Can you explain the results given by the print statements below?

print "demonstrating proc"
print list1
proc(list1)
print list1
print
print "demonstrating proc2"
print list2
proc2(list2)
print list2

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4,5]
list3 += [6, 7]

# Does this behave like list1 = list1 + [6,7] or list2.append([6,7])? Write a
# procedure, proc3 similar to proc and proc2, but for +=.

import random

# 1. Create random list of integers using while loop
random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0, 10))

# Write code here to loop through the list and count all occurrences
# of the number 9. Note that `if` statements and `while` loops will help you solve
# this problem.




# Test: If the `while` loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
print random_list


