# Shop inventory
mamu_shop = [
    {"item": "floor", "price": 100, "inventory": 250},
    {"item": "sugar", "price": 180, "inventory": 500},
    {"item": "rice", "price": 300, "inventory": 500},
    {"item": "oil", "price": 500, "inventory": 1000},
    {"item": "ghee", "price": 500, "inventory": 500},
    {"item": "tea", "price": 400, "inventory": 100},
    {"item": "soap", "price": 200, "inventory": 500},
    {"item": "salt", "price": 150, "inventory": 100}
]

# Function to handle the shopping process
def shopping():
    cart = {}
    while True:
        item_name = input("Enter the item name you want to buy or press 'q' to exit: ").lower()
        if item_name == 'q':
            break
        else:
            found = False
            for item in mamu_shop:
                if item["item"] == item_name:
                    found = True
                    if item_name in cart:
                        print("Item already added to the cart.")
                    else:
                        print(f"{item_name} is Rs. {item['price']} per unit.")
                        quantity = float(input("How much do you want? "))
                        if item["inventory"] >= quantity:
                            cart[item_name] = item["price"] * quantity
                            item["inventory"] -= quantity
                            print(f"{quantity} {item_name} added to your cart.")
                        else:
                            print(f"{item_name} is not available in enough quantity.")
                    break
            
            if not found:
                print("Item not found. Please try again.")

    # Generate bill after the shopping is done
    generate_bill(cart)

# Function to generate the bill after shopping
def generate_bill(cart):
    net = total(cart)
    tax = apply_tax(net)
    disc = apply_discount(net)

    print("\nYour Cart Summary:")
    for item, price in cart.items():
        print(f"{item.capitalize()} : Rs. {price:.2f}")
    
    print(f"""
        Total Amount : Rs. {net:.2f}
        Tax Applied  : Rs. {tax:.2f}
        Applied Discount : Rs. {disc:.2f}
        Amount Payable : Rs. {net + tax - disc:.2f}
    """)

# Function to calculate the total amount from the cart
def total(cart):
    total_amount = sum(cart.values())
    return total_amount

# Function to apply discount based on the total amount
def apply_discount(total_amount):
    if total_amount >= 50000:
        disc = total_amount * 0.10
    elif total_amount >= 25000:
        disc = total_amount * 0.05
    elif total_amount >= 10000:
        disc = total_amount * 0.01
    else:
        disc = 0
    return disc

# Function to apply tax based on the total amount
def apply_tax(total_amount):
    if total_amount >= 50000:
        tax = total_amount * 0.05
    elif total_amount >= 25000:
        tax = total_amount * 0.025
    elif total_amount >= 10000:
        tax = total_amount * 0.001
    else:
        tax = 0
    return tax
