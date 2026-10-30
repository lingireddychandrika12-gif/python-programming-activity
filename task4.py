
# Multi-Stage Examination Eligibility System

name = input("Enter student name: ")

attendance = float(input("Enter attendance percentage: "))
lab = input("Is laboratory completed? (yes/no): ").lower()
internal = float(input("Enter internal assessment marks: "))
fees = input("Are all fees cleared? (yes/no): ").lower()

unmet = []

# Check attendance
if attendance < 75:
    unmet.append("Attendance is below 75%")

# Check laboratory completion
if lab != "yes":
    unmet.append("Laboratory work is incomplete")

# Check internal marks
if internal < 40:
    unmet.append("Internal marks are below 40")

# Check fee clearance
if fees != "yes":
    unmet.append("Fee payment is not cleared")

# Display result
print("\n----- EXAMINATION ELIGIBILITY -----")
print("Student Name:", name)

if len(unmet) == 0:
    print("Status: Eligible for Final Examination")
else:
    print("Status: Not Eligible")
    print("Unmet Requirements:")

    for item in unmet:
        print("-", item)

print("-----------------------------------")
