import time

tasks = []

def view_tasks():
    count = 0
    for task in tasks:
        count += 1
        print(f"#{int(count)} {task}")
        
    if not tasks:
        print("There are currently no tasks.")
        
    print("---------------------")
    main()

def add_tasks():
    task_add = input("Enter the name of your task: ").strip().lower()
    tasks.append(task_add)
    print(f"Task '{task_add}' has successfully been added to the tasks list.")
    
    print("---------------------")
    main()
 
    

def delete_tasks():
    if not tasks:
        print("There are currently no tasks.")
        print("---------------------")
        main()
    else:
        task_del = input("Enter the number of the task you wish to delete: ")
        while int(task_del) > len(tasks):
            print("Please enter a value that is present in the task list.")
            task_del = input("Enter the number of the task you wish to delete: ")
        
        print(f"Task '{tasks[int(task_del) - 1]}' has sucessfully been deleted.")
    
        del tasks[int(task_del) - 1]
        main()


def main():
    print("What would you like to do?")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

    choice = input("")
    if choice == "1":
        print("---------------------")
        view_tasks()
        
    elif choice == "2":
        print("---------------------")
        add_tasks()
        
    elif choice == "3":
        print("---------------------")
        delete_tasks()
        
    elif choice == "4":
        print("Exiting the program...")
        exit()
        
    else:
        print("Invalid input. Please try again and choose from the list of options.")
        print("---------------------")
        time.sleep(2)
        main()
        
if __name__ == "__main__":
    main()