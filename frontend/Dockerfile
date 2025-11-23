FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend app
COPY . /app/

# Streamlit will read ENV from docker-compose
CMD ["streamlit", "run", "app.py"]