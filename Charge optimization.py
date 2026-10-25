
# Courier Charge Optimization

services = {
    "Standard": {"rate": 40, "days": 5},
    "Express": {"rate": 70, "days": 2},
    "SameDay": {"rate": 120, "days": 1}
}

weight = float(input("Enter parcel weight (kg): "))
length = float(input("Enter length (cm): "))
width = float(input("Enter width (cm): "))
height = float(input("Enter height (cm): "))
zone = int(input("Enter distance zone (1-3): "))
urgency = input("Enter urgency (normal/urgent): ").lower()
restricted = input("Restricted item? (yes/no): ").lower()
budget = float(input("Enter your budget (Rs): "))

if weight <= 0 or min(length, width, height) <= 0:
    print("Invalid parcel measurements!")
elif zone not in [1, 2, 3] or budget < 0:
    print("Invalid zone or budget!")
elif restricted == "yes":
    print("Parcel cannot be accepted due to restrictions.")
elif restricted != "no" or urgency not in ["normal", "urgent"]:
    print("Invalid restriction or urgency input.")
else:
    volume = length * width * height
    volumetric_weight = volume / 5000
    chargeable_weight = max(weight, volumetric_weight)
    options = []

    print("\n--- Courier Service Comparison ---")

    for name, service in services.items():
        if urgency == "urgent" and name == "Standard":
            continue

        base = service["rate"] * chargeable_weight
        distance_charge = base * (zone - 1) * 0.5
        total = base + distance_charge

        if chargeable_weight > 10:
            total += 100

        print(name, "Charge: Rs.", round(total, 2))

        if total <= budget:
            options.append((total, name, service["days"]))

    if options:
        best = min(options)
        print("\nBest Service:", best[1])
        print("Delivery Time:", best[2], "day(s)")
        print("Total Charge: Rs.", round(best[0], 2))
    else:
        print("\nNo service fits your budget.")
