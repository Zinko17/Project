import time


# def decorator(func):
#     print('Start!')
#     return func
#
#
# @decorator
# def f1():
#     print('Send request!')
#     print('Finish!')
#
# f1()

# def timer(func):
#     start_time = time.time()
#     func()
#     print(time.time() - start_time)
#
# @timer
# def f1():
#     for i in range(1000000):
#         pass

def func(*args, **kwargs):
    print(args, kwargs)


func(1, 2, 3, 5, name='john', last_name='snow')


def archieve(*args):
    print(args)


l1 = [1, 2, 3, 4, 5, 6]
archieve(*l1)
