# Function definition
def is_even(number): # Definition/Header: def identifier/name(parameter(s))
    # Function Body 
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is not even")

def add(n1, n2): # We can have 0 to infinite # of parameters. Multiple parameters are separated by a comma.
    calculation = n1 + n2

    return calculation

def main():
    # Function call
    is_even(33) # identifier/name(argument)

    print(f"Addition: {add(4, 5)}") # add(4, 5) will become 9

    for x in range(10):
        is_even(x)

    

if __name__ == "__main__":
    main()