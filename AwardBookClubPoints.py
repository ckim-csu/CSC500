# Award points to book club members

numOfBooks = int(input("Number of books purchased this month: "))
totalPoints = 0

if numOfBooks >= 8: 
    totalPoints = 60
elif numOfBooks >= 6:
    totalPoints = 30
elif numOfBooks >= 4:
    totalPoints = 15
elif numOfBooks >= 2:
    totalPoints = 5
else:
    totalPoints = 0

print("Points awarded=", totalPoints)