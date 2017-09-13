from Vector import Vector


def plus(self,v):
    new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
    return Vector(new_coordinates)

def minus(self,v):
    new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)

def times_scalar(self,c):
    new_coordinates = [c * x for x in self.coordinates]
    return Vector(new_coordinates)



# v = Vector([-0.221,7.437])
# print v.normalized()

# v = Vector([7.887,4.138])
# w = Vector([-8.802,6.776])
# print v.dot(w)
#
# v = Vector([-5.995,-4.904,-1.874])
# w = Vector([-4.496,-8.755,7.103])
# print v.dot(w)
#
# v = Vector([3.183,-7.627])
# w = Vector([-2.668,5.319])
# print v.angle_with(w)
#
# v = Vector([7.35,0.221,5.188])
# w = Vector([2.751,8.259,3.985])
# print v.angle_with(w,in_degrees=True)

# v = Vector([-7.579,-7.88])
# w = Vector([22.737,23.64])
# print v.is_parallel_to(w)
#
# v = Vector([-2.029,9.97,4.172])
# w = Vector([-9.231,-6.639,-7.245])
# print v.is_parallel_to(w)
