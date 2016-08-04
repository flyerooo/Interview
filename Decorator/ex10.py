# # coding:utf-8
# names = ['jianpx', 'yue']
# ages = [23, 40]
# m = dict(zip(names, ages))
# print m
# # 用Python生成指定长度的斐波那契数列
# def fib(n):
#     result = [0, 1]
#     for index in range(n - 2):
#         result.append(result[-2] + result[-1])
#     return result
#
# if __name__ == "__main__":
#     num = input('Enter one number: ')
#     print fib(num)
# import copy
# a = 2
# b = copy.deepcopy(a)
# print b

def multipliers():
    return [lambda x : i * x for i in range(4)]



# def multipliers():
#     newlist = []
#     def foo(x):
#         for i in range(3):
#             newlist.append(i* x)
#         return newlist
#     return foo

print [m(2) for m in multipliers()]