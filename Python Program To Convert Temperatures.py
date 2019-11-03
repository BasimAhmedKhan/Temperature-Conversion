print(" ")
print('                 "Python Program To Convert Temperatures"')
print(" ")
print("Select Operation!")
print(" ")
print("1.Celsius To Fahrenheit,Kelvin")
print(" ")
print("2.Fahrenheit To Celsius,Kelvin")
print(" ")
print("3.Kelvin To Fahrenheit,Celsius")
print(" ")

choice = int(input("Enter Choice(1/2/3): "))
print(" ")

if choice == 1:
    temp1 = float(input("Enter Celsius: "))
    print(" ")
    ans1 = (temp1 * 9/5) + 32
    ans2 = (temp1 + 273.15)
    print(str(temp1) + " Degree Celsius" + " is Equal To " + str(ans1) + " Fahrenheit")
    print(" ")
    print(str(temp1) + " Degree Celsius" + " is Equal To " + str(ans2) + " kelvin")
    print(" ")

elif choice == 2:
    temp2 = float(input("Enter Fahrenheit: "))
    ans3 = (temp2 - 32) * 5/9
    ans4 = (temp2 - 32) * 5/9 + 273.15
    print(" ")
    print(str(temp2) + " Farenheit" + " is Equal To " + str(ans3) + " Celsius")
    print(" ")
    print(str(temp2) + " Farenheit" + " is Equal To " + str(ans4) + " Kelvin")
    print(" ")

elif choice == 3:
    temp3 = float(input("Enter Kelvin: "))
    ans5 = (temp3 - 273.15) * 9/5 + 32
    ans6 = (temp3 - 273.15)
    print(" ")
    print(str(temp3) + " Kelvin" + " is Equal To " + str(ans5) + " Farenheit")
    print(" ")
    print(str(temp3) + " Kelvin" + " is Equal To " + str(ans6) + " Celsius")
    print(" ")

else:
    print("Invalid Input!")