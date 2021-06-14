firstName= "Srikar"  #input("whats your name? ")
lastName = "Kotha"
fullName = firstName + " " + lastName

score1 = 34 #int(input("score1: "))
score2 =  56 #int(input("score2: "))
finalScore = score2 - score1


print("My Name is: " + fullName + ", not done yet,....")
print("Result: " + str(score2-score1) + ", end of program....")
# concatenate format, useful small scale but gets messy with a  lot of variables

print("My name is: %s, my score is %i" % (fullName, finalScore))
# the letters in %s and %i stand for str and int
# the %'s are corrseponding first % to first in parenthsis, and same with the second
# % format

print("My name is: {}, my score is {}" .format(fullName, finalScore))
# .format way
# better than % way because you don't need to define the data type, just need to put the {}
# also has the same corrseponding first to first thing as the % way
print("My name: {first}, my score is: {second}".format(second=finalScore, first=fullName))
# in tis way you can correspond the variables in this cool way, and the first and second can be anything, like a
# variable for the variable

print(f"My name: {fullName}, my score: {finalScore}")
# this is probably the best way, as you can directly enter the varibles. USE THIS!!!!!

# 1. plain format, passing multiple values
# 2. string concatenate : sting join
# 3. using % format
# 4. using format()
# 5. using f-string