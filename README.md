Overview
--------

This is a Python-based application simulating a coffee shop where customers place orders for different types of coffee. The app models the relationships between *Customers, **Coffee, and **Orders* using object-oriented programming (OOP).

This project helps demonstrate OOP concepts such as:
----------------------------------------------------

*   Classes and Instances
*   Class Methods
*   Object Relationships
*   Aggregation and Association Methods

Purpose
-------

The goal of this project is to deepen understanding of object-oriented principles through the development of a simple coffee shop domain model, focusing on how objects relate to one another.

•⁠  ⁠* *

Folder Structure
----------------


coffee_shop/
│
├── models/
│   ├── customer.py       # Customer class implementation
│   ├── coffee.py         # Coffee class implementation
│   ├── order.py          # Order class implementation
│   └── utils.py          # Helper utilities
│
├── tests/
│   ├── test_customer.py  # Tests for Customer class
│   ├── test_coffee.py    # Tests for Coffee class
│   └── test_order.py     # Tests for Order class
│
└── README.md             # Project documentation


•⁠  ⁠* *

Features
--------

1.  *Customer Management*: Create customers and associate them with their orders.
2.  *Coffee Options*: Different coffee types available for orders.
3.  *Order System*: Customers can place orders for coffee with different prices.
4.  *Statistics*: Track the number of orders for each coffee, average price, and customers who ordered a specific coffee.

•⁠  ⁠* *

Setup Instructions
------------------

### 1\. Clone the Repository

⁠ bash
git clone <repository url>
cd <file>
 ⁠

### 2\. Create and Activate a Virtual Environment

For *macOS/Linux*:

⁠ bash
python3 -m venv env
source env/bin/activate
 ⁠

For *Windows*:

⁠ bash
python -m venv env
.\env\Scripts\activate
 ⁠

### 3\. Install Dependencies

If there are any dependencies listed in ⁠ requirements.txt ⁠, install them:

⁠ bash
pip install -r requirements.txt
 ⁠

### 4\. Run the Application

You can run the app by navigating to the directory where your main files are located. Here’s a basic prompt flow in the terminal:

⁠ bash
python3 -i models/customer.py
 ⁠

### 5\. Run Tests

To make sure your application works properly, run the tests in the ⁠ tests/ ⁠ directory:

⁠ bash
python3 tests/test_customer.py
python3 tests/test_coffee.py
python3 tests/test_order.py
 ⁠

•⁠  ⁠* *

How It Works (With Input Prompts)
---------------------------------

In the main application, you will be prompted to create customers, coffees, and place orders. Here’s how each prompt works:

1.  *Creating a Customer:*
    
    ⁠ python
    
    from customer import Customer
    name = input("Enter the customer name: ")
    customer = Customer(name)
     ⁠
    
2.  *Creating Coffee:*
    
    ⁠ python
    
    from coffee import Coffee
    coffee_name = input("Enter coffee type (e.g., Espresso, Latte): ")
    coffee = Coffee(coffee_name)
     ⁠
    
3.  *Placing an Order:*
    
    ⁠ python
    
    from order import Order
    price = float(input(f"Enter the price of the {coffee.name}: "))
    order = Order(customer, coffee, price)
     ⁠
    
4.  *View Orders for a Customer:*
    
    ⁠ python
    customer_orders = customer.orders()
    print(f"{customer.name}'s Orders: {customer_orders}")
     ⁠
    

•⁠  ⁠* *

How to Use
----------

1.  *Create Customers*: You can create multiple customers by following the prompts.
2.  *Create Coffee Options*: Add as many coffee types as needed.
3.  *Place Orders*: For each customer, you can create multiple orders for different coffee types and prices.
4.  *Track Orders and Statistics*: Use the built-in methods to see which coffees have been ordered, how many times a coffee was ordered, and which customer spent the most on a particular coffee.

•⁠  ⁠* *
