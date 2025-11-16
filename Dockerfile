FROM python:3

WORKDIR /app

RUN pip install fastapi requests uvicorn

COPY ./app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--port", "8000"]