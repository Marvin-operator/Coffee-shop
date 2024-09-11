class Coffee:
    def _init_(self, name):
        self.name = name
        self.orders = []

    def add_order(self, price):
        """Add a new order to the coffee's list of orders."""
        self.orders.append(price)
    
    def average_price(self):
        """Calculate the average price of this coffee."""
        if not self.orders:
            return 0
        return sum(self.orders) / len(self.orders)

    def total_orders(self):
        """Get the total number of orders for this coffee."""
        return len(self.orders)