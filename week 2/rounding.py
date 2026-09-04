def main():
    num1 = 3.14159265359
    num2 = 3.7

    num1_round = round(num1)
    num2_round = round(num2)

    print(f"num1_round = {num1_round} is a {type(num1_round)}")
    print(f"num2_round = {num2_round} is a {type(num2_round)}")

    print()

    num1_round_2 = round(num1, 2)
    num2_round_2 = round(num2, 2)
    num2_round_2_f = f"{num2:.2f}"

    print(f"num1_round_2 = {num1_round_2} is a {type(num2_round_2)}")
    print(f"num2_round_2 = {num2_round_2} is a {type(num2_round_2)} (concatenation)")
    print(f"num2_round_2 = {num2_round_2_f} is a {type(num2_round_2_f)} (f-string)")
    print(f"num2_round_2 = {num2:.2f} (f-string)")

    print()

    num3 = 3.1
    print(f"num3 = {round(num3)}")

    num3 = 3.7
    print(f"num3 = {round(num3)}")

    num3 = 3.5
    print(f"num3 = {round(num3)}")

    num3 = 2.5
    print(f"num3 = {round(num3)}")

if __name__ == "__main__":
    main()