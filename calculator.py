print("welcome to the python calculator app.")
print("beware! only enter numbers no characters would be accepted.")
while True:
    try:
        no1= float(input("enter 1st number: "))
        no2= float(input("enter 2nd number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
print("Now enter the arithmetic operation you want: \n +, -, *, /")
sign=input(">>")
if sign=="+":
    result=no1+no2
elif sign=="-":
    result=no1-no2
elif sign=="*":
    result=no1*no2
elif sign=="/":
    result=no1/no2
print("Your result is:",result)
input("Press enter to exit")
