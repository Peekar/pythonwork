# Hackerrank problem: find the second highest score of a competition.
# Link - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

scores = list(input().split())
length = len(scores) - 2
scores.sort()
first = scores[length]
print("Runner-up score is " + scores[length])

# or this method found on the internet

scores = list(input().split())
length = len(scores) - 1
first = scores[length]
while scores[length] == first:
    scores.append(first)
    length = length - 1
print("Runner-up score is " + scores[length])