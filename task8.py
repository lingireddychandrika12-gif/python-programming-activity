
# Integrated Warehouse Order Prioritization

stock = {
    "Laptop": 10,
    "Mobile": 15,
    "Keyboard": 20
}

orders = []

n = int(input("Enter number of orders: "))

for i in range(n):

    print("\nOrder", i + 1)

    product = input("Enter product name: ").title()
    quantity = int(input("Enter required quantity: "))
    priority = input("Enter priority (High/Medium/Low): ").title()

    if product not in stock:
        print("Product not available")
        continue

    if quantity <= 0:
        print("Invalid quantity")
        continue

    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority")
        continue

    orders.append([product, quantity, priority])

# Sort orders based on priority
priority_order = {"High": 1, "Medium": 2, "Low": 3}

orders.sort(key=lambda x: priority_order[x[2]])

print("\n----- ORDER FULFILMENT REPORT -----")

for order in orders:

    product = order[0]
    required = order[1]
    priority = order[2]

    fulfilled = min(required, stock[product])
    outstanding = required - fulfilled

    stock[product] -= fulfilled

    print("\nProduct:", product)
    print("Priority:", priority)
    print("Required Quantity:", required)
    print("Fulfilled Quantity:", fulfilled)
    print("Outstanding Quantity:", outstanding)

    if outstanding == 0:
        print("Status: Fully Fulfilled")
    else:
        print("Status: Partially Fulfilled")

# Display remaining stock
print("\n----- REMAINING WAREHOUSE STOCK -----")

for product, quantity in stock.items():
    print(product, ":", quantity)
