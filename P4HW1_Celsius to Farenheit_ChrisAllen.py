# Celsius to Farenheit Table
# 10 Oct 18
# CTI-110 P4HW1 - Celsius to Farenheit Table
# Chris Allen
#

# This is what the program will do
print ("This program will convert Celsius to Fahrenheit from 0 to 20.")
# convert and print the temperatures
print("Celsius\tFahrenheit")
print("------------------")
for Celsius in range (0,21):
    Fahrenheit = 9/5*Celsius+32
    print(Celsius,"\t",format (Fahrenheit, ".1f"))
