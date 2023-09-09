# Define a list to store the to-do items
to_do_list = []

# Function to display the to-do list
def display_to_do_list():
    if to_do_list:
        print("To-Do List:")
        for index, item in enumerate(to_do_list, start=1):
            print(str(index) + ". " + item)
    else:
        print("Your to-do list is empty.")

# Function to add a task to the to-do list
def add_task(task):
    to_do_list.append(task)
    print("Added: " + task)

# Function to remove a task from the to-do list
def remove_task(index):
    if 1 <= index <= len(to_do_list):
        removed_task = to_do_list.pop(index - 1)
        print("Removed: " + removed_task)
    elif index==0:
        print("No task removed")
    else:
        print("Invalid index.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_to_do_list()
    elif choice == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "3":
        display_to_do_list()
        index = int(input("Enter the index of the task to remove (or 0 to cancel): "))
        remove_task(index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
input("press enter to exit program")
