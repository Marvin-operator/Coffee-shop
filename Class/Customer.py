class Customer:
    def _init_(self, name):
        self.name = name
        self.orders = []

    def place_order(self, coffee, price):
        """Method to place an order for a specific coffee and price."""
        self.orders.append((coffee, price))
        print(f"{self.name} has placed an order for {coffee.name} at ${price:.2f}")

    def view_orders(self):
        """View all the orders placed by the customer."""
        if not self.orders:
            print(f"{self.name} has not placed any orders yet.")
        else:
            print(f"Orders placed by {self.name}:")
            for i, (coffee, price) in enumerate(self.orders, 1):
                print(f"{i}. {coffee.name} - ${price:.2f}")

    def total_spent(self):
        """Calculate the total amount spent by the customer."""
        return sum(price for _, price in self.orders)