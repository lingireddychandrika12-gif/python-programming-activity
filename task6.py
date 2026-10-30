
# Smart Canteen Order and Stock Management

stock = {
    "Idli": 20,
    "Dosa": 15,
    "Meals": 10,
    "Juice": 25
}

price = {
    "Idli": 20,
    "Dosa": 40,
    "Meals": 60,
    "Juice": 30
}

sales = 0

n = int(input("Enter number of customers: "))

for i in range(n):

    print("\nCustomer", i + 1)
    print("Available Items:", stock)

    item = input("Enter food item: ").title()
    quantity = int(input("Enter quantity: "))

    if item not in stock:
        print("Item not available")

    elif quantity <= 0:
        print("Invalid quantity")

    elif quantity > stock[item]:
        print("Insufficient stock! Order rejected")

    else:
        bill = price[item] * quantity
        stock[item] -= quantity
        sales += bill

        print("Order successful")
        print("Total Bill: Rs.", bill)

# Daily Summary
print("\n----- DAILY SALES SUMMARY -----")

print("Total Sales: Rs.", sales)

print("\nRemaining Stock:")

for item in stock:
    print(item, ":", stock[item])

print("\nThank you!")
