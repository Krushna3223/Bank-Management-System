import streamlit as st
from bank.bank import Bank

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Bank System",
    page_icon="🏦",
    layout="centered"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>

body {
    background-color: #0e0e0e;
}

.card {
    background: #1a1a1a;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px #000;
    margin-bottom: 20px;
}

.gradient-btn {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    padding: 12px;
    color: white;
    text-align: center;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
}

.gradient-btn:hover {
    background: linear-gradient(90deg, #dd2476, #ff512f);
}

.sidebar-profile {
    background: #1e1e1e;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

.sidebar-profile img {
    width: 70px;
    border-radius: 50%;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR PROFILE
# -------------------------
st.sidebar.markdown("""
<div class='sidebar-profile'>
    <img src='https://i.imgur.com/8Km9tLL.png'>
    <h3 style='color:white;'>User</h3>
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Menu",
    ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Details", "Delete Account"]
)


# -------------------------
# REUSABLE CARD FUNCTION
# -------------------------
def card(title):
    st.markdown(f"<div class='card'><h2 style='color:white;'>{title}</h2>", unsafe_allow_html=True)


def end_card():
    st.markdown("</div>", unsafe_allow_html=True)


# -------------------------
# UI SCREENS
# -------------------------

# CREATE ACCOUNT
if menu == "Create Account":
    card("🆕 Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120)
    email = st.text_input("Email")
    pin = st.text_input("PIN (4 digits)", type="password")

    if st.button("Create Account"):
        if len(pin) != 4 or not pin.isdigit():
            st.error("PIN must be 4 digits!")
        elif age < 18:
            st.error("Minimum age is 18!")
        else:
            user = Bank.create_account(name, age, email, int(pin))
            st.success("🎉 Account Created!")
            st.info(f"Your Account Number: **{user['accNO']}**")

    end_card()


# DEPOSIT
elif menu == "Deposit":
    card("💰 Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit Money"):
        bal = Bank.deposit(acc, int(pin), amount)
        if bal is None:
            st.error("Invalid Account or PIN!")
        else:
            st.success(f"Deposit Successful! New Balance: ₹{bal}")

    end_card()


# WITHDRAW
elif menu == "Withdraw":
    card("🏧 Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw Money"):
        bal = Bank.withdraw(acc, int(pin), amount)
        if bal is None:
            st.error("Invalid Account or PIN!")
        elif bal is False:
            st.error("Insufficient Balance!")
        else:
            st.success(f"Withdrawal Successful! New Balance: ₹{bal}")

    end_card()


# SHOW DETAILS
elif menu == "Show Details":
    card("📄 Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details"):
        user = Bank.get_user(acc, int(pin))
        if not user:
            st.error("Invalid Account or PIN!")
        else:
            st.json(user[0])

    end_card()


# UPDATE DETAILS
elif menu == "Update Details":
    card("⚙️ Update Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    new_pin = st.text_input("New PIN (4 digits)", type="password")

    if st.button("Update"):
        status = Bank.update_details(
            acc, int(pin),
            name=new_name if new_name else None,
            email=new_email if new_email else None,
            new_pin=int(new_pin) if new_pin else None
        )
        if status:
            st.success("Account Updated!")
        else:
            st.error("Invalid Account or PIN!")

    end_card()


# DELETE ACCOUNT
elif menu == "Delete Account":
    card("🗑 Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):
        status = Bank.delete_account(acc, int(pin))
        if status:
            st.success("Account Deleted Successfully!")
        else:
            st.error("Invalid Account or PIN!")

    end_card()
