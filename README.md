# E-Commerce and Inventory Management System

Welcome to the E-Commerce and Inventory Management System repository. This Python project provides a versatile and interactive platform for managing an online store's inventory and customer orders. Below, you'll find details about the project's file structure, including `user.json`, `admin.json`, and `products.csv`.

## File Structure

- `main.py`: The main Python script that runs the E-Commerce and Inventory Management System. It handles user interactions, product management, shopping cart functionality, and more.
- `user.json`: This JSON file stores user account information. Users can create accounts, log in, and manage their details. When users make purchases, their order history is updated in this file.
- `admin.json`: This JSON file is used for administrative logins. Admins can add, remove, and update products in the inventory.
- `products.csv`: A CSV file that stores the product inventory. The inventory is categorized into mobiles, televisions, and watches, with details such as model, brand, price, and quantity. Any updates made by administrators are reflected in this file.


## Getting Started

1. **Python Installation**: Ensure you have Python 3.x installed on your system.

2. **Tabulate Library Installation**: Install the `tabulate` library, which is used for formatting and displaying data in tables. You can install it using `pip`:

   ```bash
   pip install tabulate
   ```

3. **Running the Project**: Run the project by executing main.py:
     ```bash
     python main.py
     ```
4. **Exploring the System**: Follow the on-screen instructions to create user accounts, explore products, add items to the shopping cart, and more.

## User and Admin Management
**User Accounts**: User accounts can be created, and their details are stored in user.json. Users can log in, log out, change passwords, and view their purchase history.

**Admin Panel**: Admins can access the admin panel by logging in. The admin.json file is used to manage admin accounts. Admins have the ability to add, remove, and update products, view inventory, and identify top-selling products.

Please note that this project provides a foundation for building an e-commerce platform. Additional features, such as payment processing and product images, can be added for a complete online shopping experience.

Feel free to contribute, report issues, or suggest improvements to this project. We hope you find this E-Commerce and Inventory Management System useful for your own online store or inventory management needs.
