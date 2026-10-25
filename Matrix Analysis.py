
# Student Marks Matrix Analysis

students = ["Ravi", "Sita", "Rahul", "Priya"]
subjects = ["Python", "Maths", "English"]

marks = [
    [85, 90, 78],
    [92, 88, 95],
    [65, 70, 60],
    [75, 80, 72]
]

low_limit = 75
totals = []
averages = []

print("--- Student-wise Analysis ---")

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    totals.append(total)
    averages.append(average)
    print(students[i], "Total:", total, "Average:", round(average, 2))

top_score = max(averages)
print("\nTop Performer(s):")
for i in range(len(students)):
    if averages[i] == top_score:
        print(students[i], "Average:", round(averages[i], 2))

print("\n--- Subject-wise Analysis ---")
subject_averages = []

for j in range(len(subjects)):
    column = [marks[i][j] for i in range(len(students))]
    average = sum(column) / len(students)
    subject_averages.append(average)
    print(subjects[j], "Average:", round(average, 2))

print("\nSubjects with Low Average:")
found = False
for j in range(len(subjects)):
    if subject_averages[j] < low_limit:
        print(subjects[j], "Average:", round(subject_averages[j], 2))
        found = True

if not found:
    print("No subjects have a low average.")

print("\nHighest Total Marks:", max(totals))
print("Lowest Total Marks:", min(totals))
print("Class Average:", round(sum(averages) / len(students), 2))
