# -*- coding: utf-8 -*-
from decimal import Decimal, getcontext
from Vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    # 基准点
    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Plane.first_nonzero_index(n.coordinates)
            initial_coefficient = n.coordinates[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    # 两个平面是否平行
    def is_parallel_to(self, ell):
        n1 = self.normal_vector  # 获取法向量
        n2 = ell.normal_vector
        return n1.is_parallel_to(n2)

    # 两个平面是否相等
    def __eq__(self, other):

        if self.normal_vector.is_zero():
            if not other.normal_vector.is_zero():
                return False
            else:
                diff = self.constant_term - other.constant_term
                return MyDecimal(diff).is_zero()
        elif other.normal_vector.is_zero():
            return False
        if not self.is_parallel_to(other):  # 判断是否平行
            return False
        x0 = self.basepoint
        y0 = other.basepoint
        basepoint_difference = x0.minus(y0)
        n = self.normal_vector
        return basepoint_difference.is_orthogonal_to(n)  # 两点连线的向量是否与法向量正交

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Plane.first_nonzero_index(n.coordinates)
            terms = [write_coefficient(n.coordinates[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n.coordinates[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

p1 = Plane(normal_vector=Vector(['-0.412','3.806','0.728']),constant_term='-3.46')
p2 = Plane(normal_vector=Vector(['1.03','-9.515','-1.82']),constant_term='8.65')
print 'first pair of planes are parallel?:{} ',format(p1.is_parallel_to(p2))
print 'first pair of planes are equal?:{} ',format(p1==p2)

p1 = Plane(normal_vector=Vector(['2.611','5.528','0.283']),constant_term='4.6')
p2 = Plane(normal_vector=Vector(['7.715','8.306','5.342']),constant_term='3.76')
print 'second pair of planes are parallel?:{} ',format(p1.is_parallel_to(p2))
print 'second pair of planes are equal?:{} ',format(p1==p2)

p1 = Plane(normal_vector=Vector(['-7.926','8.625','-7.212']),constant_term='-7.95')
p2 = Plane(normal_vector=Vector(['-2.642','2.875','-2.404']),constant_term='-2.44')
print 'third pair of planes are parallel?:{} ',format(p1.is_parallel_to(p2))
print 'third pair of planes are equal?:{} ',format(p1==p2)