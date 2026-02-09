FROM python:3.13-slim

# Arbeitsverzeichnis
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry

# Alles kopieren
COPY pyproject.toml poetry.lock /app/
COPY src/AnimalGame /app/AnimalGame

# Poetry Install
RUN poetry install --no-root

# Standard-Command: CLI starten
CMD ["poetry", "run", "python", "-m", "AnimalGame.__main__", "--cli"]
