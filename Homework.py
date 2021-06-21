s = input()

print (any(c.isalnum() for c in s))
print (any(c.isalpha() for c in s))
print (any(c.isdigit() for c in s))
print (any(c.islower() for c in s))
print (any(c.isupper() for c in s))

# The any function will see if the string meets ANY of the parameters. For example, in the 3rd line, it is looking if
# any of the contents of the string contain a alphanumeric character, 0-9 or a-z. In the fourth line, it is looking for
# any letter from a-z. If we didn't have the any function, it would look at the string as a whole. If we inputed qA2
# into this code, everything would come True. If we didn't have the any command, it would look to see if the entire
# string was uppercase, or if the entire string was numbers. But if at least one of the numbers is upper case or a
# number, the command will print False.