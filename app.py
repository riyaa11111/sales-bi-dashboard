import streamlit as st

# 1. Page Configuration & Title
st.set_page_config(page_title="Python SuperMart", page_icon="🛒", layout="centered")
st.title("🛒 Python SuperMart")
st.write("Welcome to the smart grocery checkout application.")

# 2. Predefined product list
products = {
    "apple": 50,
    "banana": 20,
    "milk": 40,
    "bread": 30,
    "egg": 10,
}

# 3. Initialize the shopping cart using Streamlit's session state
# (This keeps the cart data alive while the web page reloads!)
if "cart" not in st.session_state:
    st.session_state.cart = {}

# 4. Sidebar Menu Navigation (Replaces your 'while True' loop)
menu = ["View Products", "Add to Cart", "View Cart & Checkout"]
choice = st.sidebar.selectbox("Navigation Menu", menu)

# --- FEATURE 1: VIEW PRODUCTS ---
if choice == "View Products":
    st.header("📋 Available Products")
    # Display products nicely in a table
    st.table({"Product": [k.title() for k in products.keys()], "Price (₹)": list(products.values())})

# --- FEATURE 2: ADD TO CART ---
elif choice == "Add to Cart":
    st.header("➕ Add Items to Cart")

    # Dropdown to select product and a number selector for quantity
    selected_item = st.selectbox("Select an item:", list(products.keys()))
    qty = st.number_input(f"Quantity of {selected_item}:", min_value=1, value=1, step=1)

    if st.button("Add to Cart"):
        st.session_state.cart[selected_item] = st.session_state.cart.get(selected_item, 0) + qty
        st.success(f"✓ Added {qty} {selected_item}(s) to your cart!")

# --- FEATURE 3: VIEW CART & CHECKOUT ---
elif choice == "View Cart & Checkout":
    st.header("🛒 Your Shopping Cart")

    cart = st.session_state.cart

    if not cart:
        st.info("Your cart is empty. Go back to 'Add to Cart' to add items!")
    else:
        # Display items currently in cart
        total = 0
        for item, qty in cart.items():
            price = products[item] * qty
            total += price
            st.write(f"• **{item.title()}** (x{qty}) = ₹{price}")

        st.divider()
        st.subheader(f"Subtotal: ₹{total}")

        # Apply discount logic
        if total >= 500:
            discount = total * 0.10
            discount_text = "10% Off"
        elif total >= 200:
            discount = total * 0.05
            discount_text = "5% Off"
        else:
            discount = 0
            discount_text = "0%"

        final_amount = total - discount

        st.write(f"Discount Applied ({discount_text}): -₹{discount}")
        st.markdown(f"### **Final Payable: ₹{final_amount}**")

        # Place Order Button
        if st.button("✅ Confirm & Place Order"):
            st.balloons()  # Fun visual effect!
            st.success("Thank you for shopping with Python SuperMart!")
            st.session_state.cart = {}  # Clear cart after checkout