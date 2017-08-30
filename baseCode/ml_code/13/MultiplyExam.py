

def product_list(list_of_numbers):
  value = 1
  for e in list_of_numbers:
      value = value * e
  return value



print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1

def greatest(list_of_numbers):
    maxValue = 0
    for e in list_of_numbers:
        if e >= maxValue:
           maxValue = e
    return maxValue



print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

# A list of replacement words to be passed in to the play game function.
parts_of_speech1 = ["PLACE", "PERSON", "PLURALNOUN", "NOUN", "NAME", "VERB", "OCCUPATION", "ADJECTIVE"]

# The following are some test strings to pass in to the play_game function.
test_string1 = "Hi, my name is NAME and I really like to VERB PLURALNOUN. I'm also a OCCUPATION at PLACE."
test_string2 = """PERSON! What is PERSON going to do with all these ADJECTIVE PLURALNOUN? Only a registered
OCCUPATION could VERB them."""
test_string3 = "What a ADJECTIVE day! I can VERB the day off from being a OCCUPATION and go VERB at PLACE."


# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None


# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in a: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


print play_game(test_string1, parts_of_speech1)