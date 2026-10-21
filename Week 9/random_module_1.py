import random

def main():
    random.seed(10)

    print("using randint()")
    for x in range(3):
        # The end argument in randint is inclusive
        random_number = random.randint(1, 10)
        print(random_number)

    print("using randrange()")
    for x in range(10):
        # The end argument in randrange is exclusive
        random_number = random.randrange(1, 11, 2)
        print(random_number)


if __name__ == "__main__":
    main()