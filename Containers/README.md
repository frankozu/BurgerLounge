# BurgerLounge Project

## Overview
The BurgerLounge project allows customers to view the menu, place orders, and sends those orders to the kitchen. The system is built using Flask and SQLite for the backend, with Docker managing the different containers.

The main components are:
- **BurgerOrderer**: A customer-facing web interface that allows customers to browse the menu and place orders.
- **MenuStore**: A database that stores information about burgers, condiments, and drinks.
- **KitchenView**: A kitchen-facing web interface that receives and displays customer orders.

## Which modules? Which methods? Which API endpoints?
Testing the BurgerOrderer, KitchenView, and MenuStore modules.
Methods include placing orders, listing menu items, and receiving orders.
API endpoints: /menu, /order, /orders, /search, /order/remove, /order/customize.
## How shall they be tested? How shall they be called? What answers will you get?
Using Pytest
API endpoints are tested using client.get() for GET requests and client.post() for POST requests.
Expected answers are JSON responses, such as order confirmation or error messages.
## Which technologies (e.g. test frameworks) do you need?
pytest for automated testing.
Flask's test for API requests
PDB for debugging.
## How often shall the tests be run? What happens if a test fails?
Tests should be run regularly, especially after changes or before deployment.
If a test fails, it will be shown in the test report, and debugging will be necessary to identify and fix the issue.

## The system will be available on 
BurgerOrderer: http://localhost:5000
KitchenView: http://localhost:5001

## Place an order in a second terminal (the first terminal should be open with docker-compose up --build):
curl -X POST http://localhost:5000/order -H "Content-Type: application/json" -d '{"burger": "Cheeseburger", "drink": "Cola"}'

## To activate venv
source venv/bin/activate

## How to set up and run Docker
docker-compose up --build
## To Stop the containers:
docker-compose down

## after running "python app.py" in the terminal, Find what IP you have and run it like this for example:
curl -X POST http://<IP-HERE>:5000/order -H "Content-Type: application/json" -d '{"burger": "drink": "Cola"}'



## To run tests in docker
docker exec -it burgerorderer pytest
    - When reaching pbd you can:
        - Continue execution by typing "c" and pressing enter
    - To step through the code line by line:
        - Type "n" and press enter
    - To inspect a variable:
        - Type for example "order_data" or "request.data"
    - To exit pdb:
        - Type "q" then enter

## How to Run
### 1. Clone the repository
```bash
git clone https://github.com/frankozu/BurgerLounge.git
cd BurgerLounge
