def foo(x):
    print "executing foo(%s)" % (x)

class A(object):
    def foo(selfself, x):
        print "executing foo(%s,%s)"%(self,x)
    @classmethod
    def class_foo(clscls,x):
        print "executing class_foo(%s,%s)"%(cls,x)
    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x

a=A()