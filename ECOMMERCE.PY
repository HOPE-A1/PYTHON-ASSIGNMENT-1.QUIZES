def add_product(product_name, price, quantity):
    return {"product_name": product_name, "price": price, "quantity": quantity}

def update_price(product, new_price):
    product["price"] = new_price
    return product

def update_quantity(product, quantity_change):
    product["quantity"] += quantity_change
    return product

product = add_product("Laptop", 75000, 10)
product = update_price(product, 72000)
product = update_quantity(product, -2)
print(product)
