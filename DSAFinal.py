import json
from tabulate import tabulate
import pwinput
import os
import csv


class Node:  # Node class
    def __init__(self, model, brand, price, quantity):  # Constructor
        self.model = model
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.next = None


class LinkedList:  # Linked List class
    def __init__(self):
        self.head = None

    def InsertAtBeg(self, model, brand, price, quantity):  # Insert at beginning
        newnode = Node(model, brand, price, quantity)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def InsertAtEnd(self, model, brand, price, quantity):  # Insert at end
        end = Node(model, brand, price, quantity)
        if self.head == None:
            self.head = end
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = end

    def DeleteAtPos(self, pos):  # Delete at position
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            if pos == 1:
                self.head = temp.next
                temp = None
                return
            for i in range(pos - 2):
                temp = temp.next
                if temp == None:
                    break
            if temp == None:
                print("Index out of range")
            elif temp.next == None:
                print("Index out of range")
            else:
                next = temp.next.next
                temp.next = None
                temp.next = next

    def InsertAtPos(self, pos, model, brand, price):  # Insert at position
        newnode = Node(model, brand, price, 10)
        if pos == 1:
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            for i in range(pos - 2):
                temp = temp.next
                if temp == None:
                    break
            if temp == None:
                print("Index out of range")
            else:
                newnode.next = temp.next
                temp.next = newnode

    def display(self):  # we dont display quantity
        temp = self.head
        dict = {}
        brand = []
        model = []
        price = []
        i = 1
        index = []
        while temp != None:
            model.append(temp.model)
            brand.append(temp.brand)
            price.append(temp.price)
            index.append(i)
            temp = temp.next
            dict = {
                "Position": index,
                "Model": model,
                "Brand": brand,
                "Price": price,
            }  # Display as a table
            i = i + 1
        print(
            tabulate(
                dict,
                headers="keys",
                tablefmt="fancy_grid",
            )
        )

    def search_by_brand(self):  # Search by brand
        brand = input("Enter the brand: ")
        temp = self.head
        matching_products = []
        while temp is not None:  # Traverse the list
            if temp.brand == brand:  # If brand matches
                matching_products.append(
                    {
                        "Model": temp.model,
                        "Brand": temp.brand,
                        "Price": temp.price,
                    }  # Append to matching products
                )
            temp = temp.next

        if not matching_products:  # If no matching products
            print("No products found for the given brand.")
            matching_product = self.search_by_brand()
            return matching_product
        else:
            dict = {
                "Model": [p["Model"] for p in matching_products],
                "Price": [p["Price"] for p in matching_products],
            }
            print(tabulate(dict, headers=["Model", "Price"], tablefmt="fancy_grid"))
            return matching_products, brand  # Return matching products and brand

    def search_by_model(self):
        model = input("Enter the model: ")
        temp = self.head
        product_brand = ""  # Brand of the product
        matching_products = []
        while temp is not None:
            if temp.model == model:
                matching_products.append(
                    {
                        "Model": temp.model,
                        "Brand": temp.brand,
                        "Price": temp.price,
                    }  # Append to matching products
                )
            temp = temp.next

        if not matching_products:  # If no matching products
            print("No products found for the given model.")
            matching_product = self.search_by_model()
            return matching_product
        else:
            dict = {
                "Brand": [p["Brand"] for p in matching_products],
                "Price": [p["Price"] for p in matching_products],
            }
            print(tabulate(dict, headers=["Brand", "Price"], tablefmt="fancy_grid"))
            return (
                matching_products,
                product_brand,
            )  # Return matching products and brand

    def search(self):
        print("1. Search by brand")  # Search by brand or model
        print("2. Search by model")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            matching_product, pbrand = self.search_by_brand()
        elif choice == 2:
            matching_product, pbrand = self.search_by_model()
        else:
            print("Invalid choice")
        return matching_product, pbrand

    def UpdatePrice(self):
        model = input("Enter the model: ")  # Update price
        temp = self.head
        while temp != None:
            if temp.model == model:  # If model matches
                temp.price = input("Enter the new price: ")
                print("Price updated successfully")
            temp = temp.next

    def FilterByPrice(self, brand):  # Filter by price
        price = int(input("Enter the price: "))  # Price to filter
        temp = self.head
        matching_products = []  # Matching products
        while temp is not None:
            if (
                temp.brand == brand and temp.price <= price
            ):  # If brand matches and price is less than the threshold
                matching_products.append(
                    {"Model": temp.model, "Brand": temp.brand, "Price": temp.price}
                )
            temp = temp.next
        print(tabulate(matching_products, headers="keys", tablefmt="fancy_grid"))
        return matching_products  # Return matching products

    def concatenate(self, list2):  # Concatenate two linked lists
        if self.head == None:
            self.head = list2.head
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = list2.head

    def get_product_by_position(self, position):  # Get product by position
        temp = self.head
        current_position = 1  # Current position
        while (
            temp is not None and current_position < position
        ):  # traverse all the matching products
            temp = temp.next  # Move to next node
            current_position += 1  # Increment current position
        if temp is not None:
            return {
                "Model": temp.model,
                "Brand": temp.brand,
                "Price": temp.price,
            }  # Return product
        else:
            return None  # Return None

    def admindisplay(self):
        temp = self.head
        dict = {}
        brand = []
        model = []
        price = []
        quantity = []
        i = 1
        index = []
        while temp != None:  # Display as a table
            model.append(temp.model)
            brand.append(temp.brand)
            price.append(temp.price)
            quantity.append(temp.quantity)
            index.append(i)
            temp = temp.next  # Move to next node
            dict = {
                "Position": index,
                "Model": model,
                "Brand": brand,
                "Price": price,
                "Quantity": quantity,
            }
            i = i + 1
        print(
            tabulate(
                dict,
                headers="keys",
                tablefmt="fancy_grid",  # Display as a table
            )
        )

    def UpdateQuantity(self, model):  # Update quantity
        temp = self.head
        while temp != None:  # Traverse the list
            if temp.model == model:  # If model matches
                temp.quantity = temp.quantity - 1  # Decrement quantity
            temp = temp.next  # Move to next node

    def TopProduct(self):  # Top product
        temp = self.head
        max = self.head.quantity  # Maximum quantity
        if temp.quantity == 10:  # If quantity is 10
            temp = temp.next  # Move to next node
        while temp != None:  # Traverse the list
            if temp.quantity < max:  # If quantity is less than max
                max = temp.quantity  # Update max
                model = temp.model
                brand = temp.brand
                price = temp.price
            temp = temp.next  # Move to next node
        try:
            print("Top Product")
            print("Model: ", model)
            print("Brand: ", brand)
            print("Quantity Sold:", 10 - max)  # Quantity sold
        except:
            print("No products sold")  # If no products sold

    def Restock(self):
        temp = self.head
        self.admindisplay()
        pos = input(
            "Enter the position of the product to restock: "
        )  # Position to restock
        if pos == "all":  # Restock all products
            while temp != None:  # Traverse the list
                temp.quantity = 10  # Restock
                temp = temp.next
            print("All products restocked successfully")
        else:
            for i in range(int(pos) - 1):  # Traverse the list
                temp = temp.next  # Move to next node
            temp.quantity = 10  # Restock
            print("Product restocked successfully")


