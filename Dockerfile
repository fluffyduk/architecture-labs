FROM python:3

WORKDIR /app

RUN pip install fastapi requests

COPY ./app ./app

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"]