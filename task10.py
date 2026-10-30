
# Advanced String-Based Registration Record Analyzer

records = []
roll_numbers = []

n = int(input("Enter number of registration records: "))

for i in range(n):

    print("\nRecord", i + 1)

    data = input("Enter Name,Roll,Email,Phone: ")

    fields = data.split(",")

    errors = []

    if len(fields) != 4:
        print("Error: Invalid number of fields")
        continue

    name = fields[0].strip()
    roll = fields[1].strip()
    email = fields[2].strip()
    phone = fields[3].strip()

    # Validate name
    if len(name) < 3:
        errors.append("Invalid Name")

    # Validate roll number
    if roll == "":
        errors.append("Invalid Roll Number")
    elif roll in roll_numbers:
        errors.append("Duplicate Roll Number")

    # Validate email
    if "@" not in email or "." not in email.split("@")[-1]:
        errors.append("Invalid Email")

    # Validate phone
    if len(phone) != 10 or not phone.isdigit():
        errors.append("Invalid Phone Number")

    # Display result
    if len(errors) == 0:
        records.append([name, roll, email, phone])
        roll_numbers.append(roll)
        print("Registration Successful")
    else:
        print("Registration Failed")
        for error in errors:
            print("-", error)

# Final report
print("\n----- REGISTRATION REPORT -----")

print("\nValid Registration Records:")

for record in records:
    print(record)

print("\nTotal Valid Registrations:", len(records))
print("Total Records Entered:", n)
print("Invalid Records:", n - len(records))

print("\nAnalysis Completed")
