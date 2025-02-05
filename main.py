
from admin import Account, Bank
from database import accounts

bank=Bank(100000000)



while True:
    
    print('1. User')
    print('2. Admin')
    print('3. Exit')
    print('Select an option: ', end='')
    option = int(input())
    if option ==3 :
        break
    elif option == 1:
        
        
        
        while True:
            print('1. Create account')
            print("2. Check balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. Check Transaction History")
            print("7. Apply for loan")
            print("8. Exit")
            print("Select an option: ", end='')
            
            
            
            
            option = int(input())
            
            if option == 1:
                print("Enter your name: ", end='')
                name = input()
                print("Enter your email: ", end='')
                email = input()
                print("Enter your address: ", end='')
                address = input()
                print("Enter your account type: ", end='')
                account_type = input()
                account = Account(name,email,address,account_type,bank)
                accounts[account.account_number] = account
                print("Account created successfully" + " with account number: " + str(account.account_number))
                
            elif option in [2,3,4,5,6,7]:
                account_number = input("Enter your account number: ")
    
                if account_number not in accounts:
                    print('Enter a valid account number')
                    continue
                
                account = accounts[account_number]
                
                
                
                if option == 2:
                    print(account.check_balance())
                elif option == 3:
                    amount = input("Enter amount to deposit: ")
                    amount = int(amount)
                    account.deposit(amount)
                elif option == 4:
                    amount = input("Enter amount to withdraw: ")
                    amount = int(amount)
                    account.withdraw(amount)
                    
                elif option == 5:
                    receiver_account = input("Enter account number to transfer to: ")
                    
                    amount = int(input("Enter amount to transfer: "))
                    receiver = bank.find_account(receiver_account) 
                    
                    if receiver:
                        account.transfer(amount, receiver_account) 
                    else:
                        print("Enter a valid account number.")
                    

                    
                        
                elif option == 6:
                    account.show_transaction_history()
                elif option == 7:
                    amount = input("Enter amount to apply for loan: ")
                    amount = int(amount)
                    account.apply_for_loan(amount)
            elif option == 8:
                break
        
    elif option == 2:
        print("Enter your password: ")
        password = input()
        if password == "admin":
            
            while True:
                print("1. Delete account")
                print("2. Show all accounts")
                print("3. Check bank balance")
                print("4. Exit")
                print("Select an option: ", end='')
                
                option = int(input())
                
                if option == 1:
                    account_number = input("Enter account number to delete: ")
                    acc=bank.find_account(account_number)
                    if acc:
                        bank.delete_user_account(account_number)
                        print("Account deleted")
                    else:
                        print("Account does not exist")
                    
                elif option == 2:
                    if accounts:
                        for account in accounts.values():
                            print(vars(account))
                    else:
                        print("No accounts")
                        
                elif option == 3:
                    print(bank.check_bank_balance())
                elif option == 4:
                    break
        else:
            print("Invalid password")