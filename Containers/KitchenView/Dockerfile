# KitchenView Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install required Python packages (Flask for API handling)
RUN pip install -r requirements.txt

# Expose port 5001 for the KitchenView app
EXPOSE 5001

# Command to run the app
CMD ["python", "app.py"]