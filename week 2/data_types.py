def main():
    num1 = 20 # this is an int value
    num2 = 3.14 # this is a float value
    my_bool_1 = True # this is a boolean value
    my_bool_2 = False # this is a boolean value
    my_string = "Hello CSE 1321"

    # Variables and values in python can change/mutate
    # throughout the code.
    # We can use the type() function to determine
    # the data type at a particular instance
    print(num1)

    num1 = 30 

    print(num1)
    print(type(num1))

    num1 = 30.0

    print(num1)
    print(type(num1))

    num1 = "30.0"

    print(num1)

    print(type(num1))

    # We can also change or convert a value from 
    # one data type into another
    num3 = 40.5
    print(num3, end=" is a ")
    print(type(num3))

    num3 = str(num3)
    print(num3, end=" is a ")
    print(type(num3))

    # We change num3 to 40.7 (int)
    num3 = 40.7
    print(num3, end=" is a ")
    print(type(num3))

    num3 = int(num3)
    print(num3, end=" is a ")
    print(type(num3))

    # We change num3 to "40.7" (str)
    # num3 = "40.7"
    # num3 = int(num3) # this is illegal
    # print(num3, end=" is a ")
    # print(type(num3))

    num3 = "40.7"
    num3 = float(num3)
    print(num3, end=" is a ")
    print(type(num3))

    num3 = "40.7!!!"
    num3 = float(num3)
    print(num3, end=" is a ")
    print(type(num3))


if __name__ == "__main__":
    main()