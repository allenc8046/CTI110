# CTI-110 
# P3HW2 - Shipping Charges 
# Allen 
# 1 Oct 2018
#

# enter weight of package


weight = int (input ("Enter the weight of the package: "))

# display the shipping charge

if weight <= 2:
    print ("Shipping charge: $1.50")
elif weight > 2 and weight <= 6:
    print ("Shipping charge: $3.00")
elif weight > 6 and weight <= 10:
    print ("Shipping charge: $4.00")
else:
    print ("Shipping charge: $4.75")
