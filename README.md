🛍️ Flask Shop

A simple and minimalistic e-commerce web app built using Flask. This demo project fetches product data from FakeStoreAPI and allows users to simulate adding/removing items from a shopping cart using browser cookies.
🔧 Features

    🛒 View a list of 8 sample products

    ➕ Add items to a shopping cart

    ➖ Remove items from the shopping cart

    💵 Real-time cart total calculation

    🍪 Cart data stored in browser cookies (no database required)


📁 Project Structure

shop_flask/
├── flask-shop/
│   ├── app.py               # Main Flask application
│   ├── static/
│   │   └── style.css        # CSS styles
│   └── templates/
│       └── index.html       # Main HTML template
├── LICENSE
└── README.md

🚀 Getting Started
Prerequisites

Make sure you have Python 3.7+ installed.
Installation

Clone the repository:

    git clone https://github.com/matin3ai/shop_flask.git
    cd flask-shop

Create a virtual environment and activate it:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the dependencies:

    pip install Flask requests

Run the Flask app:

    python app.py

Open your browser and visit:
http://127.0.0.1:5000

🧪 Tech Stack

    Backend: Python, Flask

    Frontend: HTML, CSS (Vanilla)

    API: Fake Store API

⚠️ Warning

This is a demo project and not secure for production use. Cart data is stored in cookies using eval(), which is unsafe for real-world applications. Do not use this pattern in production—replace with JSON parsing and server-side session handling.
📜 License

This project is licensed under the MIT License – see the LICENSE file for details.
