# Hackerrank problem: take a text and make it split into a input of lines
# Link - https://www.hackerrank.com/challenges/text-wrap/problem

string = (input("Enter a string: "))
wrap = int(input("How many times do you want to wrap this string: "))
l = len(string)
text = []
sub = []
num = 0
counter = 0

# puts string into a list (text)
for i in string:
    text.append(i)
    counter = counter + 1

iteration = 0
additor = counter//wrap

while iteration != additor:
    for x in range(wrap):
        sub.append(text[num])
        num = num + 1
        if num == wrap:
            print(*sub, sep='')
            num = 0
            for i in range(wrap):
                sub.pop()
                text.pop(0)
            break
    iteration = iteration + 1
print(*text, sep='')