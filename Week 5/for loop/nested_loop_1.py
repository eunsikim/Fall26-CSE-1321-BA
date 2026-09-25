# A single repetition/iteration of the Outer Loop
# is composed of the full amount of iteration of
# inner loop
def main():
    count = 1

    # Outer Loop
    for i in range(3): # [0, 10)
        # Inner Loop
        for y in range(3):
            print(f"{count} Hello")
            count += 1

if __name__ == "__main__":
    main()