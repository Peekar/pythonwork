string = str(input())
length = len(string)
output = []
proceed = input()

while proceed == 'y':
    for i in range(length):
        output.append(string[length - 1])
        length = length - 1

print(*output, sep="")