class ShoppingCart:  # Shopping cart class
    def __init__(self):  # Constructor
        self.cart = []
        self.head = None

    def add_to_cart(self, product):  # Add to cart
        self.cart.append(product)

    def remove_from_cart(self, position):
        if 1 <= position <= len(self.cart):  # If position is valid
            removed_product = self.cart.pop(position - 1)  # Remove from cart
            print(
                # Display removed product
                f"Removed {removed_product['Brand']} {removed_product['Model']} from the cart."
            )
        else:
            print("Invalid position.")  # If position is invalid

    def display_cart(self):
        if not self.cart:
            print("Your cart is empty.")  # If cart is empty
        else:
            print("Your Shopping Cart:")
            headers = ["Position", "Model", "Brand", "Price"]  # Display as a table
            cart_data = [
                [
                    i + 1,
                    item["Model"],
                    item["Brand"],
                    item["Price"],
                ]  # Display as a table
                for i, item in enumerate(self.cart)
            ]
            print(tabulate(cart_data, headers=headers, tablefmt="fancy_grid"))

    def checkout(self):  # Checkout
        self.display_cart()
        price = sum([item["Price"] for item in self.cart])  # Total price
        print(f"Total price: {price}")  # Total price
        print("1. Confirm")
        print("2. Cancel")
        choice = int(input("Enter your choice: "))  # Choice
        if choice == 1:
            print("Order placed successfully")  # Order placed successfully
            for item in self.cart:
                if (  # If model is mobile
                    item["Model"] == "F62"
                    or item["Model"] == "F41"
                    or item["Model"] == "F31"
                    or item["Model"] == "F21"
                    or item["Model"] == "X"
                    or item["Model"] == "12"
                    or item["Model"] == "14"
                    or item["Model"] == "15"
                    or item["Model"] == "Note 10"
                    or item["Model"] == "Note 9"
                    or item["Model"] == "Note 8"
                    or item["Model"] == "Note 7"
                ):
                    mobile.UpdateQuantity(item["Model"])  # Update quantity
                elif (  # If model is television
                    item["Model"] == "8k 64 inch"
                    or item["Model"] == "4k 55 inch"
                    or item["Model"] == "4k 40 inch"
                    or item["Model"] == "4k 32 inch"
                    or item["Model"] == "Bravia 64 inch"
                    or item["Model"] == "Bravia 55 inch"
                    or item["Model"] == "Bravia 40 inch"
                    or item["Model"] == "Bravia 32 inch"
                    or item["Model"] == "SM 64 inch"
                    or item["Model"] == "SM 55 inch"
                    or item["Model"] == "SM 40 inch"
                    or item["Model"] == "SM 32 inch"
                ):
                    televisions.UpdateQuantity(item["Model"])
                elif (  # If model is watch
                    item["Model"] == "Storm"
                    or item["Model"] == "Enigma"
                    or item["Model"] == "Flash"
                    or item["Model"] == "Xplorer"
                    or item["Model"] == "Reflex 3.0"
                    or item["Model"] == "Reflex Invoke"
                    or item["Model"] == "Reflex Beat"
                    or item["Model"] == "Reflex 2.0"
                    or item["Model"] == "Series 8"
                    or item["Model"] == "Series 7"
                    or item["Model"] == "Series 6"
                    or item["Model"] == "Series 5"
                ):
                    watches.UpdateQuantity(item["Model"])  # Update quantity
            print("Thank you for shopping with us")
            return self.cart  # Return cart
        elif choice == 2:
            print("Order cancelled")
        self.cart = []

    def ClearCart(self):
        self.cart = []


