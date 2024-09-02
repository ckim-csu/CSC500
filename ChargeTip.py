# Script to calculate total price at restaurant

# Get charge amount
cost = float(input("Food cost: "))

# Calculate tip, tax, and total
tip = cost * .18
tax = cost * .07
total = cost + tip + tax

print("Tip: ", tip)
print("Tax: ", tax)
print("Total: ", total)