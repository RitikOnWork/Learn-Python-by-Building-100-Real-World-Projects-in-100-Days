# Lists in Python
# Shopping List Application
def display_menu():
    print("Shopping List Menu:")
    print("1. View Shopping List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")
def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")
def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            view_list(shopping_list)
        elif choice == '2':
            add_item(shopping_list)
        elif choice == '3':
            remove_item(shopping_list)
        elif choice == '4':
            print("Exiting the shopping list application.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()