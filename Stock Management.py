
# Smart Canteen Order and Stock Management

menu = {
    "Idly": {"price": 30, "stock": 20},
    "Dosa": {"price": 40, "stock": 15},
    "Meals": {"price": 80, "stock": 10},
    "Juice": {"price": 25, "stock": 12}
}

sales = 0
orders = 0

print("SMART CANTEEN MANAGEMENT")
print("\nMenu:")
for item, details in menu.items():
    print(item, "- Rs.", details["price"],
          "| Stock:", details["stock"])

while True:
    item = input("\nEnter item name (or 'done'): ").title()

    if item.lower() == "done":
        break

    if item not in menu:
        print("Item not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be positive!")
            continue

        if quantity > menu[item]["stock"]:
            print("Insufficient stock!")
            print("Available:", menu[item]["stock"])
            continue

        bill = menu[item]["price"] * quantity
        menu[item]["stock"] -= quantity
        sales += bill
        orders += 1

        print("Order successful!")
        print("Item:", item)
        print("Quantity:", quantity)
        print("Bill: Rs.", bill)

    except ValueError:
        print("Please enter a valid whole number!")

print("\n--- DAILY SALES SUMMARY ---")
print("Successful Orders:", orders)
print("Total Sales: Rs.", sales)
print("\nRemaining Stock:")

for item, details in menu.items():
    print(item, ":", details["stock"], "units")
