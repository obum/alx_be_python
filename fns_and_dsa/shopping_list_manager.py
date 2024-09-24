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
        choice = input("Enter your choice: ")

        if choice == '1':
            new_item = input("Enter a new shopping item: ")
            shopping_list.append(new_item)

        elif choice == '2':
            remove_item = input("Enter the item to be removed: ")
            shopping_list = shopping_list.remove(remove_item)
            
        elif choice == '3':
            print(shopping_list)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()