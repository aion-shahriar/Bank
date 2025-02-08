
import random

accounts={}

class Account:
    def __init__(self,name,email,address,account_type,bank):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_count=0
        self.transaction_history = []
        self.account_number = self.generate_account_number()
        self.bank=bank
        
        
        
        
    def generate_account_number(self):
        words=self.name.split()
        account_number = ""
        for word in words:
            account_number += word[0]
        account_number += str(random.randint(1000,9999))
        return account_number
    
        
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print("Deposit successful, amount deposited: ",amount)
        
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print("Withdrawal successful, amount withdrawn: ",amount)
        else:
            print("Insufficient funds")
        
    
    def check_balance(self):
        return self.balance
    
    def show_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)
    
    def apply_for_loan(self,amount):
        if self.loan_count<2:
            loan=self.bank.loan_approval(amount)
            if loan:
                self.balance+=amount
                self.loan_count+=1
                self.bank.total_loan+=amount
                self.transaction_history.append(f"Loan received, amount : {amount}")
                print("Loan approved and amount = ",amount)
            else:
                print("Loan not approved")
        else:
            print("Your limit of taking loon is exceded")
        
    
        
    def transfer(self, amount, receiver_account_number):
        if self.balance < amount:
            print("Insufficient funds")
            return

        
        if receiver_account_number in accounts:
            receiver = accounts[receiver_account_number]
            
            self.withdraw(amount)
            receiver.deposit(amount)
            
            print("Transfer successful")
            self.transaction_history.append(f"Transferred {amount} to {receiver.account_number}")
            receiver.transaction_history.append(f"Received {amount} from {self.account_number}")
        else:
            print("Receiver account not found")


class Bank:
    def __init__(self,total_bank_balance):
        self.total_bank_balance = total_bank_balance
        self.total_loan = 0
        self.loan_limit=100000
    
    def create_account(self, account):
        accounts[account.account_number] = account
        print("Account created successfully with account number: ", account.account_number)

    def find_account(self, account_number):
        return accounts.get(account_number, None)

    def delete_user_account(self, account_number):
        if account_number in accounts:
            del accounts[account_number]
        else:
            return "Account not found"
    
    
    
    def show_all_accounts(self):
        for account_number, account in accounts.items():
            print(account_number, account.name)
    
    def check_bank_balance(self):
        return self.total_bank_balance
    
    def check_total_loan_amount(self):
        return self.total_loan
    
    def check_loan_status(self):
        return self.loan_status
    
    def loan_approval(self,amount):
        if amount>self.loan_limit:
            return False
        else:
            return True



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