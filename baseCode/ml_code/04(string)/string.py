# coding=utf-8
# name = 'dave'
# print name[-2]
#
# s = "<any string>"
#
#
# print s[0]
# print (s+s)[0]
#
# print (s+'ity')[1]
# print s[1]

# 选择子序列
# word = 'assume'
# # print word[3]
# print word[3:4]
# print word[4:]
# print word[:3]
# print word[:]
#
# s ='audacity'
# print s
# print 'U'+ s[2:]
# print s[0:]
# print s[:-1]
# print s[:3]+s[3:]

#--------------------------------------------

s = 'asdfdsfdf'
s1 = "df"
print s.find(s1,3)

#----------------------------------------------

# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string

#返回 一个unicode
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str,str):   #如果是字符串
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value

# 返回字符串
def to_str(unicode_or_str):
    if isinstance(unicode_or_str,unicode): #如果是unicode
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value