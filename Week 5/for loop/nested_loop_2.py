# A single repetition/iteration of the Outer Loop
# is composed of the full amount of iteration of
# inner loop
def main():
    # Outer Loop
    for i in range(3): # [0, 3)
        print(f"Outer Iteration #{i + 1}")
        for y in range(3):
            print(f"\tInner Iteration #{y + 1}")

if __name__ == "__main__":
    main()