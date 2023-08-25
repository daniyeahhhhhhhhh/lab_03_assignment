class Task:
    def __init__(self, p_id, start_time, priority):
        self.p_id = p_id
        self.start_time = start_time
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            print(f"Task ID: {task.p_id}, Start Time: {task.start_time}, Priority: {task.priority}")

    def sort_by_p_id(self):
        self.tasks.sort(key=lambda task: task.p_id)

    def sort_by_start_time(self):
        self.tasks.sort(key=lambda task: task.start_time)

    def sort_by_priority(self):
        self.tasks.sort(key=lambda task: task.priority)

def main():
    task_manager = TaskManager()

    while True:
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Sort by P_ID")
        print("4. Sort by Start Time")
        print("5. Sort by Priority")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            p_id = input("Enter Task ID: ")
            start_time = input("Enter Start Time: ")
            priority = input("Enter Priority: ")
            task = Task(p_id, start_time, priority)
            task_manager.add_task(task)
        elif choice == 2:
            task_manager.display_tasks()
        elif choice == 3:
            task_manager.sort_by_p_id()
            print("Tasks sorted by P_ID.")
        elif choice == 4:
            task_manager.sort_by_start_time()
            print("Tasks sorted by Start Time.")
        elif choice == 5:
            task_manager.sort_by_priority()
            print("Tasks sorted by Priority.")
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
