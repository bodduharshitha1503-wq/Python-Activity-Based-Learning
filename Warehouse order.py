
# Integrated Warehouse Order Prioritization

inventory = {
    "Laptop": 10,
    "Phone": 15,
    "Tablet": 8,
    "Headphones": 20
}

priority_order = {"High": 1, "Medium": 2, "Low": 3}
orders = [
    {"id": 101, "product": "Laptop", "qty": 8, "priority": "High"},
    {"id": 102, "product": "Phone", "qty": 10, "priority": "Medium"},
    {"id": 103, "product": "Tablet", "qty": 12, "priority": "Low"},
    {"id": 104, "product": "Headphones", "qty": 5, "priority": "High"}
]

orders.sort(key=lambda x: priority_order[x["priority"]])

print("--- WAREHOUSE ORDER REPORT ---")

for order in orders:
    product = order["product"]
    quantity = order["qty"]
    order_id = order["id"]
    priority = order["priority"]

    if product not in inventory:
        print("Order", order_id, ": Product unavailable")
        continue

    available = inventory[product]
    fulfilled = min(quantity, available)
    outstanding = quantity - fulfilled

    inventory[product] -= fulfilled

    if outstanding == 0:
        status = "Fully Fulfilled"
    elif fulfilled > 0:
        status = "Partially Fulfilled"
    else:
        status = "Not Fulfilled"

    print("\nOrder ID:", order_id)
    print("Product:", product)
    print("Priority:", priority)
    print("Ordered Quantity:", quantity)
    print("Fulfilled Quantity:", fulfilled)
    print("Outstanding Quantity:", outstanding)
    print("Status:", status)

print("\n--- REMAINING STOCK ---")
for product, stock in inventory.items():
    print(product, ":", stock, "units")

print("\nWarehouse processing completed.")



