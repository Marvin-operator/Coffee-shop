class Order:
    def _init_(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.record_order()

    def record_order(self):
        """Record the order for both the customer and the coffee."""
        self.customer.place_order(self.coffee, self.price)
        self.coffee.add_order(self.price)
        print(f"Order recorded: {self.customer.name} ordered {self.coffee.name} at ${self.price:.2f}")