FROM python:3.12-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

COPY pyproject.toml poe* /app/
RUN poetry install --no-root --no-interaction --no-ansi

COPY app /app/app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
