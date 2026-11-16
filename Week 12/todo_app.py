class todo_item:
    def __init__(self, title):
        self.title = title
        self.is_done = False

        print(f"Finished constructing a todo_item object with title: {self.title}")

    def print_item(self):
        if self.is_done == True:
            return f"[x] {self.title}"
        else:
            return f"[ ] {self.title}"

    def set_done(self):
        if self.is_done == True:
            print("This item is already done.")
        else:
            self.is_done = True

def main():
    todo_list = []

    while True:
        print("1. Add To Do Item")
        print("2. Set and Item as done")
        print("3. Print To Do List")
        print("4. Exit")

        choice = int(input("> "))
        print()

        if choice == 1:
            title = input("Enter a title: ")

            todo_list.append(todo_item(title))

            print("Finished appending a new To Do item into the list")
        elif choice == 2:
            print("Choose a item:")
            for index in range(len(todo_list)):
                print(f"{index} - {todo_list[index].title}")

            user_selection = int(input("> "))

            todo_list[user_selection].set_done()

        elif choice == 3:
            for item in todo_list:
                print(item.print_item())
        elif choice == 4:
            print("Terminating Program...")
            break

        print()


if __name__ == "__main__":
    main()