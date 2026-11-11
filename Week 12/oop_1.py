# This is our template
class sword:
    material = "Gold"
    sharpness = 0.0
    shape = ""
    handle_material = ""

def main():
    sword_1 = sword()

    sword_1.material = "Iron"
    sword_1.sharpness = 100.0
    sword_1.shape = "Short Sword"
    sword_1.handle_material = "Oak"

    sword_2 = sword()
    sword_2.material = "Steel"
    sword_2.sharpness = 50.0
    sword_2.shape = "Long Sword"
    sword_2.handle_material = "Leather"

    print(f"Sword 1 Material: {sword_1.material}")
    print(f"Sword 2 Material: {sword_2.material}")
    print(f"Sword Material: {sword.material}")

    sword_1.material = "Tin"

    print()

    print(f"Sword 1 Material: {sword_1.material}")
    print(f"Sword 2 Material: {sword_2.material}")
    print(f"Sword Material: {sword.material}")

if __name__ == "__main__":
    main()