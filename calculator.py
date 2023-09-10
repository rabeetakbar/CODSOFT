print("welcome to the python calculator app.")
print("beware! only enter numbers no characters would be accepted.")




#main loop
while True:
    try:
        no1= float(input("enter 1st number: "))
        no2= float(input("enter 2nd number: "))
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
        print("press n if you dont want to continue. or any key to start again.\n")
        dec=input(">>>")
        if dec=="n":
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

input("Press enter to exit program")
