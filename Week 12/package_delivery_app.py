class Package:
    def __init__ (self, content):
        self.content = content

class Warehouse:
    def __init__ (self, warehouse_id):
        self.warehouse_id = warehouse_id
        self.inventory = [] # invetory will contain `Package` type objects

    def add(self, package_obj):
        self.inventory.append(package_obj)

    def remove(self, package_obj):
        self.inventory.remove(package_obj)

    def load_into_truck(self, truck_obj):
        # Manually create a copy of inventory
        copy_inventory = []
        for package_obj in self.inventory:
            copy_inventory.append(package_obj)

        for package_obj in copy_inventory:
            truck_obj.load(package_obj)

            self.remove(package_obj)

    def show_inventory(self):
        if len(self.inventory) == 0:
            print(f"Warehouse {self.warehouse_id} Inventory is empty")
        else:
            print(f"Printing Warehouse {self.warehouse_id} Inventory: ")
            for package_obj in self.inventory:
                print(package_obj.content)

class Truck:
    def __init__ (self, truck_id, destination):
        self.truck_id = truck_id
        self.cargo = [] # crago will contain `Package` type objects

        # Since a truck will move a package from a warehouse to another warehouse
        # `destination` will be a `Warehouse` type object
        self.destination = destination

    def load(self, package_obj):
        self.cargo.append(package_obj)

    def unload(self, package_obj):
        self.cargo.remove(package_obj)

    def unload_into_warehouse(self, warehouse_obj):
        # Creating a copy of `cargo`
        copy_cargo = []
        for package_obj in self.cargo:
            copy_cargo.append(package_obj)

        for package_obj in copy_cargo:
            self.unload(package_obj)

            warehouse_obj.add(package_obj)

    def show_cargo(self):
        if len(self.cargo) == 0:
            print(f"Truck {self.truck_id} Cargo is empty")
        else:
            print(f"Printing Truck {self.truck_id} Cargo: ")
            for package_obj in self.cargo:
                print(package_obj.content)

def main():
    warehouse_A = Warehouse("A")
    warehouse_B = Warehouse("B")

    warehouse_A.add(Package("Laptop"))
    warehouse_A.add(Package("Headphones"))
    warehouse_A.add(Package("Keyboard"))

    truck_A = Truck("A", warehouse_B)

    print("Step 1: Showing Cargo/Inventory")
    warehouse_A.show_inventory()
    print()
    truck_A.show_cargo()
    print()
    warehouse_B.show_inventory()

    print()

    print("Step 2: Loading packages from Warehouse A to Truck")
    warehouse_A.load_into_truck(truck_A)

    warehouse_A.show_inventory()
    print()
    truck_A.show_cargo()
    print()
    warehouse_B.show_inventory()

    print()
    print("Step 3: Unloading packages from Truck to Warehouse B")
    truck_A.unload_into_warehouse(warehouse_B)

    warehouse_A.load_into_truck(truck_A)
    
    warehouse_A.show_inventory()
    print()
    truck_A.show_cargo()
    print()
    warehouse_B.show_inventory()
    

if __name__ == "__main__":
    main()