# Use an official Python runtime
FROM python:3.8

# Set working directory inside container
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port your app runs on
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
