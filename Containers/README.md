# BurgerLounge Project

## Overview
The BurgerLounge project allows customers to view the menu, place orders, and sends those orders to the kitchen. The system is built using Flask and SQLite for the backend, with Docker managing the different containers.

The main components are:
- **BurgerOrderer**: A customer-facing web interface that allows customers to browse the menu and place orders.
- **MenuStore**: A database that stores information about burgers, condiments, and drinks.
- **KitchenView**: A kitchen-facing web interface that receives and displays customer orders.

## Setup Instructions

## How to set up and run Docker
docker-compose up --build

## The system will be available on 
BurgerOrderer: http://localhost:5000
KitchenView: http://localhost:5001

## How to Run
### 1. Clone the repository
```bash
git clone https://github.com/frankozu/BurgerLounge.git
cd BurgerLounge
