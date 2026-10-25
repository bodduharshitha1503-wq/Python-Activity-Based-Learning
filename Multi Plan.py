
# Multi-Plan Telecommunications Cost Optimization

plans = [
    {"name": "Plan A", "price": 199, "data": 2, "validity": 28, "extra": 20},
    {"name": "Plan B", "price": 299, "data": 3, "validity": 28, "extra": 15},
    {"name": "Plan C", "price": 399, "data": 5, "validity": 56, "extra": 10},
    {"name": "Plan D", "price": 499, "data": 6, "validity": 84, "extra": 8},
]

usage = float(input("Enter required data per day (GB): "))
days = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs): "))

results = []

print("\n--- Mobile Plan Comparison ---")

for plan in plans:
    total_data = plan["data"] * plan["validity"]
    required_data = usage * days
    excess_data = max(0, required_data - total_data)
    extra_charge = excess_data * plan["extra"]
    total_cost = plan["price"] + extra_charge

    eligible = (
        plan["validity"] >= days
        and total_cost <= budget
        and total_data >= required_data
    )

    print("\nPlan:", plan["name"])
    print("Price: Rs.", plan["price"])
    print("Total Data:", total_data, "GB")
    print("Excess Data:", excess_data, "GB")
    print("Extra Charges: Rs.", extra_charge)
    print("Total Cost: Rs.", total_cost)

    if eligible:
        results.append((plan["name"], total_cost))

if results:
    best_plan = min(results, key=lambda x: x[1])
    print("\n--- Best Eligible Plan ---")
    print("Plan:", best_plan[0])
    print("Total Cost: Rs.", best_plan[1])
else:
    print("\nNo plan satisfies all your requirements.")
    print("Try increasing your budget or choosing lower usage.")
