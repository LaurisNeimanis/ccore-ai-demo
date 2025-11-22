FROM python:3.12-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

COPY pyproject.toml /app/
RUN poetry install --no-root --no-interaction --no-ansi

COPY app.py /app/

CMD ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
