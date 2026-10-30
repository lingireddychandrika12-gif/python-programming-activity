
# ATM Transaction Sequence Simulation

balance = float(input("Enter initial balance: "))

deposit_total = 0
withdraw_total = 0
rejected = 0

limit = 10000

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        rejected += 1

    elif choice == 1:
        balance += amount
        deposit_total += amount
        print("Deposit successful")

    elif choice == 2:
        if amount > limit:
            print("Withdrawal limit exceeded")
            rejected += 1

        elif amount > balance:
            print("Insufficient balance")
            rejected += 1

        else:
            balance -= amount
            withdraw_total += amount
            print("Withdrawal successful")

    else:
        print("Invalid transaction type")
        rejected += 1

# Transaction Summary
print("\n----- ATM SUMMARY -----")
print("Total Deposits:", deposit_total)
print("Total Withdrawals:", withdraw_total)
print("Rejected Transactions:", rejected)
print("Final Balance:", balance)
