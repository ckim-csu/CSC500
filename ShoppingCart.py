# Shopping Cart script with ItemToPurchase class

class ItemToPurchase:
    item_name = "none"
    item_price = float(0)
    item_quantity = int(0)
    item_description = "none"

    item_total = float(0)

    def __init__(self):
        self.item_name = input("Enter the item name: ")
        self.item_price = float(input("Enter the item price: "))
        self.item_quantity = int(input("Enter the item quantity: "))
        self.item_description = input("Enter the item description: ")

        self.item_total = self.item_price * self.item_quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@ $", self.item_price, " = $", self.item_total)

class ShoppingCart:
    customer_name = "none"
    current_date = "January 1, 2020"
    cart_items = []

    def __init__(self, name, date):
        self.customer_name = name
        self.current_date = date
    
    def add_item(self): # removed ItemToPurchase paramenter--redundant
        added_item = ItemToPurchase()
        self.cart_items.append(added_item)

    def remove_item(self, item):
        for x in self.cart_items:
            if x.item_name == str(item):
                self.cart_items.remove(x)       
            else:
                print("Item not found in cart")
    
    def modify_item(self, item):
        for x in self.cart_items:
            if x.item_name == str(item) and x.item_price != 0.0 and x.item_quantity != 0:
                x.item_price = float(input("Enter the item price: "))
                x.item_quantity = int(input("Enter the item quantity: "))
                x.item_description = input("Enter the item description: ")
            else:
                print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total = 0
        for x in self.cart_items:
            total += x.item_quantity
        return total
    
    def get_cost_of_cart(self):
        total = 0.0
        for x in self.cart_items:
            total += x.item_total
        return total

    def print_total(self):
        if len(self.cart_items) > 0:
            print(self.customer_name,"'s Shopping Cart - ", self.current_date)
            print("Number of items: ", self.get_num_items_in_cart())
            for x in self.cart_items:
                x.print_item_cost()
            print("Total: ", self.get_cost_of_cart())
        else:
            print("SHOPPING CART IS EMPTY")
        

    def print_descriptions(self):
        if len(self.cart_items) > 0:
            print(self.customer_name,"'s Shopping Cart - ", self.current_date)
            print("Item Descriptions")
            for x in self.cart_items:
                print(x.item_name,":",x.item_description)

def print_menu(ShoppingCart):
    acceptable_options = ["a", "r", "c", "i", "o", "q"]

    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    option = input("Choose an option: ")
    
    while option not in acceptable_options:
       option = input("Select valid menu option: ") 

    if option in acceptable_options:        
        if option == "q":
            exit()
        elif option == "a":
            ShoppingCart.add_item()
            return print_menu(ShoppingCart)
        elif option == "r":
            removed_item = input("What item are you removing? ")
            ShoppingCart.remove_item(removed_item)
            return print_menu(ShoppingCart)
        elif option == "c":
            modified_item = input("What item are you modifying? ")
            ShoppingCart.modify_item(modified_item)
            return print_menu(ShoppingCart)
        elif option == "i":
            ShoppingCart.print_descriptions()
            return print_menu(ShoppingCart)
        elif option == "o":
            ShoppingCart.print_total()
            return print_menu(ShoppingCart)
    
JohnDoeCart = ShoppingCart("John Doe", "February 1, 2020")
print_menu(JohnDoeCart)


