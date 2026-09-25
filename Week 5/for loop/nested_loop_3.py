"""
Print this:
123
456
789

Using nested for loops 
"""

def main():
    seq = "1234"

    count = 1

    for y in seq:
        for x in seq:
            print(count, end="")
            count += 1
        print()

if __name__ == "__main__":
    main()