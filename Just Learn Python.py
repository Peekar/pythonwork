print('')

arr = 10, 20, 30, 40, 50, 60, 70
sum = 0

for i in arr:
    sum = i + sum

print('Print the sum of every number in "arr"')
print(sum)

#--------------------------------------------------------

credit_str = "xxxx—-xxxx-8888——xxxx"
number = 8
x = []

for i in credit_str:
    if i == '8':
        x.append('8')


print('--------------------------------------------------------')

print('Take "xxxx—-xxxx-8888——xxxx", and print "8" for every 8 in it')
print(*x, sep='')

#--------------------------------------------------------

gadgets = ['Mobile', 'Laptop', 100, 'Camera', 310.28, 'Speakers', 27.00, 'Television', 1000, 'Laptop Case', 'Camera Lens']
strings = []
numbers = []

for i in gadgets:
    if isinstance(i, int) or isinstance(i, float):
        numbers.append(i)
    elif isinstance(i, str):
        strings.append(i)

print('--------------------------------------------------------')

print('Take "gadgets", and print out the items and numbers separately')
print('')
print(f"Strings: {strings}")
print(f"Numbers: {numbers}")

#--------------------------------------------------------
print('--------------------------------------------------------')
print("Take two inputs, and if the second string is a reverse of the first one, print True, else False")
print('')

string = 'ABC' #str(input("Input a string: "))
stringReverse = 'CBA' #str(input("Input another string: "))

if stringReverse == string[::-1]:
    print(True)
else:
    print(False)
#--------------------------------------------------------
print('--------------------------------------------------------')
print("Take an input, if the first and last word are the same, print 'same'")
print('')

string = str(input()).split(' ')

if string[0] == string[-1]:
    print("Same")
else:
    print("Not same")
#--------------------------------------------------------
print('--------------------------------------------------------')
print("Take an input, if the first and last word are the same, print 'same'")
print('')