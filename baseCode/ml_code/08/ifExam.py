def bigger(number1,number2):
    if(number1 > number2):
        return number1
    else:
        return number2

print bigger(2,7)
print bigger(3,2)
print bigger(3,3)

def is_friend(name):
    return name[0]== 'D'or name[0] == 'N'

print is_friend('Diane')
print is_friend('NFred')

def biggest(number1,number2,number3):

   return max(number1,number2,number3)

    # if(number1 > number2):
    #     value = number1
    # else:
    #     value = number2
    # if(value > number3):
    #     return value
    # else:
    #     return number3

print biggest(6,2,3)

i = 0
while i != 10:
    i = i + 1
    print i