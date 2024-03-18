while True:
    password = input("Enter a password: ")
    if len(password) < 5:
        print("No, this password is not good enough.")
    else:
        print("Thank you, your password is good enough.")
        break