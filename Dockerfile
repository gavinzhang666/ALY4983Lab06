# Use a minimal Python 3.10 image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and model artifact
COPY src/ src/
COPY artifacts/model.pkl artifacts/model.pkl

# Define default command to evaluate the model
CMD ["python", "src/evaluate.py"]
