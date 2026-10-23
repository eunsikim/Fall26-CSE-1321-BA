import time

def main():
    s = "Hello World"

    # # Printing the first character
    # print(s[0])

    # # Printing the last character
    # print(s[10])
    
    # # Printing the first 3 characters
    # for x in range(3):
    #     print(s[x])

    # Traversing a sequence by the element
    print("Traversing by Element")
    for char in s:
        print(char, end="")
        time.sleep(0.25)
    print()

    # Traversing a sequence by the index
    print("Traversing by Index (FOR)")
    for x in range(len(s)):
        print(s[x], end="")
        time.sleep(0.25)
    print()

    print("Traversing by Index (WHILE)")
    index = 0
    while index < len(s):
        print(s[index], end="")
        time.sleep(0.25)
        index += 1
    print()

if __name__ == "__main__":
    main()