person1 = "Suhas"
person2 = "Mohan"
person3 = "Vasanthi"
# This is not efficient and is not the best way to list information

people = ["Suhas", "Mohan", "Vasanthi"]
# This is a list,  which uses brackets to define it and has words in quotations
# separated by commas
print(people) # The printed list still has brackets, and is not clean
print(*people) # Adding the asterisk takes away the brackets and commas
print(*people, sep=", ") # A separator can be anything, form a simple space to a different word
print(*people, sep=",") # If we didn't add the space before, it would've been like this

print(*people[0], sep="") # We can access certain parts of the list like we would with splicing or range
# the first value is 0, and every thing goes from there


#-----------------------------------------------------------------------#

