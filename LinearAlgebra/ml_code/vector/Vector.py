from math import sqrt, acos, pi

from decimal import Decimal, getcontext

import numpy

getcontext().prec = 30

class Vector(object):
    CANNOT_NORMALEZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'no_unique_parallel_component_msg'
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'no_unique_orthogonal_component_msg'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([x for x in coordinates])  # 返回一个元祖 ,坐标
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    # 输出向量坐标
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    # 判断两个向量是否相等
    def __eq__(self, v):
        return self.coordinates == v.coordinates

    # 向量加法
    def plus(self, v):
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]     # 相对应的点相加
        return Vector(new_coordinates)

    # 向量减法
    def minus(self, v):
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]   # 相对应的点相减
        return Vector(new_coordinates)

    #标量乘法
    def scalar(self,c):
        new_coordinates = [c * x for x in self.coordinates]
        return Vector(new_coordinates)

     # 向量的大小
    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))   # 相加求和的平方根

    # 求标准化向量
    def normalized(self):
        try:
            magnitude = self.magnitude()   # 先求出大小
            return self.scalar(1.0/ magnitude)   # 再相乘
        except ZeroDivisionError:
            raise Exception('cannot normalized the zero vector')

    # 求向量的点积
    def dotProduct(self,v):
        new_coordinates = [x * y for x, y in zip(self.coordinates, v.coordinates)]  # 相对应的点相乘
        return sum(new_coordinates)

    # 求向量的角度
    def angle(self,v,in_degrees = False):
        try:
            u1 = self.normalized()  # 求出标准化向量
            u2 = v.normalized()
            u3 = u1.dotProduct(u2)

            angle_in_radians = numpy.arccos(u3)  # 求出弧度

            if in_degrees:  # 如果是角度
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.CANNOT_NORMALEZE_ZERO_VECTOR_MSG:
                raise Exception('cannot compute an angle with the zero vector')
            else:
                raise e

    # 判断向量是否为正交
    def is_orthogonal_to(self,v,tolerance=1e-10):
         return abs(self.dotProduct(v)) < tolerance

    # 判断向量是否平行
    def is_parallel_to(self,v):
        return (self.is_zero() or v.is_zero() or self.angle(v) == 0 or self.angle(v) == pi)

    #检查是否为零向量
    def is_zero(self,tolerance=1e-10):
        return self.magnitude() < tolerance


    #向量基于 basis 的垂直向量
    def component_orthogonal_to(self,basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALEZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    #计算基于basis 向量的投影
    def component_parallel_to(self,basis):
        try:
            u = basis.normalized()
            weight = self.dotProduct(u)
            return u.scalar(weight)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALEZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    # 向量积
    def cross(self,v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [y_1 * z_2 - y_2 * z_1, -(x_1 * z_2 - x_2 * z_1), x_1 * y_2 - x_2 * y_1]
            return Vector(new_coordinates)
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates+('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif(msg == 'too many values to unpack' or msg == 'need more than 1 value to unpack'):
                raise Exception('only defined in two three dims msg')
            else:
                raise e

    # 向量面积
    def area_of_parallelogram_with(self,v):
         cross_product = self.cross(v)
         return cross_product.magnitude()

    # 向量三角形面积
    def area_of_triangle_with(self,v):
        return self.area_of_parallelogram_with(v) / Decimal('2.0')