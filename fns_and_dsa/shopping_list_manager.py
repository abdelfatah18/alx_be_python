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
        
        # Input validation for menu choice
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if choice == 1:
            item = input("Enter your item: ")
            shopping_list.append(item)
            print(f"Item '{item}' has been added to the shopping list.")
        
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Item '{item}' has been removed from the shopping list.")
            else:
                print(f"Item '{item}' not found in the shopping list.")
            
        elif choice == 3:
            if shopping_list:
                print("The shopping list contains:")
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
