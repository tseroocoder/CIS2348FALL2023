# Michelle Oteri
# 2252197
lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
serve = float(input("How many servings does this make?\n"))

# below 4 lines calculates and print output
print("\nLemonade ingredients - yields {:.2f} servings".format(serve))
print("{:.2f} cup(s) lemon juice".format(lemon))
print("{:.2f} cup(s) water".format(water))
print("{:.2f} cup(s) agave nectar".format(agave))

# takes input for servings to make
desire = float(input("\nHow many servings would you like to make?\n"))
# below 4 lines calculates and print output
print("\nLemonade ingredients - yields {:.2f} servings".format(desire))
print("{:.2f} cup(s) lemon juice".format(lemon * desire / serve))
print("{:.2f} cup(s) water".format(water * desire / serve))
print("{:.2f} cup(s) agave nectar".format(agave * desire / serve))

# below 4 lines calculates and print output
print("\nLemonade ingredients - yields {:.2f} servings".format(desire))
print("{:.2f} gallon(s) lemon juice".format(lemon * desire / serve / 16))
print("{:.2f} gallon(s) water".format(water * desire / serve / 16))
print("{:.2f} gallon(s) agave nectar".format(agave * desire / serve / 16))

