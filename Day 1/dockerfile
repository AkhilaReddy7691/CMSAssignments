# Use an official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy the script into the container
COPY webscrapping.py .

# Install required packages
RUN pip install requests pandas beautifulsoup4

EXPOSE 8000

# Run the script
CMD ["python", "webscrapping.py"]
