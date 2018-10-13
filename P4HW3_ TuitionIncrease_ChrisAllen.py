# Tuition Increase
# 13 Oct 2018
# CTI-110 P4HW3 - Tuition Increase
# Chris Allen
#

# cost of tuition per year
tuition = 8000

# create table layout
print("Year\tTuition Cost")

# determine tuition costs per year
for year in range(1,6): 
    tuition += tuition * .03
    print(year,"\t", format (tuition, ".2f"))
