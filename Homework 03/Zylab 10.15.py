# Michelle Oteri
#2252197
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")

def input_item_details(item_num):
    print(f"Item {item_num}")
    item_name = input("Enter the item name:\n")
    item_price = float(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))
    return ItemToPurchase(item_name, item_price, item_quantity)

if __name__ == "__main__":
    item1 = input_item_details(1)
    item2 = input_item_details(2)

    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"Total: ${total_cost}”)