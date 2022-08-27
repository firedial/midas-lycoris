FROM python:3.10.6-bullseye

ENV PYTHONPATH /app

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
