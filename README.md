<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/aldomatus/flask-docker_simple-rest-api">
    <img src="https://i.imgur.com/HnXl6w4.png" alt="Header" >
  </a>
   <div align="center">
   <a href="https://www.facebook.com/aldo.matusmartinez" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/facebook.svg" title="Facebook" width="60"  margin="30px"/></a><a href="https://github.com/aldomatus/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/github.svg" title="Github" width="60"/></a><a href="https://www.instagram.com/aldomatus1/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/instagram.svg" title="Instagram" width="60"  /></a><a href="https://www.linkedin.com/in/aldomatus/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/linkedin.svg" title="Linkedin" width="60"  /></a>

  </div>

  <h4 align="center"></h4>

  <p align="center">
    A simple REST API made with flask and containerized in Docker so that you can practice the methods: GET, POST, PUT and DELETE, create Docker containers and make use of Docker-compose.yml.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is made with the intention of teaching how to use Docker with Flask in the project we are going to take into account the following points:

* Create the dockerfile that will have the necessary instructions to create a Python image that will later be converted into a single application.
* Docker Compose allows you through YAML files to instruct the Docker Engine to perform tasks, programmatically. Here we will install the mysql image, declare the environment variables for both mysql and Flask, and also declare the volumes.
* We will add the list of requirements in a requirements.txt file that will be executed automatically within the Dockerfile
* Create a REST API with the methods: GET, POST, PUT and DELETE

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Docker](https://www.docker.com/)

### To check your rest api
#### Insomnia

With their streamlined API client, you can quickly and easily send REST, SOAP, GraphQL, and GRPC requests directly within Insomnia.
Link to visit insomnia website: - [Link](https://insomnia.rest/download)
<div align="center">
 <img src=https://seeklogo.com/images/I/insomnia-logo-A35E09EB19-seeklogo.com.png width="150" alt="Header" >
  </div>


#### Postman
Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs—faster.
Link to visit postman website: - [Link](https://www.postman.com/downloads/)
<div align="center">
 <img src=https://seeklogo.com/images/P/postman-logo-F43375A2EB-seeklogo.com.png width="150" alt="Header" >
</div>

<!-- EXPLAIN CODE -->
## Description of the REST API code
<details open="open">
    <summary>Click to see the code</summary>
    
    ``` 
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
    ```
  
</details>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

For this project you need to have Docker and Docker compose installed

<ol>
<li>Link to install Docker engine:</li>
<a href="https://docs.docker.com/engine/install/ubuntu/">Linux</a>
<a href="https://docs.docker.com/engine/install/">  -  Windows or Mac</a>

<li>After installing docker engine install docker compose</li>
<a href="https://docs.docker.com/compose/install/">Linux Windows Mac</a>
</li>

Fist

### Installation

1. To obtain my repository you must create a folder in a desired directory and within this folder open a terminal or use cmd in the case of windows.
2. Clone the repo
   ```
   git remote add origin git@github.com:aldomatus/flask_rest_api.git
   
   ```
3. In the folder where docker-compose.yml is located, open a terminal (the same address where you ran the previous line) and write the following command to build the image.
   ```
   docker-compose build
   ```
4. Once the previous execution is finished, you must run the services made in the build.
   ```
   docker-compose up
   ```
5. If all goes well, our application should already be executing the app.py file with python using the mysql database, now we just have to check by entering the following link in our browser:

   ```
   http://localhost:5000/
   ```
6. You should have a response like this:
   ```
   {"message": "Welcome to my API"}
   ```


<!-- USAGE EXAMPLES -->
## Usage

With this base you can make any flask code, modify the API and adapt it to your projects. It is important that you study the docker code to understand what is behind each file in both the Docker and the docker-compose.yml.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/aldomatus/flask_rest_api/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Aldo Matus - [Linkedin](https://www.linkedin.com/in/aldomatus/) [Facebook](https://www.facebook.com/aldo.matusmartinez/)

Project Link: [Repository](https://github.com/aldomatus/flask_rest_api/)






