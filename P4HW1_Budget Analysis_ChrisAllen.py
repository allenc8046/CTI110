# Budget Analysis
# 10 Oct 18
# CTI-110 P4HW1 - Budget Analysis
# Chris Allen
#

# enter the budget for the month

totalBudget = float(input("Enter the total budget for the month: "))
purchases = int(input("Enter the number of purchases were made this month: "))

# create accumulator variable

total = 0

# start the loop

for num in range (purchases):
    # ask user to enter the costs of the purchases
    costs = float(input("What was the purchase cost: "))

    total += costs
    
# display total costs
print ("\nTotal costs: $",total,sep="")

# determine if total costs of purchases are over or under budget

if total > totalBudget:
    print("You are over budget for this month!")
elif total <= totalBudget:
    print("You are at or under budget for the month!")
