from random import randint
# i = 1
# while i != 10:
#     i = i + 2
#     print i

# def print_numbers(number):
#     value = 1
#     while value<= number:
#         print value
#         value += 1
#
# print_numbers(4)

# def weekend(day):
#     # your code here
#     return str(day) == 'Saturday' or str(day) == 'Sunday'
# print weekend('Monday')
# # >>> False
# print weekend('Saturday')
# # >>> True
# print weekend('July')
#
# def countdown(number):
#     value = 0
#     while number>value:
#         print number - value
#         value+=1
#     print 'blastoff'
#
# countdown(-10)
#
# def bigger(a,b):
#     if a > b:
#         return a
#     else:
#         return b
#
# def biggest(a,b,c):
#     return bigger(a,bigger(b,c))
#
# def median(a,b,c):
#     value = biggest(a,b,c)
#     if(value == a):
#         return bigger(b,c)
#     if(value == b):
#         return bigger(a,c)
#     if(value == c):
#         return bigger(a,c)

# the string "sofa" if the number is 0, else return "llama".
# def random_noun():
#     if(randint(0,1) == 0):
#         return 'sofa'
#     else:
#         return 'llama'
#
# print  random_noun()

from random import randint


def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"


def random_noun():
    random_num = randint(0, 1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    # your code here
    if (word == "NOUN"):
        return random_noun()
    elif(word == "VERB"):
        return random_verb()
    else:
        return word[0]


def process_madlib(mad_lib):
    processed = ""
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    index = 0
    box_len = 4
    len(mad_lib)
    while index < len(mad_lib):
        frame = mad_lib[index:index+box_len]
        to_add = word_transformer(frame)
        processed += to_add
        if len(to_add) == 1:
            index += 1
        else:
            index += 4
    return processed



test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)