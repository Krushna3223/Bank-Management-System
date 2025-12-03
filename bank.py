import json
from pathlib import Path
import random
import string


class Bank:
    database = "data.json"
    data = []

    # Load database on start
    try:
        if Path(database).exists():
            with open(database, "r") as f:
                data = json.load(f)
        else:
            data = []
    except:
        data = []

    @classmethod
    def update(cls):
        """Save data to JSON."""
        with open(cls.database, "w") as f:
            json.dump(cls.data, f, indent=2)

    @classmethod
    def generate_acc(cls):
        """Generate unique account number."""
        letters = random.choices(string.ascii_letters, k=3)
        digits = random.choices(string.digits, k=3)
        symbol = random.choice("!@#$%^")
        acc = letters + digits + [symbol]
        random.shuffle(acc)
        return "".join(acc)

    @classmethod
    def get_user(cls, acc, pin):
        """Return user list matching acc & pin."""
        return [u for u in cls.data if u["accNO"] == acc and u["pin"] == pin]

    @classmethod
    def create_account(cls, name, age, email, pin):
        """Create new bank account."""
        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accNO": cls.generate_acc(),
            "balance": 0
        }
        cls.data.append(user)
        cls.update()
        return user

    @classmethod
    def deposit(cls, acc, pin, amount):
        user = cls.get_user(acc, pin)
        if not user:
            return None
        user[0]["balance"] += amount
        cls.update()
        return user[0]["balance"]

    @classmethod
    def withdraw(cls, acc, pin, amount):
        user = cls.get_user(acc, pin)
        if not user:
            return None
        if amount > user[0]["balance"]:
            return False
        user[0]["balance"] -= amount
        cls.update()
        return user[0]["balance"]

    @classmethod
    def update_details(cls, acc, pin, name=None, email=None, new_pin=None):
        user = cls.get_user(acc, pin)
        if not user:
            return False

        u = user[0]
        if name:
            u["name"] = name
        if email:
            u["email"] = email
        if new_pin:
            u["pin"] = new_pin

        cls.update()
        return True

    @classmethod
    def delete_account(cls, acc, pin):
        user = cls.get_user(acc, pin)
        if not user:
            return False

        cls.data.remove(user[0])
        cls.update()
        return True
