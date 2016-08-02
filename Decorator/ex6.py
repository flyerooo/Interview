# def foo():
#     x = 3
#     def bar():
#         print x
#     x = 5
#     return bar
#
# bar = foo()
# bar()

def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper

def logging(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1}x".format(func.__name__,wrapper.count)
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print reverse_string("Able was I ere I saw Elba")
print "-------------"
print reverse_string("A man, a plan, a canoe, pasta,"
                     " heros, rajahs, a coloratura, maps, "
                     "snipe, percale, macaroni, a gag, a banana bag, "
                     "a tan, a tag, a banana bag again (or a camel), "
                     "a crepe, pins, Spam, a rut, a Rolo, cash, a jar, "
                     "sore hats, a peon, a canal: Panama!")