class Account:  # Account class
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""  # password
        self.log_detail = ""  # to check who is logged in
        self.log = False  # to check if someone is logged in

    def acc_create(self):
        print("Enter your details")
        self.name = input("Enter your name: ")
        self.email = input("Enter your email: ")
        self.password = pwinput.pwinput("Enter your password: ", "*")  # Hide password
        data1 = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }  # Create a dictionary

        try:
            with open("user.json", "r") as f:  # Open user.json
                data = json.load(f)
        except:
            data = []  # If file is empty

        data.append(data1)  # Append to data

        with open("user.json", "w") as f:  # Open user.json
            json.dump(data, f, indent=4)  # Dump data to user.json

        print("Account created successfully")
        self.log_detail = self.email  # Email of the user
        self.log = True
        return self.log

    def login(self):
        self.email = input("Enter your email: ")
        self.password = pwinput.pwinput("Enter your password: ", "*")  # Hide password

        try:
            with open("user.json", "r") as f:
                data = json.load(f)
        except:
            print(
                "No user accounts found. Please create an account first."
            )  # If file is empty
            return False

        for user in data:
            if (
                user["email"] == self.email and user["password"] == self.password
            ):  # If email and password matches
                print("Login successful")
                self.log = True
                self.name = user["name"]  # Name of the user
                self.log_detail = self.email  # Email of the user
                return self.log

        print("Invalid email or password")
        self.log = False
        return self.log

    def logout(self):
        self.log = False
        print("Logged out successfully")
        return self.log

    def AdminLogin(self):
        self.email = input("Enter your email: ")
        self.password = pwinput.pwinput("Enter your password: ", "*")
        with open(f"admin.json", "r") as f:
            data = json.load(f)
            for user in data:
                if user["email"] == self.email and user["password"] == self.password:
                    print("Login successful")
                    self.log = "Admin"
                    return self.log
                else:
                    print("Invalid email or password")
                    self.log = False
                    return self.log

    def Purchased(self, cart):  # Update purchase history
        with open("user.json", "r") as f:
            data = json.load(f)
            for i in range(len(data)):
                if data[i]["email"] == self.email:  # If email matches
                    try:
                        data[i]["purchase_history"].append(
                            cart
                        )  # Append to purchase history
                    except:
                        # If purchase history is empty
                        data[i]["purchase_history"] = []
                        data[i]["purchase_history"].append(
                            cart
                        )  # Append to purchase history
                    with open("user.json", "w") as f:
                        json.dump(data, f, indent=4)
                        print(
                            "Purchase history updated successfully"
                        )  # Purchase history updated successfully

    def PurchaseHistory(self):  # Display purchase history
        with open("user.json", "r") as f:
            data = json.load(f)
            for i in range(len(data)):
                if data[i]["email"] == self.email:  # If email matches
                    try:
                        data1 = data[i]["purchase_history"]  # Purchase history
                    except:
                        try:
                            with open("user.json", "r") as f:
                                data = json.load(f)
                                data[i]["purchase_history"] = []
                                json.dump(data, f, indent=4)
                            print("No purchase history found")
                        except:
                            break
        print("Purchase History:")
        order = []
        model = []
        brand = []
        price = []
        for i in range(len(data1)):
            for j in range(len(data1[i])):  # Traverse the list
                order.append(i + 1)
                model = data1[i][j]["Model"]
                brand = data1[i][j]["Brand"]
                price = data1[i][j]["Price"]
                purchase_history.InsertAtEnd(
                    model, brand, price, 10
                )  # Insert at end, keep quantity as 10 as it is not required
        purchase_history.display()  # Display purchase history

    def MyAccount(self):  # My account
        print("1. Account Details")
        print("2. Change Password")
        print("3. Delete Account")
        print("4. Purchase History")
        print("5. Admin Login")
        print("6. Logout")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            if self.log_detail == "":
                print("Login first")  # If no one is logged in
            else:
                print("Name: ", self.name)
                print("Email: ", self.email)
        elif choice == 2:
            if self.log_detail == "":
                print("Login first")
            else:
                self.password = pwinput.pwinput(
                    "Enter your new password: ", "*"
                )  # Hide password
                with open("user.json", "r") as f:
                    data = json.load(f)
                    for i in range(len(data)):
                        if data[i]["email"] == self.email:
                            data[i]["password"] = self.password
                            with open("user.json", "w") as f:
                                json.dump(data, f, indent=4)
                                print("Password updated successfully")
                                pass

        elif choice == 3:
            if self.log_detail == "":
                print("Login first")
            else:
                with open("user.json", "r") as f:
                    data = json.load(f)

                updated_data = [
                    user for user in data if user["email"] != self.email
                ]  # updated data without the user to be deleted

                with open("user.json", "w") as f:
                    json.dump(
                        updated_data, f, indent=4
                    )  # Dump updated data to user.json
                print("Account deleted successfully")
                self.log = False
                return self.log
        elif choice == 4:
            if self.log_detail == "":  # If no one is logged in
                print("Login first")
            else:
                self.PurchaseHistory()  # Display purchase history
                pass
        elif choice == 5:
            l = Account.AdminLogin()  # Admin login
            return l
        elif choice == 6:
            l = Account.logout()  # Logout
            return l


