import requests

API_URL = "http://127.0.0.1:8000/api/products/"

def add_product(name, description, price):
    """
    Sends a POST request to add a new product.
    """
    data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(API_URL + 'create/', json=data)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Failed to create product:", response.json())

def list_products():
    """
    Sends a GET request to retrieve all products.
    """
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Failed to retrieve products:", response.json())

# Example Usage
if __name__ == "__main__":
    # Add new products
    add_product("Laptop", "High-performance laptop", 1200.99)
    add_product("Smartphone", "Latest model smartphone", 799.49)

    # List all products
    list_products()
