#Michelle Oteri
#2252197
# Dictionary of automotive services and their costs
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12
}

# Output the menu of automotive services
print("Davy's auto shop services")
for service, cost in services.items():
    print(service, "-- $" + str(cost))

# Prompt the user for the first service
service1 = input("\nSelect first service:\n")

# Prompt the user for the second service
service2 = input("Select second service:\n")

# Output the invoice
print("Davy's auto shop invoice\n")
total_cost = 0

# Service 1
if service1 in services:
    cost1 = services[service1]
    print("Service 1:", service1 + ",", "$" + str(cost1))
    total_cost += cost1
else:
    print("Service 1: No service")

# Service 2
if service2 in services:
    cost2 = services[service2]
    print("Service 2:", service2 + ",", "$" + str(cost2))
    total_cost += cost2
else:
    print("Service 2: No service")

# Total cost
print("\nTotal: $" + str(total_cost))




