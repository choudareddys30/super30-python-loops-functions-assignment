#17 Shopping Cart using Functions

#Create functions for add_item(), remove_item(), view_cart(), calculate_total(), and checkout().
# Keep the application running using a while loop until checkout or exit.

cart = {}


def add_item():
    name = input("Enter item name: ").strip()

    if name == "":
        print("Item name cannot be empty.")
        return

    price = float(input("Enter item price: ₹"))

    if price <= 0:
        print("Price must be greater than zero.")
        return

    cart[name] = price
    print("Item added.")


def remove_item():
    name = input("Enter item name to remove: ").strip()

    if name in cart:
        del cart[name]
        print("Item removed.")
    else:
        print("Item not found.")


def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        for name, price in cart.items():
            print(f"{name}: ₹{price:.2f}")


def calculate_total():
    total = 0

    for price in cart.values():
        total += price

    return total


def checkout():
    view_cart()
    print(f"Total amount: ₹{calculate_total():.2f}")
    print("Thank you for shopping!")


while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        remove_item()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        print(f"Total amount: ₹{calculate_total():.2f}")

    elif choice == "5":
        checkout()
        break

    elif choice == "6":
        print("Application closed.")
        break

    else:
        print("Invalid choice. Please try again.")