
# Smart Parking Fee Management System
from datetime import datetime, timedelta

rates = {"Bike": 10, "Car": 30, "Truck": 50}
daily_limit = {"Bike": 100, "Car": 300, "Truck": 500}
penalty = 100

print("SMART PARKING FEE MANAGEMENT")
print("Vehicle types: Bike, Car, Truck")

vehicle = input("Enter vehicle type: ").capitalize()

if vehicle not in rates:
    print("Invalid vehicle type!")
else:
    try:
        entry = input("Enter entry time (HH:MM): ")
        exit_time = input("Enter exit time (HH:MM): ")

        start = datetime.strptime(entry, "%H:%M")
        end = datetime.strptime(exit_time, "%H:%M")

        if end < start:
            end += timedelta(days=1)

        duration = (end - start).total_seconds() / 3600

        if duration <= 0:
            raise ValueError("Invalid parking duration")

        hours = int(duration) + (duration % 1 > 0)
        charge = hours * rates[vehicle]
        days = int(duration // 24)

        if duration >= 24:
            charge = days * daily_limit[vehicle]
            remaining = duration % 24
            charge += min(
                int(remaining) + (remaining % 1 > 0),
                24
            ) * rates[vehicle]
        else:
            charge = min(charge, daily_limit[vehicle])

        overnight = end.date() > start.date()
        if overnight:
            print("Overnight Parking: Yes")
        else:
            print("Overnight Parking: No")

        late = input("Late exit penalty applicable? (yes/no): ").lower()
        if late == "yes":
            charge += penalty

        print("\n--- PARKING BILL ---")
        print("Vehicle:", vehicle)
        print("Duration:", round(duration, 2), "hours")
        print("Parking Fee: Rs.", round(charge, 2))
        print("Penalty: Rs.", penalty if late == "yes" else 0)
        print("Total Amount: Rs.", round(charge, 2))

    except ValueError:
        print("Invalid time! Enter time in HH:MM format.")

