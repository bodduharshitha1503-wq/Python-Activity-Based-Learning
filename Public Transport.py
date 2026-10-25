
# Smart Public Transport Fare Reconciliation

routes = {
    "A": 20,
    "B": 35,
    "C": 50
}

categories = {
    "Adult": 1.0,
    "Student": 0.5,
    "Senior": 0.7
}

expected_revenue = 0
collected_revenue = 0
records = []

print("PUBLIC TRANSPORT FARE SYSTEM")
print("Routes:", routes)
print("Categories:", categories)

n = int(input("Enter number of passenger records: "))

for i in range(n):
    print("\nPassenger", i + 1)
    route = input("Enter route (A/B/C): ").upper()
    category = input("Enter category (Adult/Student/Senior): ").title()

    if route not in routes or category not in categories:
        print("Invalid route or passenger category!")
        continue

    try:
        count = int(input("Enter passenger count: "))
        collected = float(input("Enter collected fare (Rs): "))

        if count <= 0 or collected < 0:
            print("Invalid passenger count or fare!")
            continue

        fare = routes[route] * categories[category]
        expected = fare * count
        difference = collected - expected

        expected_revenue += expected
        collected_revenue += collected
        records.append((route, category, expected, collected, difference))

        print("Expected Fare: Rs.", expected)
        print("Collected Fare: Rs.", collected)
        print("Difference: Rs.", difference)

    except ValueError:
        print("Enter valid numeric values!")

print("\n--- RECONCILIATION REPORT ---")
print("Expected Revenue: Rs.", expected_revenue)
print("Collected Revenue: Rs.", collected_revenue)
print("Overall Difference: Rs.", collected_revenue - expected_revenue)

print("\n--- DISCREPANCIES ---")
for r, c, e, a, d in records:
    if abs(d) > 0.01:
        print(r, c, "Expected:", e, "Collected:", a, "Difference:", d)

if abs(collected_revenue - expected_revenue) <= 0.01:
    print("Revenue fully reconciled.")
