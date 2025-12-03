FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install flask requests

CMD ["python", "Main/app.py"]
