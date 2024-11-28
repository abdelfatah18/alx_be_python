def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Display menu options
        
        try:
            choice = int(input("Enter your choice: "))  # Try converting input to an integer
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Skip the current iteration if input is not a valid number

        if choice == 1:  # Add Item
            item = input("Enter the name of the item to add: ")
            shopping_list.append(item)  # Add item to the list
            print(f"{item} has been added to the shopping list.")

        elif choice == 2:  # Remove Item
            item = input("Enter the name of the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item if it exists
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} is not in the shopping list.")

        elif choice == 3:  # View List
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is empty.")

        elif choice == 4:  # Exit
            print("Goodbye!")
            break  # Exit the loop and end the program

        else:  # Invalid choice (not 1, 2, 3, or 4)
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
