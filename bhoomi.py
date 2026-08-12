
import streamlit as st
import json
import os
from datetime import date
from urllib.parse import quote

# =========================================================
# BHOOMI CAFE SETTINGS
# =========================================================

CAFE_NAME = "Bhoomi Cafe"
ADMIN_PASSWORD = "cafe123"
WHATSAPP_NUMBER = "918277695928"

# =========================================================
# FOLDERS
# =========================================================

os.makedirs("images", exist_ok=True)
os.makedirs("birthday_images", exist_ok=True)

# =========================================================
# LOAD DATA
# =========================================================

if os.path.exists("data.json"):
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        data = {}
else:
    data = {}

# =========================================================
# DEFAULT DATA
# =========================================================

if "menu" not in data:
    data["menu"] = []

if "offer" not in data:
    data["offer"] = "Welcome to Bhoomi Cafe!"

if "birthday_packages" not in data:
    data["birthday_packages"] = []

if "bookings" not in data:
    data["bookings"] = []

if "orders" not in data:
    data["orders"] = []

if "contact" not in data:
    data["contact"] = {
        "phone": "9876543210",
        "address": "Bangalore",
        "email": "bhoomicafe@gmail.com"
    }

if "phone" not in data["contact"]:
    data["contact"]["phone"] = "9876543210"

if "address" not in data["contact"]:
    data["contact"]["address"] = "Bangalore"

if "email" not in data["contact"]:
    data["contact"]["email"] = "bhoomicafe@gmail.com"

# =========================================================
# SAVE DATA
# =========================================================

def save_data():
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

# =========================================================
# WHATSAPP
# =========================================================

def create_whatsapp_link(message):
    encoded_message = quote(message, safe="")
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_message}"

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Bhoomi Cafe",
    page_icon="☕",
    layout="centered"
)

# =========================================================
# STYLE
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 25px;
    }

    .welcome-box {
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
        border: 1px solid #dddddd;
    }

    .offer-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
        border: 1px solid #dddddd;
    }

    .info-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #dddddd;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">☕ Bhoomi Cafe</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Fresh Food • Great Taste • Happy Moments ❤️'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

page = st.sidebar.radio(
    "📋 Menu",
    [
        "🏠 Home",
        "🍽️ Menu & Order",
        "🎁 Offers",
        "🎂 Birthday",
        "📞 Contact",
        "⚙️ Admin"
    ]
)

# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="welcome-box">

        <h1>☕ Welcome to Bhoomi Cafe!</h1>

        <p style="font-size:20px;">
        Your place for delicious food,
        refreshing drinks and beautiful celebrations.
        </p>

        <p style="font-size:18px;">
        🍔 Delicious Food &nbsp;&nbsp;
        ☕ Fresh Drinks &nbsp;&nbsp;
        🎂 Birthday Celebrations
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.header("🍽️ Delicious Food")

    st.write(
        "Choose your favourite food from our menu "
        "and place your order online."
    )

    if len(data["menu"]) > 0:
        for item in data["menu"][:3]:
            st.write(
                f"🍽️ **{item['name']}** — ₹{item['price']}"
            )
    else:
        st.info("Our menu will be updated soon!")

    st.divider()

    st.header("🎂 Celebrate Your Birthday")

    st.write(
        "Make your special day memorable at "
        "Bhoomi Cafe with our birthday decoration packages."
    )

    if len(data["birthday_packages"]) > 0:
        for package in data["birthday_packages"][:3]:
            st.write(
                f"🎁 **{package['name']}** — "
                f"₹{package['price']}"
            )
    else:
        st.info("Birthday packages will be available soon!")

    st.divider()

    st.header("🎁 Today's Offer")

    if data["offer"].strip() != "":
        st.markdown(
            f"""
            <div class="offer-box">

            <h3>🎁 Special Offer</h3>

            <p style="font-size:20px;">
            {data["offer"]}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("No special offer available right now.")

    st.divider()

    st.header("❤️ Why Choose Bhoomi Cafe?")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🍽️ Fresh & Tasty Food")
        st.info("☕ Refreshing Drinks")

    with col2:
        st.info("🎂 Birthday Celebrations")
        st.info("❤️ Happy Moments")

    st.divider()

    st.markdown(
        """
        <div class="info-box">

        <h3>📞 Visit Bhoomi Cafe</h3>

        <p>
        Come with your family and friends
        and enjoy a wonderful time!
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# MENU & ORDER
# =========================================================

elif page == "🍽️ Menu & Order":

    st.header("🍽️ Bhoomi Cafe Menu")

    st.write("Choose the items and quantities you want.")

    st.divider()

    cart = []

    if len(data["menu"]) == 0:

        st.warning("No menu items available yet.")

    else:

        for i, item in enumerate(data["menu"]):

            st.subheader(
                f"{item['name']} - ₹{item['price']}"
            )

            image_base = (
                item["name"]
                .lower()
                .replace(" ", "_")
            )

            possible_images = [
                f"{image_base}.jpg",
                f"{image_base}.jpeg",
                f"{image_base}.png"
            ]

            image_found = None

            for image_file in possible_images:

                path = os.path.join(
                    "images",
                    image_file
                )

                if os.path.exists(path):
                    image_found = path
                    break

            if image_found:
                st.image(
                    image_found,
                    width=250
                )

            quantity = st.number_input(
                f"Quantity of {item['name']}",
                min_value=0,
                max_value=20,
                value=0,
                step=1,
                key=f"quantity_{i}"
            )

            if quantity > 0:

                item_total = (
                    item["price"] * quantity
                )

                cart.append(
                    {
                        "name": item["name"],
                        "price": item["price"],
                        "quantity": quantity,
                        "total": item_total
                    }
                )

            st.divider()

    # =====================================================
    # CART
    # =====================================================

    st.header("🛒 Your Cart")

    if len(cart) == 0:

        st.info("Your cart is empty.")

    else:

        grand_total = 0

        for item in cart:

            st.write(
                f"🍽️ {item['name']} × "
                f"{item['quantity']} = "
                f"₹{item['total']}"
            )

            grand_total += item["total"]

        st.divider()

        st.subheader(
            f"💰 Total Amount: ₹{grand_total}"
        )

        st.header("📋 Order Details")

        customer_name = st.text_input(
            "👤 Your Name"
        )

        customer_phone = st.text_input(
            "📱 Your Phone Number (Optional)"
        )

        order_type = st.selectbox(
            "🍽️ Order Type",
            [
                "Dine In",
                "Take Away",
                "Delivery"
            ]
        )

        table_number = ""
        address = ""

        if order_type == "Dine In":

            table_number = st.text_input(
                "🪑 Table Number"
            )

        elif order_type == "Delivery":

            address = st.text_area(
                "🏠 Delivery Address"
            )

        special_note = st.text_area(
            "📝 Special Instructions (Optional)"
        )

        if st.button("🛒 Place Order"):

            if len(cart) == 0:

                st.error(
                    "Please select at least one item."
                )

            elif customer_name.strip() == "":

                st.error(
                    "Please enter your name."
                )

            elif (
                order_type == "Dine In"
                and table_number.strip() == ""
            ):

                st.error(
                    "Please enter your table number."
                )

            elif (
                order_type == "Delivery"
                and address.strip() == ""
            ):

                st.error(
                    "Please enter your delivery address."
                )

            else:

                order = {
                    "customer_name": customer_name,
                    "phone": customer_phone,
                    "order_type": order_type,
                    "table": table_number,
                    "address": address,
                    "items": cart,
                    "total": grand_total,
                    "special_note": special_note,
                    "status": "Pending"
                }

                data["orders"].append(order)

                save_data()

                message = (
                    "🛒 *NEW BHOOMI CAFE ORDER*\n\n"
                    "☕ Cafe: Bhoomi Cafe\n"
                    f"👤 Customer: {customer_name}\n"
                )

                if customer_phone.strip() != "":
                    message += (
                        f"📱 Phone: {customer_phone}\n"
                    )

                message += (
                    f"🍽️ Order Type: {order_type}\n"
                )

                if order_type == "Dine In":

                    message += (
                        f"🪑 Table: {table_number}\n"
                    )

                if order_type == "Delivery":

                    message += (
                        f"🏠 Address: {address}\n"
                    )

                message += (
                    "\n🍽️ *ORDER ITEMS*\n"
                )

                for item in cart:

                    message += (
                        f"• {item['name']} × "
                        f"{item['quantity']} = "
                        f"₹{item['total']}\n"
                    )

                message += (
                    f"\n💰 *TOTAL: ₹{grand_total}*"
                )

                if special_note.strip() != "":
                    message += (
                        f"\n📝 Note: {special_note}"
                    )

                link = create_whatsapp_link(message)

                st.success(
                    "🎉 Your order has been placed!"
                )

                st.markdown(
                    f"""
                    <a href="{link}" target="_blank">

                    <button style="
                        background-color:#25D366;
                        color:white;
                        padding:12px 20px;
                        border:none;
                        border-radius:8px;
                        font-size:16px;
                        cursor:pointer;
                    ">

                    📱 Send Order on WhatsApp

                    </button>

                    </a>
                    """,
                    unsafe_allow_html=True
                )

# =========================================================
# OFFERS
# =========================================================

elif page == "🎁 Offers":

    st.header("🎁 Bhoomi Cafe Offers")

    if data["offer"].strip() == "":
        st.info("No offers available right now.")
    else:
        st.success(data["offer"])

# =========================================================
# BIRTHDAY
# =========================================================

elif page == "🎂 Birthday":

    st.header(
        "🎂 Birthday Celebration at Bhoomi Cafe"
    )

    st.write(
        "Choose a birthday decoration package "
        "and celebrate your special day!"
    )

    st.divider()

    if len(data["birthday_packages"]) == 0:

        st.warning(
            "No birthday packages available yet."
        )

    else:

        for package in data["birthday_packages"]:

            st.subheader(
                f"🎉 {package['name']}"
            )

            st.write(
                f"💰 Price: ₹{package['price']}"
            )

            st.write(
                f"📝 {package['description']}"
            )

            image_base = (
                package["name"]
                .lower()
                .replace(" ", "_")
            )

            possible_images = [
                f"{image_base}.jpg",
                f"{image_base}.jpeg",
                f"{image_base}.png"
            ]

            image_found = None

            for image_file in possible_images:

                path = os.path.join(
                    "birthday_images",
                    image_file
                )

                if os.path.exists(path):

                    image_found = path
                    break

            if image_found:

                st.image(
                    image_found,
                    width=300
                )

            st.divider()

    # =====================================================
    # BOOKING
    # =====================================================

    st.header("📅 Book Your Birthday")

    package_names = [
        package["name"]
        for package in data["birthday_packages"]
    ]

    if len(package_names) > 0:

        selected_package = st.selectbox(
            "🎁 Select Package",
            package_names
        )

        customer_name = st.text_input(
            "👤 Your Name",
            key="birthday_name"
        )

        phone = st.text_input(
            "📱 Your Phone Number",
            key="birthday_phone"
        )

        booking_date = st.date_input(
            "📅 Birthday Date",
            min_value=date.today()
        )

        guests = st.number_input(
            "👥 Number of Guests",
            min_value=1,
            value=10
        )

        requirements = st.text_area(
            "📝 Special Requirements"
        )

        if st.button("🎂 Book Birthday"):

            if customer_name.strip() == "":

                st.error(
                    "Please enter your name."
                )

            elif phone.strip() == "":

                st.error(
                    "Please enter your phone number."
                )

            else:

                selected_package_data = None

                for package in data["birthday_packages"]:

                    if package["name"] == selected_package:

                        selected_package_data = package
                        break

                booking = {
                    "customer_name": customer_name,
                    "phone": phone,
                    "date": str(booking_date),
                    "package": selected_package,
                    "price": selected_package_data["price"],
                    "guests": guests,
                    "requirements": requirements,
                    "status": "Pending"
                }

                data["bookings"].append(booking)

                save_data()

                message = (
                    "🎂 *NEW BHOOMI CAFE "
                    "BIRTHDAY BOOKING*\n\n"
                    "☕ Cafe: Bhoomi Cafe\n"
                    f"👤 Customer: {customer_name}\n"
                    f"📱 Phone: {phone}\n"
                    f"📅 Date: {booking_date}\n"
                    f"🎁 Package: {selected_package}\n"
                    f"💰 Price: "
                    f"₹{selected_package_data['price']}\n"
                    f"👥 Guests: {guests}\n"
                )

                if requirements.strip() != "":
                    message += (
                        f"📝 Requirements: "
                        f"{requirements}\n"
                    )

                link = create_whatsapp_link(message)

                st.success(
                    "🎉 Your birthday booking has been received!"
                )

                st.markdown(
                    f"""
                    <a href="{link}" target="_blank">

                    <button style="
                        background-color:#25D366;
                        color:white;
                        padding:12px 20px;
                        border:none;
                        border-radius:8px;
                        font-size:16px;
                        cursor:pointer;
                    ">

                    📱 Send Booking on WhatsApp

                    </button>

                    </a>
                    """,
                    unsafe_allow_html=True
                )

# =========================================================
# CONTACT
# =========================================================

elif page == "📞 Contact":

    st.header("📞 Contact Bhoomi Cafe")

    st.write(
        f"📱 **Phone:** {data['contact']['phone']}"
    )

    st.write(
        f"📍 **Address:** {data['contact']['address']}"
    )

    st.write(
        f"📧 **Email:** {data['contact']['email']}"
    )

    st.divider()

    st.info(
        "❤️ We look forward to serving you!"
    )

# =========================================================
# ADMIN
# =========================================================

elif page == "⚙️ Admin":

    st.header(
        "🔐 Bhoomi Cafe Admin Panel"
    )

    password = st.text_input(
        "Enter Admin Password",
        type="password"
    )

    if password == ADMIN_PASSWORD:

        st.success(
            "✅ Admin login successful!"
        )

        st.divider()

        # =================================================
        # CONTACT DETAILS
        # =================================================

        st.subheader(
            "📞 Manage Contact Details"
        )

        st.write(
            "You can change these details anytime."
        )

        new_contact_phone = st.text_input(
            "📱 Phone Number",
            value=data["contact"]["phone"],
            key="contact_phone"
        )

        new_contact_address = st.text_area(
            "📍 Address",
            value=data["contact"]["address"],
            key="contact_address"
        )

        new_contact_email = st.text_input(
            "📧 Email",
            value=data["contact"]["email"],
            key="contact_email"
        )

        if st.button("💾 Save Contact Details"):

            data["contact"]["phone"] = new_contact_phone
            data["contact"]["address"] = new_contact_address
            data["contact"]["email"] = new_contact_email

            save_data()

            st.success(
                "✅ Contact details updated successfully!"
            )

            st.rerun()

        st.divider()

        # =================================================
        # MENU MANAGEMENT
        # =================================================

        st.subheader(
            "🍽️ Manage Menu"
        )

        for i, item in enumerate(data["menu"]):

            st.write(
                f"### Menu Item {i + 1}"
            )

            new_name = st.text_input(
                "Item Name",
                value=item["name"],
                key=f"admin_name_{i}"
            )

            new_price = st.number_input(
                "Price ₹",
                value=item["price"],
                min_value=0,
                key=f"admin_price_{i}"
            )

            uploaded_image = st.file_uploader(
                "Upload / Change Image",
                type=["jpg", "jpeg", "png"],
                key=f"admin_image_{i}"
            )

            if st.button(
                f"💾 Save Item {i + 1}",
                key=f"admin_save_{i}"
            ):

                data["menu"][i]["name"] = new_name
                data["menu"][i]["price"] = new_price

                if uploaded_image is not None:

                    image_path = os.path.join(
                        "images",
                        new_name.lower()
                        .replace(" ", "_")
                        + ".jpg"
                    )

                    with open(
                        image_path,
                        "wb"
                    ) as image_file:

                        image_file.write(
                            uploaded_image.getbuffer()
                        )

                save_data()

                st.success(
                    "✅ Menu item updated!"
                )

                st.rerun()

            if st.button(
                f"🗑️ Delete Item {i + 1}",
                key=f"admin_delete_{i}"
            ):

                data["menu"].pop(i)

                save_data()

                st.success(
                    "🗑️ Menu item deleted!"
                )

                st.rerun()

            st.divider()

        # =================================================
        # ADD MENU
        # =================================================

        st.subheader(
            "➕ Add New Menu Item"
        )

        add_name = st.text_input(
            "New Item Name"
        )

        add_price = st.number_input(
            "New Item Price ₹",
            min_value=0,
            value=0
        )

        add_image = st.file_uploader(
            "New Item Image",
            type=["jpg", "jpeg", "png"],
            key="add_menu_image"
        )

        if st.button("➕ Add Menu Item"):

            if add_name.strip() == "":

                st.error(
                    "Please enter item name."
                )

            else:

                data["menu"].append(
                    {
                        "name": add_name,
                        "price": add_price
                    }
                )

                if add_image is not None:

                    image_path = os.path.join(
                        "images",
                        add_name.lower()
                        .replace(" ", "_")
                        + ".jpg"
                    )

                    with open(
                        image_path,
                        "wb"
                    ) as image_file:

                        image_file.write(
                            add_image.getbuffer()
                        )

                save_data()

                st.success(
                    "🎉 Menu item added!"
                )

                st.rerun()

        st.divider()

        # =================================================
        # OFFERS
        # =================================================

        st.subheader(
            "🎁 Manage Offers"
        )

        new_offer = st.text_area(
            "Offer Details",
            value=data["offer"]
        )

        if st.button("💾 Save Offer"):

            data["offer"] = new_offer

            save_data()

            st.success(
                "✅ Offer updated!"
            )

            st.rerun()

        st.divider()

        # =================================================
        # BIRTHDAY PACKAGES
        # =================================================

        st.subheader(
            "🎂 Manage Birthday Packages"
        )

        for i, package in enumerate(
            data["birthday_packages"]
        ):

            st.write(
                f"### Birthday Package {i + 1}"
            )

            package_name = st.text_input(
                "Package Name",
                value=package["name"],
                key=f"package_name_{i}"
            )

            package_price = st.number_input(
                "Package Price ₹",
                value=package["price"],
                min_value=0,
                key=f"package_price_{i}"
            )

            package_description = st.text_area(
                "Package Description",
                value=package["description"],
                key=f"package_description_{i}"
            )

            package_image = st.file_uploader(
                "Upload / Change Package Image",
                type=["jpg", "jpeg", "png"],
                key=f"package_image_{i}"
            )

            if st.button(
                f"💾 Save Package {i + 1}",
                key=f"package_save_{i}"
            ):

                data["birthday_packages"][i]["name"] = (
                    package_name
                )

                data["birthday_packages"][i]["price"] = (
                    package_price
                )

                data["birthday_packages"][i]["description"] = (
                    package_description
                )

                if package_image is not None:

                    image_path = os.path.join(
                        "birthday_images",
                        package_name.lower()
                        .replace(" ", "_")
                        + ".jpg"
                    )

                    with open(
                        image_path,
                        "wb"
                    ) as image_file:

                        image_file.write(
                            package_image.getbuffer()
                        )

                save_data()

                st.success(
                    "✅ Birthday package updated!"
                )

                st.rerun()

            if st.button(
                f"🗑️ Delete Package {i + 1}",
                key=f"package_delete_{i}"
            ):

                data["birthday_packages"].pop(i)

                save_data()

                st.success(
                    "🗑️ Birthday package deleted!"
                )

                st.rerun()

            st.divider()

        # =================================================
        # ADD BIRTHDAY PACKAGE
        # =================================================

        st.subheader(
            "➕ Add Birthday Package"
        )

        new_package_name = st.text_input(
            "New Package Name"
        )

        new_package_price = st.number_input(
            "New Package Price ₹",
            min_value=0,
            value=0
        )

        new_package_description = st.text_area(
            "New Package Description"
        )

        new_package_image = st.file_uploader(
            "New Package Image",
            type=["jpg", "jpeg", "png"],
            key="new_package_image"
        )

        if st.button(
            "➕ Add Birthday Package"
        ):

            if new_package_name.strip() == "":

                st.error(
                    "Please enter package name."
                )

            else:

                data["birthday_packages"].append(
                    {
                        "name": new_package_name,
                        "price": new_package_price,
                        "description":
                            new_package_description
                    }
                )

                if new_package_image is not None:

                    image_path = os.path.join(
                        "birthday_images",
                        new_package_name.lower()
                        .replace(" ", "_")
                        + ".jpg"
                    )

                    with open(
                        image_path,
                        "wb"
                    ) as image_file:

                        image_file.write(
                            new_package_image.getbuffer()
                        )

                save_data()

                st.success(
                    "🎉 Birthday package added!"
                )

                st.rerun()

        st.divider()

        # =================================================
        # BIRTHDAY BOOKINGS
        # =================================================

        st.subheader(
            "🎂 Birthday Bookings"
        )

        if len(data["bookings"]) == 0:

            st.info(
                "No birthday bookings yet."
            )

        else:

            for i, booking in enumerate(
                data["bookings"]
            ):

                st.write(
                    f"### Booking {i + 1}"
                )

                st.write(
                    f"👤 Customer: "
                    f"{booking['customer_name']}"
                )

                st.write(
                    f"📱 Phone: "
                    f"{booking['phone']}"
                )

                st.write(
                    f"📅 Date: "
                    f"{booking['date']}"
                )

                st.write(
                    f"🎁 Package: "
                    f"{booking['package']}"
                )

                st.write(
                    f"💰 Price: "
                    f"₹{booking['price']}"
                )

                st.write(
                    f"👥 Guests: "
                    f"{booking['guests']}"
                )

                st.write(
                    f"📝 Requirements: "
                    f"{booking['requirements']}"
                )

                st.write(
                    f"📌 Status: "
                    f"{booking['status']}"
                )

                st.divider()

        # =================================================
        # FOOD ORDERS
        # =================================================

        st.subheader(
            "🛒 Food Orders"
        )

        if len(data["orders"]) == 0:

            st.info(
                "No food orders yet."
            )

        else:

            for i, order in enumerate(
                data["orders"]
            ):

                st.write(
                    f"### Order {i + 1}"
                )

                st.write(
                    f"👤 Customer: "
                    f"{order['customer_name']}"
                )

                if order["phone"].strip() != "":

                    st.write(
                        f"📱 Phone: "
                        f"{order['phone']}"
                    )

                else:

                    st.write(
                        "📱 Phone: Not provided"
                    )

                st.write(
                    f"🍽️ Order Type: "
                    f"{order['order_type']}"
                )

                if order["order_type"] == "Dine In":

                    st.write(
                        f"🪑 Table: "
                        f"{order['table']}"
                    )

                if order["order_type"] == "Delivery":

                    st.write(
                        f"🏠 Address: "
                        f"{order['address']}"
                    )

                st.write("🍽️ Items:")

                for item in order["items"]:

                    st.write(
                        f"• {item['name']} × "
                        f"{item['quantity']} = "
                        f"₹{item['total']}"
                    )

                st.write(
                    f"💰 Total: ₹{order['total']}"
                )

                if order["special_note"].strip() != "":

                    st.write(
                        f"📝 Note: "
                        f"{order['special_note']}"
                    )

                st.write(
                    f"📌 Status: "
                    f"{order['status']}"
                )

                st.divider()

    elif password != "":

        st.error(
            "❌ Incorrect password."
        )
