with open("tasks.txt", "r") as f:
    tasks = f.readlines()

with open("tasks.txt", "r") as f:
    for line in f:
        tasks.append(line.strip())
try:
    with open("tasks.txt", "r") as f:
        tasks = [line.strip() for line in f]
except FileNotFoundError:
    tasks = []

while True:
    print("=======================================================")
    print(" [1] Add task [2] View tasks [3] Remove Tasks [4] Quit")
    print("=======================================================")

    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Invalid Input, Please input a correct number!")
        continue

    if choice == 1:
        task = str(input("Enter task: "))
        tasks.append(task)

    elif choice == 2:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == 3:
        index = int(input("Which task number to remove? ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
        else:
            print("Invalid task number!")

    elif choice == 4:
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
        break

    else:
        print("Can't find that option, please input a correct number(1 - 4)!")