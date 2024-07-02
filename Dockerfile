FROM python:3.7-slim

WORKDIR /app

COPY insert_db.py /app/insert_db.py
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "insert_db.py"]