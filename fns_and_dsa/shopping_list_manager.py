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
        choice = int(input("Enter your choice: "))
        if choice == 1 :
            item=input("enter your item : ")
            print(f"item {item}  is added")
            shopping_list.append(item)
        elif choice == 2:
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
            
        elif choice == 3:
                print("The shopping list is currently empty.")
            
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
