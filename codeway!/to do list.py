tasks = []
 
def Add_task():
     task = input("enter a new task ")
     tasks.append(task)
     print("task added successfully")


def View_task():

    if len(tasks) == 0:
        print("no tasks added")
    else:
        print("list of tasks:")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')

def Delete_task():
     if len(tasks) == 0:
        print("no task added")
     else:
            print("tasks:")
            for i, task in enumerate(tasks):
                print(f'{i+1}. {task}')
            
            choice = int(input("enter the task number to delete:"))

            if 0 < choice <= len(tasks):
                del tasks[choice-1]
                print("task deleted succesfully")
            else:
                print("invalid number")


def main():
     while True:
        print('\n')
        print("1.Add_task")
        print("2.View_task")
        print("3.Delete_task")
        print("4.Quit")

        choice = int(input("enter your choice"))
        if choice == 1:
            Add_task()
        elif choice == 2:
            View_task()
        elif   choice == 3:
            Delete_task()
        elif choice == 4:
            print("thank for using") 
            break
        else:
            print("invalide choice")


if __name__ == "__main__":
    main()
