from datetime import datetime, timedelta
import random

class Product:
    def __init__(self, name, price, stock, duration_minutes):
        self.name = name
        self.price = price
        self.stock = stock
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=duration_minutes)

    def is_active(self, current_time):
        return self.start_time <= current_time <= self.end_time

    def buy(self, qty):
        if self.stock >= qty:
            self.stock -= qty
            return True
        return False


class User:
    def __init__(self, name):
        self.name = name
        self.balance = random.randint(50, 500)

        # datang random dalam 0-10 menit
        self.arrival_time = datetime.now() + timedelta(
            minutes=random.randint(0, 10)
        )

    def wants_to_buy(self):
        return random.choice([True, False])


class FlashSaleSystem:
    def __init__(self):
        self.products = []
        self.users = []
        self.transactions = []

    def add_product(self, product):
        self.products.append(product)

    def add_user(self, user):
        self.users.append(user)

    def run(self):
        print("\n=== SIMULASI FLASH SALE ===\n")

        # urutkan user berdasarkan waktu datang
        self.users.sort(key=lambda u: u.arrival_time)

        for user in self.users:
            current_time = user.arrival_time
            print(f"{user.name} datang jam {current_time.strftime('%H:%M:%S')}")

            for product in self.products:
                if product.is_active(current_time) and product.stock > 0:
                    if user.wants_to_buy():
                        qty = random.randint(1, 3)
                        total_price = qty * product.price

                        if user.balance >= total_price:
                            success = product.buy(qty)

                            if success:
                                self.transactions.append((user.name, product.name, qty))
                                print(f"  -> Beli {qty} {product.name}")
                        else:
                            print("  -> Uang tidak cukup")

        print("\n=== HASIL ===")
        for p in self.products:
            print(f"{p.name} sisa stok: {p.stock}")