# Create linked lists
mobile = LinkedList()
televisions = LinkedList()
watches = LinkedList()
purchase_history = LinkedList()
shopping_cart = ShoppingCart()

# importing data from csv file where 0th column is model, 1st column is brand, 2nd column is price, 3rd column is quantity and 4th column is type of product, it is required to constantly update the quantity of products once they are sold and some admin perform operations.
with open("products.csv", "r") as f:  # Open products.csv
    reader = csv.reader(f)
    for row in reader:  # Traverse the list
        if row[4] == "Mobile":
            mobile.InsertAtEnd(str(row[0]), str(row[1]), int(row[2]), int(row[3]))
        elif row[4] == "Television":
            televisions.InsertAtEnd(str(row[0]), str(row[1]), int(row[2]), int(row[3]))
        elif row[4] == "Watch":
            watches.InsertAtEnd(str(row[0]), str(row[1]), int(row[2]), int(row[3]))

log = False  # initially no one is logged in
# here we update log variable to true and it is constantly checked in while loop to check if someone is logged in or not
print("1. Account Create")
print("2. Login")
print("3. Logout")
print("4. Admin Login")
print("5. Exit")
Account = Account()
choice = int(input("Enter your choice: "))
if choice == 1:
    log = Account.acc_create()
elif choice == 2:
    log = Account.login()
