<<<<<<< HEAD
school = "kilLIAn"
name = "sRikAr KOthA"
# We want to get the first letter upper and the rest lower in Killian, to make it a proper noun

print(school[0]) # This will show us the first character in the list, starting from 0
# (if you go over the number of characters in the string, there will be a out of range error)

length = len(school) # creating a variable for the length of the school
print(length)
print(length-2)

# print(variable[<start (characters start at 0) dft-0>:<end dft-last (length start at 1) character>:<increment dft-1>]) dft is default
print(school[2:7:])
print(school[2::2])
print(school[5:1:-1])

print(school[0].upper() + school[1:].lower()) # Using everything, we have solved it!!!

# We can also use .upper(), .lower(), and .capitalize can do things some things as well
print(school.upper())
print(school.lower())
=======
school = "kilLIAn"
name = "sRikAr KOthA"
# We want to get the first letter upper and the rest lower in Killian, to make it a proper noun

print(school[0]) # This will show us the first character in the list, starting from 0
# (if you go over the number of characters in the string, there will be a out of range error)

length = len(school) # creating a variable for the length of the school
print(length)
print(length-2)

# print(variable[<start (characters start at 0) dft-0>:<end dft-last (length start at 1) character>:<increment dft-1>]) dft is default
print(school[2:7:])
print(school[2::2])
print(school[5:1:-1])

print(school[0].upper() + school[1:].lower()) # Using everything, we have solved it!!!

# We can also use .upper(), .lower(), and .capitalize can do things some things as well
print(school.upper())
print(school.lower())
>>>>>>> 563417c33fd85f0616db6fad0ec5d9812888c71f
print(school.capitalize())