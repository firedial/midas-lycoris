FROM python:3.10.6-bullseye

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn sqlalchemy mysqlclient

RUN adduser appuser && mkdir /app && chown -R appuser:appuser /app
WORKDIR /app
USER appuser

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