elif choice == 3:
    log = Account.logout()
    pass
elif choice == 4:
    log = Account.AdminLogin()

while log == True:  # while loop to check if someone is logged in or not
    print("1. Explore")
    print("2. Search")
    print("3. Cart")
    print("4. My Account")
    choice = int(input("Enter your choice: "))
    os.system("cls")  # Clear screen

    if choice == 1:
        print("1. Mobiles")
        print("2. Televisions")
        print("3. Watches")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            mobile.display()
            print("1. Add to cart")
            print("2. Back")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                pos = int(
                    input("Enter the position of the product to add to cart: ")
                )  # Position of the product to add to cart
                product = mobile.get_product_by_position(pos)  # Get product by position
                if product:
                    shopping_cart.add_to_cart(product)  # Add to cart
                    print(
                        "Product added to cart successfully"
                    )  # Product added to cart successfully
            elif choice == 2:
                pass
                os.system("cls")
        elif choice == 2:
            televisions.display()
            print("1. Add to cart")
            print("2. Back")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                pos = int(input("Enter the position of the product to add to cart: "))
                product = televisions.get_product_by_position(
                    pos
                )  # Get product by position
                if product:
                    shopping_cart.add_to_cart(product)  # Add to cart
                    print("Product added to cart successfully")
            elif choice == 2:
                pass
                os.system("cls")  # Clear screen
        elif choice == 3:
            watches.display()
            print("1. Add to cart")
            print("2. Back")
            choice = int(input("Enter your choice: "))  # Choice
            if choice == 1:
                pos = int(
                    input("Enter the position of the product to add to cart: ")
                )  # Position of the product to add to cart
                product = watches.get_product_by_position(pos)
                if product:
                    shopping_cart.add_to_cart(product)
                    print(
                        "Product added to cart successfully"
                    )  # Product added to cart successfully
            elif choice == 2:
                pass
                os.system("cls")
    elif choice == 2:
        print("Search For")
        print("1. Mobiles")
        print("2. Televisions")
        print("3. Watches")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            matching_products, product_brand = mobile.search()
            ch = int(
                input("Enter 1 to filter by price: ")
            )  # enter 0 to not filter by price
            if ch == 1:
                matching_products = mobile.FilterByPrice(
                    product_brand
                )  # Filter by price
            if matching_products:  # If matching products
                print("1. Add to cart")
                print("2. Back")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    pos = int(
                        input(
                            "Enter the position of the product to add to cart: "
                        )  # Position of the product to add to cart
                    )
                    if 1 <= pos <= len(matching_products):  # If position is valid
                        # Get product by position
                        product = matching_products[pos - 1]  # Get product by position
                        shopping_cart.add_to_cart(product)  # Add to cart
                        print("Product added to cart successfully")
                    else:
                        print("Invalid position.")
                elif choice == 2:
                    pass
            else:
                pass
                os.system("cls")
        elif choice == 2:
            matching_products, product_brand = televisions.search()  # Search
            ch = int(input("Enter 1 to filter by price: "))
            if ch == 1:
                matching_products = televisions.FilterByPrice(
                    product_brand
                )  # Filter by price
            if matching_products:
                print("1. Add to cart")
                print("2. Back")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    pos = int(
                        input("Enter the position of the product to add to cart: ")
                    )
                    if 1 <= pos <= len(matching_products):  # If position is valid
                        # Get product by position
                        product = matching_products[pos - 1]
                        shopping_cart.add_to_cart(product)  # Add to cart
                        print("Product added to cart successfully")
                    else:
                        print("Invalid position.")
                elif choice == 2:
                    pass
                else:
                    pass
        elif choice == 3:
            matching_products, product_brand = watches.search()  # Search
            ch = int(input("Enter 1 to filter by price: "))  # Filter by price
            if ch == 1:
                matching_products = watches.FilterByPrice(
                    product_brand
                )  # Filter by price
            if matching_products:
                print("1. Add to cart")
                print("2. Back")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    pos = int(
                        input(
                            "Enter the position of the product to add to cart: "
                        )  # Position of the product to add to cart
                    )
                    if 1 <= pos <= len(matching_products):  # If position is valid
                        # Get product by position
                        product = matching_products[pos - 1]
                        shopping_cart.add_to_cart(product)  # Add to cart
                        print("Product added to cart successfully")
                    else:
                        print("Invalid position.")
                elif choice == 2:
                    pass
            else:
                pass
    elif choice == 3:
        shopping_cart.display_cart()  # Display cart
        print("1. Remove from cart")  # Remove from cart
        print("2. Checkout")  # Checkout
        choice = int(input("Enter your choice: "))
        if choice == 1:
            pos = int(
                input("Enter the position of the product to remove from the cart: ")
            )
            shopping_cart.remove_from_cart(pos)  # Remove from cart
            shopping_cart.display_cart()  # Display cart
        if choice == 2:
            cart = shopping_cart.checkout()  # Checkout
            Account.Purchased(cart)  # Update purchase history
            shopping_cart.ClearCart()  # Clear cart after checkout
    elif choice == 4:
        log = Account.MyAccount()  # My account

