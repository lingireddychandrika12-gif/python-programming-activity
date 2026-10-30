
# Campus Festival Registration and Financial Audit

participants = []
registration_fee = 200

total_fees = 0

n = int(input("Enter number of registrations: "))

for i in range(n):

    name = input("\nEnter participant name: ").strip().title()

    if name in participants:
        print("Duplicate registration rejected")

    elif name == "":
        print("Invalid participant name")

    else:
        participants.append(name)
        total_fees += registration_fee
        print("Registration successful")

# Sponsorship and expenses
sponsorship = float(input("\nEnter sponsorship amount: "))
expenses = float(input("Enter total festival expenses: "))

# Financial calculation
total_income = total_fees + sponsorship
balance = total_income - expenses

# Display report
print("\n----- FESTIVAL AUDIT REPORT -----")

print("Registered Participants:", participants)
print("Total Participants:", len(participants))
print("Registration Fees: Rs.", total_fees)
print("Sponsorship: Rs.", sponsorship)
print("Total Income: Rs.", total_income)
print("Festival Expenses: Rs.", expenses)
print("Final Balance: Rs.", balance)

if balance > 0:
    print("Financial Status: Profit")
elif balance < 0:
    print("Financial Status: Loss")
else:
    print("Financial Status: No Profit No Loss")
