from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("Welcome to the Coffee Shop Ordering System")
    
    # Get customer name
    customer_name = input("Please enter your name: ")
    customer = Customer(customer_name)
    
    while True:
        # Menu to choose an action
        print("\nMenu:")
        print("1. Place an order")
        print("2. View your orders")
        print("3. Check total amount spent")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            coffee_name = input("Enter the name of the coffee you'd like to order: ")
            coffee = Coffee(coffee_name)
            price = float(input(f"Enter the price for {coffee_name}: $"))
            
            # Place an order
            order = Order(customer, coffee, price)
        
        elif choice == '2':
            # View all orders
            customer.view_orders()
        
        elif choice == '3':
            # Check total amount spent
            total = customer.total_spent()
            print(f"\n{customer.name}, you've spent a total of: ${total:.2f}")
        
        elif choice == '4':
            print("Thank you for using the Coffee Shop Ordering System. Goodbye!")
            break
        
        else:
            print("Invalid option, please try again.")

if _name_ == '_main_':
    main()