FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Cambiar CMD para ejecutar `query_db.py` por defecto
CMD ["python", "query_db.py"]
