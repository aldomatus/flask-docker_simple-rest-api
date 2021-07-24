#   Flask 
from flask import Flask, request, jsonify

#   Data
from products import products

app = Flask(__name__)

#   Testing route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response':'ping!'})

#   Create new products
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 12
    }
    products.append(new_product)
    return jsonify({'products': products})

# get data routes
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({'products': products})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound)>0:
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product not found'})

# Update products
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']

        return jsonify({
            'message': 'Product updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product not found'})

# Delete products
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound) > 0:
        products.remove(productFound[0])
        return jsonify({
            'message': 'Product deleted',
            'products': products
        })
    return jsonify(
        {'message': 'Product not found'}
    )


if __name__=='__main__':
    app.run(debug=True, port=5000)