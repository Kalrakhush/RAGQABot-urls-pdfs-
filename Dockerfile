# Step 1: Use a Python base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy your application code into the container
COPY . /app

# Step 4: Install any required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port that Streamlit runs on
EXPOSE 8501

# Step 6: Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
