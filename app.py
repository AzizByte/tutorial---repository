# Operations we use PEMDAS
Number_of_books = 2*3+4/2-(2**2)
print(Number_of_books)


# No need to import math
print(abs(-100))
print(round(2.9))


# Before using some mathematical function, we have to first import math it.
import math
print(math.sqrt(25))
print(math.log(1))
print(math.pow(5,2))
print(math.ceil(2.1))
print(math.floor(2.9))
print(math.pi)
print(math.e)
decibels = 10 * math.log(4/2)
print(decibels)
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(radians)
angle = math.sin(radians)


# A function Definition without arguments
def print_lyrics():
    print("I am Lumberjack and I am okay.")
    print("I sleep all night and work all day")
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    print_lyrics()
    print_lyrics()
repeat_lyrics()

# A function definition that takes arguments
def print_twice(Bruce):
    print(Bruce)
    print(Bruce)
print_twice(32)
print_twice("hello")  
print_twice(math.pi)
print_twice(" hey bro "* 7)
print_twice(math.sin(math.pi))
light = "Ramandhan"
print_twice(light)
   
# python with no arguments and no return value
def add1():
    a = 10
    b =2
    sum = a + b
    print("Total sum:", sum)
add1()

# python function with argument, no return value
def add2(a,b):
    sum = a + b
    print("Total sum:", sum)
add2(10, 2)

# python function with arguments and return value
def add3(a, b):
    sum = a + b
    return sum
z = add3(10, 2)
print("Total sum:", z)

#python with no arguments, with return value
def add4():
    a = 10
    b = 2
    sum = a + b
    return sum
x = add4()
print("Sum:", x)












