print("=== Welcome to Python SuperMart ===")
# predefined product list with prices

products = {
    "apple" : 50,
    "banana": 20,
    "milk": 40,
    "bread": 30,
    "egg": 10,
}

cart = {} #Empty cart dictionary

while True:
    print("\n---------Menu----------")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:  #Add to cart
        print("\nAvailable Products:")
        for item, price in products.items(


        ):
            print(f"{item.title()} - ₹{price}")

    elif choice == 2:  #Add to cart
        item = input("Enter product name: ").lower()
        if item in products:
            qty = int(input(f"Enter quantity of {item}: "))
            if qty > 0:
                cart[item] = cart.get(item, 0) + qty

                print(f" ✓ {qty} {item}(s) added to cart. ")

            else:
                print(" ✖ Quantity must be greater than 0.")
        else:
            print("✖ Product not available. ")

    elif choice == 3:  #view cart
        if cart:
            print("\n🛒  Your cart")
            total = 6
            for item, qty in cart.items():
                price = products[item] * qty
                total +=price
                print(f"{item.title()} (*{qty}) = ₹{price}")

            print(f"Total (without discount): ₹{price}")
        else:
            print("🛒 Your cart is empty.")

    elif choice == 4:  #checkout
        if cart:
            total = sum(products[item]*qty for item, qty in cart.items())

            #Apply discount based on amount
            if total>= 500:
                discount = total * 0.1  #10% discount
            elif total >= 200:
                discount = total *0.05  #5% discount
            else:
                discount = 0

            final_amount = total - discount
            print("\n 💰 Checkout Bill:")
            for item, qty in cart.items():
                print(f"{item.title()}  (x{qty}) = ₹{products[item] * qty}")
            print(f"Total: ₹{total}")
            print(f"Discount: ₹{discount}")
            print(f"Final Payable: ₹{final_amount}")
            print("✅ Thank You for Shopping with us!")
            break
        else:
            print("❌ Your cart is empty. And items before checkout.")
    elif choice == 5:  #Exit

        print("🥰Thank You! Visit again.")
        break

    else:
        print("❌ Invalid Choice. Please try again.")

