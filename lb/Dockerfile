# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 8080

# Set environment variables (optional, can also be passed at runtime)
# ENV GOOGLE_BOOK_API=your_api_key_here

# Run the application
CMD ["python", "main.py"]
