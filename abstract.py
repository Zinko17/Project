# import abc
#
## Абстрактный класс
#
# class Furniture(abc.ABC):
#
#     @abc.abstractmethod
#     def comfort(self):
#         pass
#
#     @abc.abstractmethod
#     def creature(self):
#         pass
#
#
# class Tumbochka(Furniture):
#
#     def comfort(self):
#         print('Its comfortable')
#
#     def creature(self):
#         print('Its creatable')
#
#
# class Stul(Furniture):
#
#     def comfort(self):
#         print('Its comfortable')
#
#     def creature(self):
#         print('Its creatable')
#
#
# t1 = Tumbochka()
# s1 = Stul()

# Контекстный менеджер

# class Timer:
#     import time
#
#     def __enter__(self):
#         self.start_time = self.time.time()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(self.time.time() - self.start_time)
#
#
# with Timer() as t:
#     for i in range(10000000):
#         pass
