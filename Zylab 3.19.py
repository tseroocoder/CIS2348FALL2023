# Michelle Oteri
# 2252197
wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))

# Calculate wall area
wall_area = wall_height * wall_width

# Output the wall area
print("Wall area:", wall_area, "square feet")

# Calculate paint needed
paint_needed = wall_area / 350

# Output the amount of paint needed
print("Paint needed: %.2f gallons" % paint_needed)

# Calculate cans needed (rounded up to the nearest gallon)
import math
cans_needed = math.ceil(paint_needed)

# Output the number of cans needed
print("Cans needed:", cans_needed, "can(s)")

# Dictionary of paint colors and their respective costs
paint_colors = {
    "red": 35,
    "blue": 25,
    "green": 23
}

# Prompt the user to choose a paint color
color_choice = input("\nChoose a color to paint the wall:\n").lower()

# Calculate the total cost of the paint cans
if color_choice in paint_colors:
    cost_per_can = paint_colors[color_choice]
    total_cost = cost_per_can * cans_needed
    print("Cost of purchasing", color_choice, "paint: $%d" % total_cost)
else:
    print("Color not found in the dictionary.")
