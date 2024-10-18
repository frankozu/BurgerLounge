# Using Python 3.10 as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# No need to install sqlite3 as it's included in Python

#installing flask that keeps running like the other containers
RUN pip install Flask
# Expose port 5002 for MenuStore
EXPOSE 5002

# Command to run the menu initialization script
CMD ["python", "menu.py"]
