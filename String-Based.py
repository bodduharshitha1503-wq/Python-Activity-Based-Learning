
# Advanced String-Based Registration Record Analyzer
import re

records = [
    "REG101|Ravi Kumar|CSE|2006",
    "REG102|Sita Devi|ECE|2005",
    "REG101|Ravi Kumar|CSE|2006",
    "R3|Rahul|IT|2007",
    "REG105|Priya Sharma|CSE|20A6"
]

seen = set()
errors = {}
valid_count = 0

for record in records:
    print("\nRecord:", record)
    fields = record.split("|")
    reasons = []

    if len(fields) != 4:
        reasons.append("Incorrect number of fields")
    else:
        reg_id, name, course, year = fields

        if not re.fullmatch(r"REG\d{3}", reg_id):
            reasons.append("Invalid registration ID format")
        elif reg_id in seen:
            reasons.append("Duplicate registration ID")
        else:
            seen.add(reg_id)

        if not (3 <= len(name) <= 30):
            reasons.append("Invalid name length")
        if not re.fullmatch(r"[A-Z]{2,4}", course):
            reasons.append("Invalid course format")
        if not re.fullmatch(r"\d{4}", year):
            reasons.append("Invalid year format")

    if reasons:
        errors[record] = reasons
        print("Status: INVALID")
        for reason in reasons:
            print("Error:", reason)
    else:
        valid_count += 1
        print("Status: VALID")
        print("Registration ID:", reg_id)
        print("Student Name:", name)
        print("Course:", course)
        print("Year:", year)

print("\n--- ANALYSIS REPORT ---")
print("Total Records:", len(records))
print("Valid Records:", valid_count)
print("Invalid Records:", len(errors))
print("\n--- ERROR CLASSIFICATION ---")

for record, reasons in errors.items():
    print(record, "->", ", ".join(reasons))
