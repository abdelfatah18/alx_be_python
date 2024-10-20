def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        # Check if the input is a valid number
        if not choice.isdigit():
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue  # Skip to the next iteration of the loop

        choice = int(choice)  # Convert the choice to an integer

        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")
        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
