Team Members: I am on my own (no team) since no one answered my message in Canvas.
    - Team Members: Franko (frankozu)
    - GitHub Repository: https://github.com/frankozu/BurgerLounge

Development Environment:
    - OS: Ubuntu
    - Editor: Visual Studio Code
    - Version Control: GitHub repository
    - Environment: Using Python virtual environment.

Git Setup:
    - The repository name is BurgerLounge.
    - Added a description of the project in README.md.

Planning:
    - Created the Planning directory for Goods.
    - Created text files for hamburgers, drinks, and condiments using mkdir and touch. No challenges were faced.

Reflections Directory:
    - Created the Reflections directory for the engineering diary.

Flask and Initial Setup:
    - Installed Flask and set up a Python virtual environment for the project.
    - Set up initial Flask app (app.py), created routes for /menu (GET) and /order (POST).

Configuration Management:
    - Wrote a summary about what configuration management is and why it is used.

Git Workflow:
    - Wrote a summary about the most common git workflow and commands used.

Setting up Flask Application:
    - Set up the BurgerOrderer module using Flask.
    - Created the app.py file and added routes for:
        - /menu (GET) – retrieves data from MenuStore (SQLite database) and returns it as JSON.
        - /order (POST) – accepts customer orders as JSON, logs the request, and returns the order confirmation.
    - Configured a SQLite database connection to retrieve data for burgers, condiments, and drinks.
    Challenges:
        - Initially, Flask wasn’t starting due to a missing app.run() statement. Adding this fixed the issue.
        - Encountered “connection refused” errors when testing the POST request using curl. Resolved this by ensuring Flask was running on the correct IP and port, and by running curl in a separate terminal.
    What I learned:
        - Importance of logging in Flask to track incoming requests.
        - Using curl to test API endpoints and debug network issues.
        - Flask’s 0.0.0.0 binding allows it to listen on all network interfaces.

Containerization and Testing API:
    - Set up Docker containers for BurgerOrderer and connected it with the MenuStore database.
    - Tested API routes using curl and a browser to verify connectivity.
    - Ensured that the /order POST route accepts and processes requests correctly.
    Challenges:
        - Had issues with getting the POST request to work through curl, but after adjusting network setup and testing, the problem was solved.
    What I learned:
        - Containerization with Docker simplifies service management.
        - Importance of testing API endpoints from both local machines and external tools (like Postman).
        - Regular commits allow tracking progress and troubleshooting issues.

JSON management:
    - The /menu route is functioning and returns a JSON response with the menu items.
    - The /order route is functioning and processes customer orders via POST requests.
    - Logging has been added to track incoming orders and JSON payloads.
    - Flask is running smoothly, and I am testing using both curl and a browser.

Docker and Containers:
    - Created docker-compose.yml to define the services for BurgerOrderer, KitchenView, and MenuStore.
    - Set up each service with its own port and volume mappings to share the database between containers.
    - Created Dockerfiles for each service such as BurgerOrderer, KitchenView and MenuStore
        - BurgerOrderer: Handles Flask routes for viewing the menu and placing orders.
        - KitchenView: Receives and displays customer orders from BurgerOrderer.
        - MenuStore: Manages the SQLite database for burgers, condiments, and drinks.
    - Tested that each container starts properly and that the services work together (e.g., BurgerOrderer connects to MenuStore successfully).
    Challenges:
        - Docker didn’t start correctly due to wrong file paths. I fixed it by adjusting the paths in the docker-compose.yml file.
        - MenuStore failed to build at first because of missing packages. This was resolved by updating the Dockerfile and installing the correct dependencies.
    What I learned:
        - I gained experience in managing Docker services and connecting them using volumes and networks.
        - I learned how to troubleshoot common Docker issues, like networking and container startup problems.


Virtual Environment:
    - requests weren’t being recognized by Pylance due to missing packages in the virtual environment. 
    I solved this by activating the virtual environment and installed by "pip install requests". 

Creating test files such as test_kitchenview.py, test_burgerorderer.py, test_menustore.py:
    - This ensures each part of the system (KitchenView, BurgerOrderer, MenuStore) has its own set of tests, 
    making debugging and maintaining the code simpler.
    - Also to keep tests organized. 
    - Good for Modular testing, ensuring scalability and easier updates as the project grows.

