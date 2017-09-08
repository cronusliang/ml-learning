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



v = Vector([-0.221,7.437])
print v.normalized()
