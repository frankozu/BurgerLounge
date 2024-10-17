FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to access the application
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

#Adding pytest to test using pytest
RUN pip install pytest


#burgerorderer    |  * Running on http://IP:5000
# burgerorderer    |  * Running on http://IP:5000