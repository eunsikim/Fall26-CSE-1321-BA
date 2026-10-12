def some_function():
    return 10

def print_hello_world():
    print("Hello World")

print(some_function()) # Function calls are an expression for some value
print(type(some_function())) # and some data type

print(print_hello_world())
print(type(print_hello_world()))

my_string = "Hello World"

my_string = my_string.upper()

print(my_string)