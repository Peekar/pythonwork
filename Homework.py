width = int(input("Enter a number: "))
length = width * 3
width = width // 2
symbol = '.|.'
num = -1

    # top half
for i in range(width):
    num = num + 2
    print((symbol * num).center(length, '-'))

# welcome
print('WELCOME'.center(length, '-'))

# bottom half
for i in range(width):
    print((symbol * num).center(length, '-'))
    num = num - 2