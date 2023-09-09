import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#main loop
while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
        elif length>0:
            password = generate_password(length)
            print("Generated Password:", password)
            key=input("press 0 if you want to exit,and 1 if you want to continue \nenter here: ")
        if key=="0":
            print("Goodbye")
            break
        
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

input("Press enter to exit program")
