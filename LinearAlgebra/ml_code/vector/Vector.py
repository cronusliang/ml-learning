from math import sqrt, acos, pi

from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALEZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([x for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def times_scalar(self,c):
        new_coordinates = [c * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1.0/ magnitude)
        except ZeroDivisionError:
            raise Exception('cannot normalized the zero vector')

    def dot(self,v):
        return sum([x*y for x,y in zip(self.coordinates,v.coordinates)])

    def angle_with(self,v,in_degrees = False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            u3 = u1.dot(u2)

            angle_in_radians = acos(u3)
            if in_degrees:
               degrees_per_radian = 180./ pi
               return angle_in_radians * degrees_per_radian
            else:
               return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALEZE_ZERO_VECTOR_MSG:
                raise ValueError('The coordinates must be nonempty')
            else:
                raise e

    def is_orthogonal_to(self,v,tolerance=1e-10):
         return abs(self.dot(v)) < tolerance

    def is_parallel_to(self,v):
        return (self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == pi)

    def is_zero(self,tolerance=1e-10):
        return self.magnitude() < tolerance
