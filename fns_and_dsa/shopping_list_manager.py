# shopping_list_manager.py
def display_menu():
    print()
    print("=== Shopping List Manager ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print()

def add_item(shopping_list):
    item = input("Enter item to add (or leave blank to cancel): ").strip()
    if not item:
        print("No item entered — cancelled.")
        return
    shopping_list.append(item)
    print(f'"{item}" added to the shopping list.')

def remove_item(shopping_list):
    if not shopping_list:
        print("Shopping list is empty — nothing to remove.")
        return

    print("Remove by:")
    print("1. Item name")
    print("2. Item number (shown in View List)")
    choice = input("Choose 1 or 2 (or press Enter to cancel): ").strip()

    if choice == "1":
        name = input("Enter the exact item name to remove: ").strip()
        if not name:
            print("No name entered — cancelled.")
            return
        lowered = [s.lower() for s in shopping_list]
        try:
            idx = lowered.index(name.lower())
            removed = shopping_list.pop(idx)
            print(f'"{removed}" removed from the shopping list.')
        except ValueError:
            print(f'Item "{name}" not found in the shopping list.')
    elif choice == "2":
        print("Current shopping list:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
        num = input("Enter item number to remove (or press Enter to cancel): ").strip()
        if not num:
            print("Cancelled.")
            return
        if not num.isdigit():
            print("Invalid number — cancelled.")
            return
        idx = int(num) - 1
        if 0 <= idx < len(shopping_list):
            removed = shopping_list.pop(idx)
            print(f'"{removed}" removed from the shopping list.')
        else:
            print("Number out of range — cancelled.")
    else:
        print("Cancelled or invalid choice.")

def view_list(shopping_list):
    if not shopping_list:
        print("Shopping list is empty.")
        return
    print("Your shopping list:")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
