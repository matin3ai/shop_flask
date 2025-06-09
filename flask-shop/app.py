# Importing Flask to create the web application and handle requests
from flask import Flask, render_template, request
import requests

# Initializing the Flask application
app = Flask(__name__)

# Defining the route for the homepage
@app.route('/')
def index():
    # Fetching products from the Fake Store API with a limit of 8
    url = "https://fakestoreapi.com/products?limit=8"
    response = requests.get(url)
    products = response.json()
    # Retrieving cart data from cookies or initializing an empty cart
    cart = request.cookies.get('cart', '[]')
    cart = eval(cart) if cart else []
    total = sum(item['price'] for item in cart)
    return render_template('index.html', products=products, cart=cart, total=total)

# Route to add a product to the cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Fetching specific product details from the API
    url = f"https://fakestoreapi.com/products/{product_id}"
    response = requests.get(url)
    product = response.json()
    # Retrieving and updating cart data
    cart = request.cookies.get('cart', '[]')
    cart = eval(cart) if cart else []
    cart.append(product)
    resp = app.make_response(render_template('index.html', products=requests.get("https://fakestoreapi.com/products?limit=8").json(), cart=cart, total=sum(item['price'] for item in cart)))
    resp.set_cookie('cart', str(cart))
    return resp

# Route to clear the cart
@app.route('/remove_from_cart')
def remove_from_cart():
    # Resetting cart and total
    resp = app.make_response(render_template('index.html', products=requests.get("https://fakestoreapi.com/products?limit=8").json(), cart=[], total=0))
    resp.set_cookie('cart', '[]')
    return resp

# Running the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)