Running tests in Docker:
    - Pytest wasn’t working in the Docker container because it wasn’t installed. This caused errors like ModuleNotFoundError: No module named 'flask'. 
    After installing pytest (while in venv) and setting up the environment, the tests worked properly.

Using Debugger in Docker: 
    - I had to use pdb to debug the app in Docker. 
    Pausing the code at breakpoints allowed me to inspect variables and fix issues, especially in the /order route.

What I learned: 
    - I learned how to use pdb to pause and inspect the Flask app running inside Docker. 
    This was helpful in fixing test issues and ensuring everything worked correctly.
    - I now understand how to run and debug tests inside Docker, making sure the local and container environments are in sync.
    - Writing tests for key features (like placing orders and customizing them) with pytest helped finding issues and ensure everything worked correctly.
    - When tests failed, I learned how to debug.

Potential Improvements for the Future:
    - While I wrote basic tests, I should have handling invalid orders, missing menu items, and different customizations.
    - Improving error handling, especially for database issues or incorrect data, would make the app more reliable.
    - As the project grows, I should monitor and optimize the performance of tests to ensure they run efficiently in the container environment.

Functionality debugging:
    - I focused on placing an order for the “Dripping With Lard Heartstopper” burger. 
    The ordering process happens in a Flask app running in a containerized environment.

Breakpoints:
    - I set breakpoints in the app.py file at these points:
        - Before extracting the order data with: order_data = request.get_json()
        - Before logging the raw request data using the Flask logger: app.logger.info(f"Raw request data: {request.data}")
    -These breakpoints helped me inspect the incoming POST request and how the order data was processed.

Debugging controls:
    - I used pdb (Python Debugger) to step through the code. Here’s how I used the key controls:
        - Step Over (n): This allowed me to move to the next line without stepping into any functions.
        - Continue (c): I used this to continue the code execution until the next breakpoint or end of the program.

Watching variables: 
    - I watched the variable "order_data", which holds the data extracted from the order request: order_data = request.get_json()
    - I observed the variable to confirm that it contained the order details: {'burger': 'Dripping With Lard Heartstopper', 'drink': 'Cola'}
    - I made sure that the order_data variable stayed the same throughout the request process and correctly represented the incoming data. 
    By stepping through the lines, I made sure the data remained as expected.

Testing different paths:
    - I focused on placing the “Dripping With Lard Heartstopper” order. 
    - Also tested extra paths such as ordering a different item or submitting incomplete data. 

What went well:
    - Stepping through the code went smoothly once again with pdb. 
    - The debugger allowed me to track the order data and understand how it flowed through the system.
    - I managed to place an order by watching the variable "order_data" and logging the output. 
What didnt go well:
    - At first, setting up the debugging environment in the container was a bit tricky and needed adjustments to run the Flask app in debug mode.
What was easy:
    - Once set up, using pdb to step through code and inspect variables was straightforward.

Usefulness of debugging:
    - In my experience, debugging is a very usefull tool for this project. 
    Using breakpoints and inspecting variables lets me check if the code works as expected and helps catch issues early in development.

Debugging conclusion:
    - Debugging helped me get a better understanidng of working with Flask apps inside Docker containers. 
    By setting breakpoints, stepping through the code, and watching variables, I was able to successfully debug the ordering process and check the app’s behavior.
    - Debugging gives insight into the app’s flow and helps catch errors and unexpected behavior, that is why it will remain important. 

## Debugging Session Documentation

Refer to the debugging session in the following file:
[Debugging Documentation](/Reflections/Debugging.Documentation.txt).

## Configuration managment

Refer to the configuration managment in the following file:
[Configuration Management](/Reflections/Configuration.Management.txt)

## Most used gitworkflow

Refers to the Most Used Gitworkflow in the following file:
[Most used gitworkflow](/Reflections/Most.used.gitworkflow.txt)

## Most used gitworkflow

Refers to reflection in the following file:
[reflection](/Reflections/reflection.txt)
