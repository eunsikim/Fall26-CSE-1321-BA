import random

def main():
    available_choice = "rps"

    # The choice function will choose a single item/element
    # in a sequence. 
    # `computer_choice` will have a value of either "r", "p", or "s"
    computer_choice = random.choice(available_choice)

    if computer_choice == "r":
        print("The computer chose Rock")
    elif computer_choice == "p":
        print("The computer chose Paper")
    elif computer_choice == "s":
        print("The computer chose Scissors")

if __name__ == "__main__":
    main()