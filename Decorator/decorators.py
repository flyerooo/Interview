# def shout(word="yes"):
#     return word.capitalize() + "!"
# print shout()
# scream =shout
# print scream()
#
# del shout
# try:
#     print shout()
# except NameError as e:
#     print e

# def talk():
#     def whisper(word="yes"):
#         return word.lower() + "..."
#     print  whisper()
#
# talk()
#
# try:
#      print whisper()

# def getTalk(kind="shout"):
#     def shout(word="yes"):
#         return word.capitalize() + "!"
#     def whisper(word="yes"):
#         return word.lower()+"..."
#     if kind == "shout":
#         return shout
#     else:
#         return whisper
#
# talk = getTalk()
# print talk()

# def doSomethingBefore(func):
#     print "I do something before then I call the function you gave me"
#     print func()
# doSomethingBefore(scream)

# def my_shiny_new_decorator(a_function_to_decorate):
#     def the_wrapper_around_the_original_function():
#         print "Before the function runs"
#         a_function_to_decorate()
#         print "After the function runs"
#     return the_wrapper_around_the_original_function
# def a_stand_alone_function():
#     print "I am a stand alone function, don't you dare modify me"

#
# a_stand_alone_function()
# # a_stand_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
# a_stand_function_decorated()

# a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
# a_stand_alone_function()
# a = my_shiny_new_decorator(a_stand_alone_function)
# a()
#
# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print "Leave me alone"
#
# another_stand_alone_function()

def bread(func):
    def wrapper():
        print "</''''''\>"
        func()
        print "<\______/>"

    return wrapper

def ingredients(func):
    def wrapper():
        print "#tomatoes#"
        func()
        print  "~salad~"
    return wrapper

def sandwich(food="--ham--"):
    print food

sandwich()
sandwich = bread(ingredients(sandwich))
sandwich()
