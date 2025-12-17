# Note Taking Application
def display_menu():
    print("Note Taking Application")
    print("1. Create a new note")
    print("2. View existing notes")
    print("3. Delete a note")
    print("4. Exit")
def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    with open(f"{title}.txt", "w") as file:
        file.write(content)
    print(f"Note '{title}' created successfully.")
def view_notes():
    import os
    notes = [f for f in os.listdir() if f.endswith('.txt')]
    if not notes:
        print("No notes found.")
        return
    for note in notes:
        print(f"- {note[:-4]}")
    title = input("Enter the title of the note to view: ")
    try:
        with open(f"{title}.txt", "r") as file:
            content = file.read()
            print(f"Content of '{title}':\n{content}")
    except FileNotFoundError:
        print(f"Note '{title}' not found.")
def delete_note():
    title = input("Enter the title of the note to delete: ")
    try:
        import os
        os.remove(f"{title}.txt")
        print(f"Note '{title}' deleted successfully.")
    except FileNotFoundError:
        print(f"Note '{title}' not found.")
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            create_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()