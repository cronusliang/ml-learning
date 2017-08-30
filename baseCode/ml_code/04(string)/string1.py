
s = 'udacity'
t = 'bodacious'

# print s[0]
# print t[2:]
# print s[0]+t[2:]

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

# Use the string.find method to locate "NOUN" and "VERB"
# noun_position = text.find('NOUN')
# verb_position = text.find('VERB') #fill this in
#
# print noun_position
# print verb_position

text = "all zip files are zipped"
#text = 'zip files are zipped'     -> 14
#text = 'zip files are compressed'  -> -1
point = text.find('zip') + 1
print text.find('zip',point)


# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

sentence = "A NOUN went on a walk. They can VERB really well."
sentence = sentence.replace('NOUN','duck') #fill this in
sentence = sentence.replace('VERB','waddle') #fill this in

print sentence

