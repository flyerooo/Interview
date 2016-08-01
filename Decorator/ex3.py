#coding:utf-8
def decorator_maker():

    print "I make decorators! I am executed only once: "+\
          "when you make me create a decorator."

    def my_decorator(func):

        print "I am a decorator! I am executed only when you decorate a function."

        def wrapped():
            print ("I am the wrapper around the decorated function. "
                  "I am called when you call the decorated function. "
                  "As the wrapper, I return the RESULT of the decorated function.")
            return func()

        print "As the decorator, I return the wrapped function."

        return wrapped

    print "As a decorator maker, I return a decorator"
    return my_decorator

# 让我们建一个装饰器.它只是一个新函数.
new_decorator = decorator_maker()
#输出:
#I make decorators! I am executed only once: when you make me create a decorator.
#As a decorator maker, I return a decorator

# 下面来装饰一个函数

def decorated_function():
    print "I am the decorated function."

decorated_function = new_decorator(decorated_function)