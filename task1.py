
# Attendance Recovery Computation

total_classes = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))
required = float(input("Enter required attendance percentage: "))

# Calculate current attendance
percentage = (attended / total_classes) * 100

print("\nCurrent Attendance:", round(percentage, 2), "%")

if percentage >= required:
    print("You are eligible for exams.")
    print("No extra classes required.")
else:
    # Calculate minimum consecutive classes
    extra = 0

    while True:
        new_percentage = ((attended + extra) /
                          (total_classes + extra)) * 100

        if new_percentage >= required:
            break

        extra += 1

    print("You are not eligible.")
    print("Minimum classes to attend:", extra)

    print("Attendance after recovery:",
          round(new_percentage, 2), "%")
