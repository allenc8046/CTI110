# Bug Collector
# 10 Oct 18
# CTI-110 P4T2 - Bug Collector
# Chris Allen
#

# enter number of days bugs were collected

days = int(input("enter number of days to add up: "))

# create accumulator variable

total = 0

# start the loop

for num in range (days):
    # ask user to enter number of bugs collected
    bugs = int(input("Number of bugs collected: "))

    total += bugs
    # or use augmented assignment of total += bugs

# display total bugs collected
print ("\nTotal bugs collected: ",total)
