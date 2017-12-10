# -*- coding: utf-8 -*-
from decimal import Decimal, getcontext
from copy import deepcopy

from Vector import Vector
from Plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    #交换行
    def swap_rows(self, row1, row2):
        if row1 == row2:
            return
        elif row1 < 0 or row1 >= len(self) or row2 < 0 or row2 >= len(self):
            print "row dimension out of range for swap"
        else:
            temp = self.planes[row1]
            self.planes[row1] = self.planes[row2]
            self.planes[row2] = temp


    #乘以系数
    def multiply_coefficient_and_row(self, coefficient, row):
        n =  self[row].normal_vector
        k = self[row].constant_term

        new_normal_vector = n.scalar(coefficient)
        new_constant_term = k * coefficient
        self[row] = Plane(normal_vector=new_normal_vector,constant_term=new_constant_term)


    # 行相加
    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        n1 = self[row_to_add].normal_vector
        n2 = self[row_to_be_added_to].normal_vector
        k1 = self[row_to_add].constant_term
        k2 = self[row_to_be_added_to].constant_term

        new_normal_vector = n1.scalar(coefficient).plus(n2)
        new_constant_term = k1 * coefficient + k2
        self[row_to_be_added_to] = Plane(normal_vector=new_normal_vector,constant_term=new_constant_term)


    # 找出每个等式中的第一个非零项
    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    # 返回方程组里的平面数量
    def __len__(self):
        return len(self.planes)


    # 获取方程组里的某个平面
    def __getitem__(self, i):
        return self.planes[i]

    # 设置方程组里的某个平面
    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    # 返回三角型的方程组
    def compute_triangular_form(self):
        system = deepcopy(self)    #不直接修改原始方程组

        num_equations = len(system)         # 行数
        num_variables = system.dimension    # 列数

        j = 0
        for i in range(num_equations):
            while j < num_variables:
                c = MyDecimal(system[i].normal_vector.coordinates[j])
                if c.is_near_zero():
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coefficient_if_able(i,j)
                    if not swap_succeeded:
                        j += 1
                        continue
                system.clear_coefficients_below(i,j)
                j += 1
                break
        return system

    # (阶梯型矩阵)
    def compute_rref(self):
        tf = self.compute_triangular_form()
        for i in reversed(range(len(tf))):
            leadingCoefIndex = None
            try:
                leadingCoefIndex = Plane.first_nonzero_index(tf[i].normal_vector.coordinates)
            except:
                pass
            if leadingCoefIndex or leadingCoefIndex == 0:
                leadingCoef = tf[i].normal_vector.coordinates[leadingCoefIndex]
                tf.multiply_coefficient_and_row(Decimal(1.)/leadingCoef,i)
                for j in range(0,i):
                    rowJCoef = tf[j].normal_vector.coordinates[leadingCoefIndex]
                    tf.add_multiple_times_row_to_row(Decimal(-1.)*rowJCoef,i,j)
        return tf


    def swap_with_row_below_for_nonzero_coefficient_if_able(self,row,col):
        num_equations = len(self)

        for k in range(row+1,num_equations):
            coefficient = MyDecimal(self[k].normal_vector.coordinates[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row,k)
                return True
        return False


    def clear_coefficients_below(self,row,col):
        num_equations = len(self)
        beta = MyDecimal(self[row].normal_vector.coordinates[col])

        for k in range(row+1,num_equations):
            n = self[k].normal_vector
            gamma = n.coordinates[col]
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha,row,k)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='-1') and
#         r[1] == p2):
#     print 'test case 1 failed'
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# r = s.compute_rref()
# if not (r[0] == p1 and
#         r[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'
#
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='0') and
#         r[1] == p2 and
#         r[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
#         r[3] == Plane()):
#     print 'test case 3 failed'
#
# p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')) and
#         r[1] == Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')) and
#         r[2] == Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9'))):
#     print 'test case 4 failed'

