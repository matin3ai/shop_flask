from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://fakestoreapi.com/products?limit=8"
    response = requests.get(url)
    products = response.json()
    cart = request.cookies.get('cart', '[]')
    cart = eval(cart) if cart else []
    total = sum(item['price'] for item in cart)
    return render_template('index.html', products=products, cart=cart, total=total)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    url = f"https://fakestoreapi.com/products/{product_id}"
    response = requests.get(url)
    product = response.json()
    cart = request.cookies.get('cart', '[]')
    cart = eval(cart) if cart else []
    cart.append(product)
    resp = app.make_response(render_template('index.html', products=requests.get("https://fakestoreapi.com/products?limit=8").json(), cart=cart, total=sum(item['price'] for item in cart)))
    resp.set_cookie('cart', str(cart))
    return resp

@app.route('/remove_from_cart/<int:index>')
def remove_from_cart(index):
    cart = request.cookies.get('cart', '[]')
    cart = eval(cart) if cart else []
    if 0 <= index < len(cart):
        cart.pop(index)
    resp = app.make_response(render_template('index.html', products=requests.get("https://fakestoreapi.com/products?limit=8").json(), cart=cart, total=sum(item['price'] for item in cart)))
    resp.set_cookie('cart', str(cart))
    return resp

if __name__ == '__main__':
    app.run()