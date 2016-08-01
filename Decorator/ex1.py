# coding:utf-8
# def makeblod(fn):
#     # 装饰器将返回新的函数
#     def wrapper():
#         # 在之前或之后插入新的代码
#         return "<b>" + fn() + "</b>"
#     return wrapper
#
# # 斜体装饰器
# def makeitalic(fn):
#     # 装饰器将返回新的函数
#     def wrapper():
#         # 在之前或者之后插入新的代码
#         return "<i>" + fn() + "</i>"
#     return wrapper
#
# @makeblod
# @makeitalic
# def say():
#     return "hello"
# print say()

# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print "I got args!Look:", arg1, arg2
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments
#
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print "My name is", first_name, last_name
# print_full_name("Peter", "Venkman")

# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie = lie - 3
#         return method_to_decorate(self, lie)
#     return wrapper
#
# class Lucy(object):
#     def __init__(self):
#         self.age = 32
#     @method_friendly_decorator
#     def sayYourAge(self, lie):
#         print "I am %s, what did you think?" %(self.age + lie)
#
# l = Lucy()
# l.sayYourAge(-3)

def a_decorator_passing_arbitrary_arguments(function_to_decorator):
    # 包装器接受所有参数
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print "Do I have args?:"
        print args
        print kwargs
        function_to_decorator(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments
# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument():
#     print "Python is cool, no argument here."

# function_with_no_argument()

# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print a, b, c
#
# function_with_arguments(1,2,3)

# @a_decorator_passing_arbitrary_arguments
# def function_with_named_arguments(a, b, c, platypus="Why not?"):
#     print "Do %s, %s and %s like platypus? %s" %\
#           (a, b, c, platypus)
#
# function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")

class Mary(object):
    def __init__(self):
        self.age = 31
    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):
        print "I am %s, what did you think?" % (self.age + lie)

m = Mary()
m.sayYourAge()