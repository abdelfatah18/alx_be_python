def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
    
def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter your item: ")
            print(f"Item '{item}' is added.")
            shopping_list.append(item)
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
        elif choice == 3:
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The shopping list is currently empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
