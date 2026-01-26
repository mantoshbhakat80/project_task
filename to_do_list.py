ta = []
while True:
    print("\nTo-Do List Menu:")
    print("\n1. Add Task")
    print("\n2. View Tasks")
    print("\n3. Remove Task")
    print("\n4. Exit")

    choice = input("Enter your Choice:")

    if choice == "1":
        task = input("Enter your task:")
        ta.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\n TO DO LIST:")
        if len(ta) == 0:
            print("No task in the list.")
        else:
            for i in range(len(ta)):
                print(f"{i+1}.{ta[i]}")
    
    elif choice == "3":
        index = int(input("Enter the index of the task to remove:"))
        if 0 <= index < len(ta):
            removed_task = ta.pop(index)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid index. Please try again.")
    
    elif choice == "4":
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid Choice. Please enter a valid option.")

