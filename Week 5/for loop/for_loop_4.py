# Count how many vowels, consonants, 
# empty/blank spaces, and character 
# We have in `message`
# You cannot use the len() function

def main():
    message = "Hello World"
    # V: 3
    # C: 7
    # B: 1
    # C#: 11

    vowel_count = 0
    cons_count = 0
    blank_count = 0
    char_count_1 = 0
    char_count_2 = 0

    message = message.upper()

    for character in message:
        if character == "A" or character == "E" or character == "I" or character == "O" or character == "U":
            vowel_count += 1
        elif character == " ":
            blank_count += 1
        else:
            cons_count += 1
        
        # Approach 1: Count each single character
        char_count_1 += 1

    # Approach 2: Sum the vowels, consonants, and empty spaces count
    char_count_2 = vowel_count + cons_count + char_count_1
    
    print(f"'{message}' has {vowel_count} vowels")
    print(f"'{message}' has {cons_count} consonants")
    print(f"'{message}' has {blank_count} blank/empty spaces")
    print(f"'{message}' has {char_count_1} characters")



if __name__ == "__main__":
    main()