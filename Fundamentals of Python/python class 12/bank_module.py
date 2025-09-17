import random

# List to store all accounts
all_accounts = []

# Function to open a new account
def open_account():
    account_title = input("Account Title: ")
    cnic = input("CNIC: ")
    contact = input("Contact Number: ")
    initial_deposit = int(input("Initial Deposit: "))
    account_number = random.randint(10000, 99999)
    account = {
        "title": account_title,
        "cnic": cnic,
        "contact": contact,
        "balance": initial_deposit,
        "account_number": account_number
    }
    all_accounts.append(account)
    print("Your account opened successfully.")
    print(f"Your account title is {account['title']} and account number is {account['account_number']}.")


# Function to deposit cash into an account
def cash_deposit(acc_num, amount):
    if amount > 0:   
        for acc in all_accounts:
            if acc["account_number"] == acc_num:
                acc["balance"] += amount
                print("Amount deposited successfully.")
                break
        else:
            print("Invalid Account Number.")
    else:
        print("Invalid Amount.")


# Function to check the balance of an account
def check_balance(acc_num):
    for acc in all_accounts:
        if acc["account_number"] == acc_num:
            print(f"Your account balance is Rs: {acc['balance']}.")
            break
    else:
        print("Invalid Account Number.")


# Function to withdraw cash from an account
def cash_withdrawal(acc_num, amount):
    for acc in all_accounts:
        if acc["account_number"] == acc_num:
            if acc["balance"] >= amount:
                acc["balance"] -= amount
                print(f"Here is your amount Rs. {amount}.")
                break
            else:
                print("Insufficient Balance.")
                break
    else:
        print("Invalid Account Number.")


# Function to close an account
def close_account(acc_num):
    for i, acc in enumerate(all_accounts):
        if acc["account_number"] == acc_num:
            print(f"Here is your amount Rs. {acc['balance']}.")
            acc["balance"] = 0
            del all_accounts[i]
            print("Your account closed successfully.")
            break
    else:
        print("Invalid Account Number.")


# Function to transfer amount from one account to another
def transfer_amount(from_account, amount, to_account):
    # Initialize variables to store the account information
    from_acc = None
    to_acc = None

    # Find the from_account and to_account in all_accounts
    for account in all_accounts:
        if account["account_number"] == from_account:
            from_acc = account  # Found the from account
        elif account["account_number"] == to_account:
            to_acc = account  # Found the to account

    # Check if both accounts were found
    if from_acc is None:
        print("Invalid from Account.")
        return  # Exit the function if from_account is not found
    if to_acc is None:
        print("Invalid to Account.")
        return  # Exit the function if to_account is not found

    # Check if the from_account has sufficient balance
    if from_acc["balance"] < amount:
        print("Insufficient funds in the from account.")
        return  # Exit the function if there are not enough funds

    # Perform the transfer: subtract from from_account and add to to_account
    from_acc["balance"] -= amount
    to_acc["balance"] += amount

    print(f"Transfer successful! {amount} transferred from account {from_account} to account {to_account}.")
    print(f"New balance of from account: {from_acc['balance']}.")
    print(f"New balance of to account: {to_acc['balance']}.")


# You can add more functionality as needed, for example:
# - List all accounts
# - Search for accounts by account number, CNIC, or contact
# - Generate account statements

