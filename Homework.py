from typing import List

iterations = int(input("How many commands do you want to enter?: "))
print("")
list = []
iterationNum = 0

for i in range(iterations):
    iterationNum = iterationNum + 1
    commandInput = input(f"What command do you want to enter? (command {iterationNum}/{iterations}): ")
    command = commandInput.split()
    commandWord = command[0]

    if  commandWord == 'insert':
        index = int(command[2])
        list.insert(index, command[1])
    elif commandWord == 'print':
        print(*list)
    elif commandWord == 'remove':
        list.remove(command[1])
    elif commandWord == 'append':
        list.append(command[1])
    elif commandWord == 'sort':
        list.sort()
    elif commandWord == 'pop':
        list.pop()
    elif commandWord == 'reverse':
        list.reverse()
    else:
        print("Something went wrong, please try again.")