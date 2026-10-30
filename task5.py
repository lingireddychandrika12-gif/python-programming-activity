
# Bus Passenger Occupancy Simulation

capacity = int(input("Enter bus capacity: "))
passengers = int(input("Enter initial passengers: "))
stops = int(input("Enter number of stops: "))

for i in range(stops):

    print("\nStop", i + 1)

    boarding = int(input("Enter boarding passengers: "))
    alighting = int(input("Enter alighting passengers: "))

    if boarding < 0 or alighting < 0:
        print("Invalid passenger count")
        continue

    if alighting > passengers:
        print("Invalid: More passengers alighting")
        continue

    passengers = passengers - alighting + boarding

    print("Current passengers:", passengers)

    if passengers > capacity:
        print("Capacity Violation!")
    else:
        print("Available seats:", capacity - passengers)

print("\n----- BUS SUMMARY -----")
print("Bus Capacity:", capacity)
print("Final Passengers:", passengers)
print("Available Seats:", capacity - passengers)
