# Here's a chance to play around with lists for a bit before you continue
# Take a look at what the following code does and try to guess how it works.

print "EXAMPLE 1: Lists can contain strings"
string_list = ['HTML', 'CSS', 'Python']
print string_list

print "EXAMPLE 2: Lists can contain numbers"
number_list = [3.14159, 2.71828, 1.61803]
print number_list

print "EXAMPLE 3: Lists can be 'accessed' and 'sliced' like how we accessed and sliced strings in the previous lessons"
pi = number_list[0]
not_pi = number_list[1:]
print pi
print not_pi

print "EXAMPLE 4: Lists can contain strings AND numbers"
mixed_list = ['Hello!', 42, "Goodbye!"]
print mixed_list

print "Example 5: Lists can even contain other lists"
list_with_lists = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']
print list_with_lists

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    return days_in_month[month_number - 1]


print how_many_days(1)
print how_many_days(9)

countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

print countries[1][1]

print countries[0][2] / countries[2][2]

stooges = ['Moe','Larry','Curly']

#['Moe','Larry','Shemp']
# stooges[2] = 'Shemp'
# print stooges
#
# spy = [0,0,7]
#
# def replace_spy(spy):
#     spy[len(spy)-1] = spy[len(spy)-1]+1
#     pass
#
# replace_spy(spy)
# print spy

p = [1,2]
p.append(3)
p = p + [4,5]
# print len(p)

def print_all_elements(p):
    i = 0
    while i< len(p):
        print p[i]
        i = i + 1


print_all_elements(p)