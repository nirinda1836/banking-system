from bank import BankAccount 
accounts = {}
while True:
    print("\n ---BANK MENU---")
    print("1.create account: ")
    print("2.withdraw:")
    print("3. deposit: ")
    print("4.check balance:")
    print("5.display account: ")
    print("6.exit")
    choice = int(input("enter your choice: "))
    if choice == 1:
        name = input("enter your name: ")
        acc_no = input("enter account number: ")
        accounts[acc_no] = BankAccount(name,acc_no)
        print("account created successfully ")
    elif choice == 2:
        amount = int(input("enter withdraw amount: "))
        accounts[acc_no].withdraw(amount)
    elif choice == 3:
        amount = int(input("enter deposit amount: "))
        accounts[acc_no].deposit(amount)
    elif choice == 4:
        accounts[acc_no].balance()
    elif choice == 5:
        accounts[acc_no].display()
    else:
        print("exit")
