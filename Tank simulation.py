
# Multi-Day Water Tank Simulation

capacity = float(input("Enter tank capacity (litres): "))
water = float(input("Enter initial water level (litres): "))
threshold = float(input("Enter target threshold (litres): "))
days = int(input("Enter number of days: "))

if capacity <= 0 or days <= 0:
    print("Invalid capacity or number of days!")
elif water < 0 or water > capacity:
    print("Invalid initial water level!")
elif threshold < 0 or threshold > capacity:
    print("Invalid threshold!")
else:
    first_interval = None
    print("\n--- Water Tank Simulation ---")

    for day in range(1, days + 1):
        inflow = float(input(f"Day {day} inflow (litres): "))
        outflow = float(input(f"Day {day} outflow (litres): "))

        if inflow < 0 or outflow < 0:
            print("Invalid quantity! Use positive values.")
            break

        previous = water
        water = water + inflow - outflow

        if water > capacity:
            overflow = water - capacity
            water = capacity
            print("Overflow:", overflow, "litres")
        else:
            print("Overflow: 0 litres")

        if water < 0:
            shortage = abs(water)
            water = 0
            print("Shortage:", shortage, "litres")
        else:
            print("Shortage: 0 litres")

        print("Day:", day)
        print("Water Level:", water, "litres")

        if first_interval is None and water >= threshold:
            first_interval = day
            print("Target threshold reached!")

    if first_interval is not None:
        print("\nFirst threshold interval: Day", first_interval)
    else:
        print("\nThreshold was not reached.")

    print("Final Water Level:", water, "litres")
