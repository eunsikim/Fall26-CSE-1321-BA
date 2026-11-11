class car:
    # Constructor
    def __init__(self, make_, model_, year_, price_, color_, milage_):
        # We define the object attribute
        # Object Attribute = Initial Value (from parameter)
        self.make = make_
        self.model = model_
        self.year = year_
        self.price = price_
        self.color = color_
        self.mileage = milage_
        self.sold = False

    # We use the `self` keyword to specify the object
    # attribute `price`.
    # Remember that the value of `price` is unique 
    # to a individual `car` object.
    def sell_car(self, money):
        return money - self.price
        # c1 = car()
        # ... return c1.price - money


def main():
    c1 = car("Hyundai", "Santa Fe", "2026", "40,000", "Blue", "0")
    c2 = car("Hyundai", "Elantra", "2026", "40,000", "Blue", "0")

    print(f"{c1.year} {c1.make} {c1.model}")
    print(f"{c2.year} {c2.make} {c2.model}")

    c1.make = "Kia"

    print(f"{c1.year} {c1.make} {c1.model}")
    print(f"{c2.year} {c2.make} {c2.model}")

    # print(f"Buying car 1 with a $100.00 bill...")
    # print(f"Your change is: ${c1.sell_car(c1, 100)}")

if __name__ == "__main__":
    main()