while log == "Admin":  # while loop to check if admin is logged in or not
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Price")
    print("4. Show Inventory")
    print("5. Top Product")
    print("6. Restock")
    print("7. Logout")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("1. Mobile")
        print("2. Television")
        print("3. Watch")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            model = input("Enter the model: ")
            brand = input("Enter the brand: ")
            price = input("Enter the price: ")
            mobile.display()  # Display as a table
            pos = int(
                input("Enter the position to add the product: ")
            )  # Position to add the product
            mobile.InsertAtPos(pos, model, brand, price)  # Insert at position
            print("Product added successfully")  # Product added successfully
            mobile.display()  # Display as a table
        elif choice == 2:
            model = input("Enter the model: ")
            brand = input("Enter the brand: ")
            price = input("Enter the price: ")
            televisions.display()
            pos = int(
                input("Enter the position to add the product: ")
            )  # Position to add the product
            televisions.InsertAtPos(pos, model, brand, price)  # Insert at position
            print("Product added successfully")  # Product added successfully
            televisions.display()  # Display as a table
        elif choice == 3:
            model = input("Enter the model: ")
            brand = input("Enter the brand: ")
            price = input("Enter the price: ")
            watches.display()
            pos = int(
                input("Enter the position to add the product: ")
            )  # Position to add the product
            watches.InsertAtPos(pos, model, brand, price)  # Insert at position
            print("Product added successfully")  # Product added successfully
            watches.display()  # Display as a table
    elif choice == 2:
        print("1. Mobile")
        print("2. Television")
        print("3. Watch")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            mobile.display()  # Display as a table
            pos = int(
                input("Enter the position of the product to be removed: ")
            )  # Position of the product to be removed
            mobile.DeleteAtPos(pos)  # Delete at position
            # Product removed successfully
            print("Product removed successfully")
            mobile.display()  # Display as a table
        elif choice == 2:
            televisions.display()
            pos = int(
                input("Enter the position of the product to be removed: ")
            )  # Position of the product to be removed
            televisions.DeleteAtPos(pos)  # Delete at position
            # Product removed successfully
            print("Product removed successfully")
            televisions.display()  # Display as a table
        elif choice == 3:
            watches.display()
            pos = int(input("Enter the position of the product to be removed: "))
            watches.DeleteAtPos(pos)  # Delete at position
            # Product removed successfully
            print("Product removed successfully")
            watches.display()  # Display as a table
    # the updated price reflects in the linked list which is then updated in the csv file
    elif choice == 3:
        print("1. Mobile")
        print("2. Television")
        print("3. Watch")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            mobile.display()  # Display as a table
            mobile.UpdatePrice()  # Update price
            mobile.display()  # Display as a table
        elif choice == 2:
            televisions.display()  # Display as a table
            televisions.UpdatePrice()  # Update price
            televisions.display()  # Display as a table
        elif choice == 3:
            watches.display()  # Display as a table
            watches.UpdatePrice()  # Update price
            watches.display()  # Display as a table
    elif choice == 4:
        print("1. Mobile")
        print("2. Television")
        print("3. Watch")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            mobile.admindisplay()  # Display as an admin to show inventory
        elif choice == 2:
            televisions.admindisplay()  # Display as an admin to show inventory
        elif choice == 3:
            watches.admindisplay()  # Display as an admin to show inventory
    elif choice == 5:
        print("1. Mobile")
        print("2. Television")
        print("3. Watch")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            mobile.TopProduct()  # find top product
        elif choice == 2:
            televisions.TopProduct()  # find top product
        elif choice == 3:
            watches.TopProduct()  # find top product
    elif choice == 6:
        print("1. Mobile")
        print("2. Television")
        print("3. Watch")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            mobile.Restock()  # Restock
        elif choice == 2:
            televisions.Restock()  # Restock
        elif choice == 3:
            watches.Restock()  # Restock
    elif choice == 7:
        print("Logged out successfully")
        log = False

# updating the csv file with the updated linked list, when next time the program is run the updated csv file is loaded into the linked list and the linked list is updated with the new data like the quantity of products sold and the quantity of products left, updated price, new products etc. As lunked list is dynamic , new products can be added easily and the csv file is updated accordingly.
with open("products.csv", "w", newline="") as f:  # Open products.csv
    writer = csv.writer(f)
    writer.writerow(
        ["Model", "Brand", "Price", "Quantity", "Category"]
    )  # Write to products.csv
    temp = mobile.head
    while temp != None:
        writer.writerow([temp.model, temp.brand, temp.price, temp.quantity, "Mobile"])
        temp = temp.next
    temp = televisions.head
    while temp != None:
        writer.writerow(
            [temp.model, temp.brand, temp.price, temp.quantity, "Television"]
        )
        temp = temp.next
    temp = watches.head
    while temp != None:
        writer.writerow([temp.model, temp.brand, temp.price, temp.quantity, "Watch"])
        temp = temp.next
