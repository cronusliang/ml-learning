def sum_list(p):
    sum = 0
    for e in p:
        sum += e
    return sum
print sum_list([1, 7, 4])
#>>> 12
print sum_list([9, 4, 10])
#>>> 23
print sum_list([44, 14, 76])
#>>> 134

def measure_udacity(p):
    value = 0
    for e in p:
        if(str(e)[0] == 'U'):
            value += 1
    return value

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])

def find_element(p,number):
    if number not in p:
        return -1
    return p.index(number)

print find_element([1,2,3],2)

