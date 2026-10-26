def main():
    grades = [] # Initialize an empty list with `[]`
    my_favorite_numbers = [1, 2, 3] # Initialize a list with initial values

    # print(my_favorite_numbers[0])

    my_favorite_numbers_sum = 0

    for x in range(3):
        my_favorite_numbers_sum += my_favorite_numbers[x]

    print(my_favorite_numbers_sum)

if __name__ == "__main__":
    main()