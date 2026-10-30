
# Examination Result and Grace-Mark Validation

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

subjects = []
total = 0
failed = False

MAX_MARK = 100
PASS_MARK = 40
GRACE_LIMIT = 5

for i in range(n):
    print("\nSubject", i + 1)

    subject = input("Enter subject name: ")
    mark = float(input("Enter obtained marks: "))

    if mark < 0 or mark > MAX_MARK:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    grace = 0

    # Apply grace marks
    if 35 <= mark < PASS_MARK:
        grace = min(PASS_MARK - mark, GRACE_LIMIT)

    final_mark = min(mark + grace, MAX_MARK)

    if final_mark < PASS_MARK:
        status = "Fail"
        failed = True
    else:
        status = "Pass"

    total += final_mark

    subjects.append(
        (subject, mark, grace, final_mark, status)
    )

percentage = total / (n * MAX_MARK) * 100

# Final classification
if failed:
    result = "Fail"
elif percentage >= 75:
    result = "Distinction"
elif percentage >= 60:
    result = "First Class"
elif percentage >= 50:
    result = "Second Class"
else:
    result = "Pass"

# Display results
print("\n------ EXAMINATION RESULT ------")
print("Student Name:", name)

print("\nSubject\tOriginal\tGrace\tFinal\tStatus")

for s in subjects:
    print(s[0], "\t", s[1], "\t", s[2],
          "\t", s[3], "\t", s[4])

print("\nTotal Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Final Classification:", result)
