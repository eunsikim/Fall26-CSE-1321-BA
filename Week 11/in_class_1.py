"""
Create program where you ask the user to enter 5 colors,
then ask the user to rank these colors from 1 (least favorite) 
- 10 (favorite)

Then, print out the user's favorite colors (only rank 8 or greater)

You have to implement a dictionary to keep track of colors and their
ranking.

Sample Output:
Enter a color: Blue
Enter a color: Brown
Enter a color: Red
Enter a color: Green
Enter a color: Yellow

Rank the color Blue (1 to 10): 10
Rank the color Brown (1 to 10): 8
Rank the color Red (1 to 10): 4
Rank the color Green (1 to 10): 5
Rank the color Yellow (1 to 10): 2

Your favorite colors are:
Blue
Brown
"""

def Approach_1():
    # Data scheme => Key-Color Name (str), Value-Ranking (int) 
    color_ranking = {}

    for x in range(5):
        color = input("Enter a color: ")

        # Adding a KV Pair into the dictionary
        color_ranking[color] = 0
    print()

    for key in color_ranking:
        ranking = int(input(f"Rank the color {key} (1 to 10): "))

        # Modifying a value of a KV Pair in the dictionary
        color_ranking[key] = ranking

    print()

    print("Your favorite colors are:")
    for key in color_ranking:
        if color_ranking[key] >= 8:
            print(key)

def Approach_2():
    favorite_colors={}
    color1=input("Enter a color: ")
    color2=input("Enter a color: ")
    color3=input("Enter a color: ")
    color4=input("Enter a color: ")
    color5=input("Enter a color: ")

    rank_color1=int(input(f"Rank the color {color1} (1 to 10): "))
    rank_color2=int(input(f"Rank the color {color2} (1 to 10): "))
    rank_color3=int(input(f"Rank the color {color3} (1 to 10): "))
    rank_color4=int(input(f"Rank the color {color4} (1 to 10): "))
    rank_color5=int(input(f"Rank the color {color5} (1 to 10): "))
    print()

    if rank_color1 >=8:
        favorite_colors[color1]=rank_color1
    if rank_color2 >=8:
        favorite_colors[color2]=rank_color2
    if rank_color3 >=8:
        favorite_colors[color3]=rank_color3
    if rank_color4 >=8:
        favorite_colors[color4]=rank_color4
    if rank_color5 >=8:
        favorite_colors[color5]=rank_color5
    print()
    print("Your favorite colors are:")
    for key in favorite_colors:
        print(key)

if __name__ == "__main__":
    print("==================Approach 1==================")
    Approach_1()

    print()

    print("==================Approach 2==================")
    Approach_2()
