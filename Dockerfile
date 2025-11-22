# Dockerfile
# Docker image for the dummy Python login system

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Default command – run the login program
# To interact with it, run container with -it
CMD ["python", "login.py"]
