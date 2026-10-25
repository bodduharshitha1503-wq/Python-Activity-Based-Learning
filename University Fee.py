
# Integrated University Fee and Eligibility Audit

students = [
    {"name": "Ravi", "fee_paid": 50000, "fee_due": 50000,
     "attendance": 85, "marks": 75},
    {"name": "Sita", "fee_paid": 90000, "fee_due": 90000,
     "attendance": 65, "marks": 80},
    {"name": "Rahul", "fee_paid": 70000, "fee_due": 90000,
     "attendance": 80, "marks": 25},
    {"name": "Priya", "fee_paid": 90000, "fee_due": 90000,
     "attendance": 90, "marks": 85}
]

MIN_ATTENDANCE = 75
MIN_MARKS = 35
outstanding = 0

print("--- UNIVERSITY ELIGIBILITY AUDIT ---")

for student in students:
    reasons = []

    if student["fee_paid"] < student["fee_due"]:
        reasons.append("Fee Payment Pending")

    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Low Attendance")

    if student["marks"] < MIN_MARKS:
        reasons.append("Low Internal Marks")

    print("\nStudent:", student["name"])
    print("Attendance:", student["attendance"], "%")
    print("Internal Marks:", student["marks"])
    print("Fee Paid: Rs.", student["fee_paid"])
    print("Total Fee: Rs.", student["fee_due"])

    if reasons:
        outstanding += 1
        print("Status: NOT ELIGIBLE")
        print("Outstanding Conditions:")
        for reason in reasons:
            print("-", reason)
    else:
        print("Status: ELIGIBLE FOR EXAMINATION")

print("\n--- FINAL AUDIT REPORT ---")
print("Total Students:", len(students))
print("Students with Outstanding Conditions:", outstanding)
print("Eligible Students:", len(students) - outstanding)
print("Audit Completed Successfully.")
