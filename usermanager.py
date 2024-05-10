user_account = {}

def main ():
    print ("\n***Welcome to Dice Roll Game***\n\n 'Wanna Play?\n1. Yes \n2. No")
    
    choice = int(input("Choice: "))

    if choice == 1:
        print ("\nCHOOSE A NUMBER TO CONTINUE\n1. Register\n2. Log-in\n3. Exit")
        choice = int(input("Choice: "))

        while True:
            if choice == 1:
                register()
            if choice == 2:
                log_in()
            if choice == 3:
                print("Logging out.....")
                break
            else:
                 print("\nInvalid Choice. Please try Again")
                 continuation()
    elif choice == 2:
        print ("Exiting...")
        exit
    else:
        exit

def continuation():
    print ("\nCHOOSE A NUMBER TO CONTINUE\n1. Register\n2. Log-in\n3. Exit")
    choice = int(input("Choice: "))

    while True:
        if choice == 1:
            register()
        if choice == 2:
            log_in()
        if choice == 3:
            print("Logging out.....")
            break
        else:
            print("\nInvalid Choice. Please try Again")
            main()

def register ():
    print("\nREGISTER")
    while True:
        try:
            username = input("\nEnter a Username: ")
            if not username:
                main()
            if username in user_account:
                print("\nUsername already exist. Try another username.")
                continue
            while True:
                try:
                    if len(username) < 4:
                        print ("\nUsername must be 4 or more characters. Try Again.")
                        register()
                    else: 
                        password = input("\nInput atleast 8 characters of password: ")
                        if len(password) < 8:
                            print ("\nPassword must be 8 or more characters. Try again")
                            continue
                        else:
                            user_account[username] = {"password" : password}
                            print ("\n\t\tRegistered Successfully!!")
                            continuation()
                except ValueError as e:
                    print(e)
                    register()
        except ValueError as r:
                    print(r)
                    register()

main()