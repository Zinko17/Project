# # l1 = [1, 2, 3]
# #
# #
# # def count(list):
# #     list += 150
# #     return list
# #
# #
# # l2 = map(count, l1)
# # print(list(l2))
# import random
#
# l1 = [1, 2, 3, 4, 5, 6, 7]
#
#
# def count(number):
#     number %= 2
#     return number
#
#
# l2 = map(count, l1)
# print(list(l2))
#
# def count1(number):
#         number %= 2
#         if number == 0:
#                 return True
# l3 = filter(count1,l1)
# print(list(l3))
#
import random


# l1 =[]
# for i in range(10000):
#     l1.append(random.randint(1,100000))
#
# def count(number):
#     if number > 99995:
#         return True
#
# l2 = filter(count,l1)
# print(list(l2))

# class AgeDescriptor:
#     def __init__(self, param):
#         self.param = param
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.param]
#
#     def __set__(self, instance, value):
#         if isinstance(value, int):
#             if 0 < value <= 250:
#                 instance.__dict__[self.param] = value
#             else:
#                 raise ValueError('Invalid number')
#         else:
#             raise ValueError('Must be int')
#

# class NameDescriptor:
#     def __init__(self, param):
#         self.param = param
#
#     def __set__(self, instance, value):
#         if isinstance(value, str):
#             if len(value) < 50:
#                 if value.isalpha():
#                     instance.__dict__[self.param] = value
#                 else:
#                     raise ValueError('Must be alpha')
#             else:
#                 raise ValueError('Too long name')
#         else:
#             raise ValueError('Must be str')
#
#
# class Human:
#     age = AgeDescriptor('age')
#     name = NameDescriptor('name')
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# h1 = Human('adada', 230)
# print(h1.__dict__)

# class Student:
#     student_count = 0
#
#
#     def __init__(self, name, spec):
#         self.name = name
#         self.spec = spec
#         Student.student_count += 1
#         self.id = Student.student_count

#
# class Service:
#     name = 'class name'
#
#     def __init__(self):
#         self.name = 'object name'
#
#     @staticmethod
#     # Нужен для того, чтобы сделать метод независимым от объекта класса
#     def printed():
#         print('staticmethod')
#
#     @classmethod
#     # Нужен для того, чтобы из метода объекта сделать метод привязанный к классу
#     def sep(cls, self):
#         print(cls.name)
#         print(self.name)
#
#
# s1 = Service()
# Service.sep(s1)

