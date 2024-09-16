# Program to calculate average rainfall
import calendar

totalYears = int(input("Input number of years: "))
totalMonths = totalYears * 12
totalRainfall = 0.0
averageRainfall = 0.0

while (totalYears > 0):
    totalYears -= 1

    for i in range(1, 13):
        print("Rainfall for", calendar.month_name[i])
        rainfall = float(input())
        totalRainfall += rainfall

print("Number of months: ", totalMonths)
print("Total rainfall: ", totalRainfall)
print("Avergae Rainfall: ", totalRainfall/totalMonths)