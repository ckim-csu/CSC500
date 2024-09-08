# Online Shopping Cart with ItemToPurchase class

class ItemToPurchase:
    item_name = "none"
    item_price = float(0)
    item_quantity = int(0)

    item_total = float(0)

    def __init__(self):
        self.item_name = input("Enter the item name: ")
        self.item_price = float(input("Enter the item price: "))
        self.item_quantity = int(input("Enter the item quantity: "))

        self.item_total = self.item_price * self.item_quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@ $", self.item_price, " = $", self.item_total)

print("Item 1")
item_1 = ItemToPurchase()
print("Item 2")
item_2 = ItemToPurchase()

print("TOTAL COST")
item_1.print_item_cost()
item_2.print_item_cost()
print("Total: $", item_1.item_total + item_2.item_total)
