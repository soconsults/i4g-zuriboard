from datetime import datetime
name = input("What is your name? \n")
allowedUsers = ["Seyi","Tayo","Ade","Kunle","Uche","Amanda","Phillip","Musa"]
allowedPassword = ["PasswordSeyi","Playboy5","Adetade","gold","65432","icing76","kayode5","passWord"] 
howMuch = 0
balance = 0

if (name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)
    if (password == allowedPassword[userId]):
        print("Welcome %s" % name)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. complaints')

        selectedOption = int(input('Please select an option: \n'))
        if (selectedOption == 1):
            print("You have selected %s" % selectedOption)
            howMuch = int(input('How much would ou want to withdraw? \n'))
            print('take your cash')
            balance = balance - howMuch
        elif (selectedOption == 2):
            print("You have selected %s" % selectedOption)
            howMuch = int(input('How much would you like to deposit? \n'))
            balance = balance + howMuch
            print(balance)
        elif (selectedOption == 3):
            print("You have selected %s" % selectedOption)
            issueReport = input('What issue will you like to report? \n')
            print('Thank you for contacting us')
        else:
            print("Invalid option selected, please try again")
    else:
        print("Password incorrect, please try again")   
else:
        print("Name not found, please try again")
