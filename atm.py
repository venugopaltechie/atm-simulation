#were are building atm simulation project using core python programming

#atm simulation 
#a basic menu atm should allow
#1.account
#2.login function
#3.check balance
#4.deposit money
#5.withdraw money
#6.exit

#1.account dictoniary(that can used to store the acc info like acc_no,pin,balance)

accounts = {
    "200604": {"pin": "1983", "balance": 2060},
    "192023": {"pin": "0412", "balance": 4067}
}
#2.login function =>{used to login new users and account users}
def login():
    acc_no = input("Enter account number: ")
    pin = input("Enter PIN: ")
    
    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(" Login successful!✅\n")
        atm_menu(acc_no)
    else:
        print("error!❌Invalid account or PIN try❌again \n")

#main interface of account
def atm_menu(acc_no):
    while True:
        print("\n---- ATM Menu ----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            check_balance(acc_no)
        elif choice == "2":
            deposit(acc_no)
        elif choice == "3":
            withdraw(acc_no)
        elif choice == "4":
            print("👋 Thank you for using ATM\n")
            break
        else:
            print("❌ Invalid choice")

#3.check_balance() => {this function is used to check our account balance}

def check_balance(acc_no):
    print(f"\nYour balance is: ₹{accounts[acc_no]['balance']}\n")

#4.deposit => {it can used to deposit amount to our account }

def deposit(acc_no):
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        accounts[acc_no]["balance"] += amount
        print(f" Deposited ₹{amount}")
    else:
        print("ERROR! Invalid amount")

#5.withdraw => {used to withdraw the amount from your account}
def withdraw(acc_no):
    amount = float(input("Enter amount to withdraw: "))

    if 0 < amount <= accounts[acc_no]["balance"]:
        accounts[acc_no]["balance"] -= amount
        print(f"✅ Withdrawn ₹{amount}")
    else:
        print("❌ Insufficient balance or invalid amount")

while True:
    print("\n===== Welcome to ATM =====")
    print("1. Login")
    print("2. Exit")
    option = input("Choose option: ")
    
    if option == "1":
        login()
    elif option == "2":
        print(" 🩻 thank you for visiting!")
        break
    else:
        print("invalid choice try again!")
  
