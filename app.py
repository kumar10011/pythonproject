from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load product data
with open('products.json') as f:
    products = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/product/<int:pid>')
def product(pid):
    item = next((p for p in products if p['id'] == pid), None)
    return render_template('product.html', product=item)

@app.route('/api/products')
def api_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
