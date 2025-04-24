# Base image
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Install dependencies
COPY proj_doc/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files to the image
COPY proj_doc/ .

# Expose port
EXPOSE 8000

# Run the app
CMD ["python", "api.py"]