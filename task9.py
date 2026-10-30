
# Examination Question Difficulty and Performance Analysis

students = int(input("Enter number of students: "))
questions = int(input("Enter number of questions: "))

key = []

print("\nEnter correct answers:")
for i in range(questions):
    ans = input("Question " + str(i+1) + ": ").strip().upper()
    key.append(ans)

correct_count = [0] * questions

# Collect student answers
for i in range(students):
    print("\nStudent", i+1)

    for j in range(questions):
        ans = input("Answer for Q" + str(j+1) + ": ").strip().upper()

        if ans == key[j]:
            correct_count[j] += 1

# Question-wise analysis
success_rates = []

print("\n----- QUESTION PERFORMANCE -----")

for i in range(questions):

    rate = (correct_count[i] / students) * 100
    missed = students - correct_count[i]

    success_rates.append(rate)

    if rate >= 75:
        level = "Easy"
    elif rate >= 40:
        level = "Moderate"
    else:
        level = "Difficult"

    print("\nQuestion:", i+1)
    print("Correct Answers:", correct_count[i])
    print("Missed Answers:", missed)
    print("Success Rate:", round(rate, 2), "%")
    print("Difficulty:", level)

# Find most frequently missed questions
max_missed = students - min(correct_count)

print("\n----- MOST MISSED QUESTIONS -----")

for i in range(questions):
    missed = students - correct_count[i]

    if missed == max_missed:
        print("Question", i+1, "Missed by", missed, "students")

print("\nAnalysis Completed")
