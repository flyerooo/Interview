# def my_decorator(func):
#     print "I am ordinary function"
#     def wrapper():
#         print "I am function returned by the decorator"
#         func()
#     return wrapper
# def lazy_function():
#     print "zzzzzzz"
#
# # decorated_function = my_decorator(lazy_function)
#
# @my_decorator
# def lazy_function():
#     print "zzzzzzzz"

def makeConstantAdder(x):
    constant = x
    def adder(y):
        return y + constant
    return adder

f = makeConstantAdder(12)
print f(3)