def many_types(x):
    if x < 0:
        return "Hello!"
    else:
        return 0


print(many_types(1))
print(many_types(-1))


def do_nothing():
    pass


print(do_nothing())


def func(*args):
    # args will be a tuple containing all values that are passed in
    for i in args:
        print(i)


func(1, 2, 3, 9)  # Calling it with 3 arguments

list_of_arg_values = [1, 2, 3]
func(*list_of_arg_values)


def func(**kwargs):
    # kwargs will be a dictionary containing the names as keys and the values as values
    for name, value in kwargs.items():
        print(name, value)


func(value1=1, value2=2, value3=3)  # Calling it with 3 arguments
# Out: value1 1
# value2 2
# value3 3
func()  # Calling it without arguments
# No Out put
my_dict = {'foo': 1, 'bar': 2}
func(**my_dict)  # Calling it with a dictionary


# Out: foo 1
# bar 2

def greeting():
    return "Hello"


print(greeting())

greet_me = lambda: "Hello"
print(greet_me())

strip_and_upper_case = lambda s: s.strip().upper()
strip_and_upper_case(" Hello ")

greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')


def make(action='nothing'):
    return action


print(make("fun"))
# Out: fun
print(make(action="sleep"))
# Out: sleep
# The argument is optional so the function will use the default value if the argument is
# not passed in.
print(make())


# Out: nothing

def f(a, b=42, c=[]):
    pass


print(f.__defaults__)


def append(elem, to=[]):
    to.append(elem)  # This call to append() mutates the default variable "to"
    return to


append(1)
# Out: [1]
append(2)  # Appends it to the internally stored list
# Out: [1, 2]
append(3, [])  # Using a new created list gives the expected result
# Out: [3]
# Calling it again without argument will append to the internally stored list again
append(4)


# Out: [1, 2, 4]


def foo(x):  # here x is the parameter
    x[0] = 9  # This mutates the list labelled by both x and y
    print(x)


y = [4, 5, 6]
foo(y)  # call foo with y as argument
# Out: [9, 5, 6] # list labelled by x has been mutated
print(y)


# Out: [9, 5, 6] # list labelled by y has been mutated too


def foo(x):  # here x is the parameter, when we call foo(y) we assign y to x
    x[0] = 9  # This mutates the list labelled by both x and y
    x = [1, 2, 3]  # x is now labeling a different list (y is unaffected)
    x[2] = 8  # This mutates x's list, not y's list


y = [4, 5, 6]  # y is the argument, x is the parameter
foo(y)  # Pretend that we wrote "x = y", then go to line 1


def makeInc(x):
    def inc(k):
        return k + x

    return inc


incOne = makeInc(1)
incFive = makeInc(5)
incOne(5)  # returns 6
incFive(5)  # returns 10


# recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
