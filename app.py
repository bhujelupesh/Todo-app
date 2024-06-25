class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print(f"Task {task_number} deleted!")
        except IndexError:
            print("Invalid task number.")

    def update_task(self, task_number):
         try:
            task = input("Enter new task: ")
            self.tasks[task_number - 1] = task
            print(f"Task {task_number} updated!")
        except IndexError:
            print("Invalid task number.")

def main():
    app = TodoApp()

    while True:
        print("\nTodo App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            app.add_task(task)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            app.delete_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to update: "))
            app.update_task(task_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
