"""
Shape Identifier:
- Use match statements
- Ask the user for the number of sides that a shape has.
- Based on the number entered by the user, display whether 
  the shape is a triangle, quadrilateral, pentagon, hexagon, 
  or “I do not know a shape with that many sides”
"""
def main():
    num_sides = input("Number of sides: ")

    match num_sides:
        case "3":
            print("You have a triangle")
        case "4":
            print("You have a quadrilateral")
        case "5":
            print("You have a pentagon")
        case "6":
            print("You have a hexagon")
        case _:
            print("I do not know a shape with that many sides.")

if __name__ == "__main__":
    main()