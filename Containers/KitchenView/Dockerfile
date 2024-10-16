# Use Python 3.10 as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install required Python packages
RUN pip install Flask

# Expose port 5001 for KitchenView
EXPOSE 5001

# Command to run the app
CMD ["python", "app.py"]
