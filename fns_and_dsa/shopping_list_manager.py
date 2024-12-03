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
            choice = int(input("Enter your choice: "))  # Convert input to integer
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Skip this loop iteration and ask again

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Added: {item}")
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed: {item}")
            else:
                print(f"Item '{item}' not found in the list.")
        elif choice == 3:
            print("Shopping List:")
            if shopping_list:
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
