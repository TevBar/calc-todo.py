#write a function that adds task to an empty list 

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"added Task: {task}")

def view_tasks():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-do list:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def delete_task(task_number):
    if 0 <= task_number <= len(todo_list):
        remove_task = todo_list.pop(task_number , 1)
        print(f"Deleted task: {remove_task}")


def show_menu():
    print("Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete tasks")
    print("4. Exit")

while True:
    show_menu()
    choice = int(input("Enter Your Choice(1-4):"))

    if choice == 1:
        task = input("enter a new task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        view_tasks()
        try:
            task_number = int(input("enter a task you want to delete: "))
            delete_task(task_number - 1)
        except ValueError:
            print("Invalid input, please enter a number.")
    elif choice == 4:
        print("exiting the program. GoodBye")
        break
    else:
        print("Invalid choice. Please try again")
