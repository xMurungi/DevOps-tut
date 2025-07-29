# Step 1: Start from an official, lightweight Python base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the dependencies file into the container
COPY requirements.txt .

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . .

# Step 6: Expose port 8080 to allow traffic to the container
EXPOSE 8080

# Step 7: The command to run when the container starts
CMD ["python", "app.py"]
