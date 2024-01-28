FROM python:3.8.11-bullseye

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

RUN pip install -r requirements.txt

CMD ["bash", "-c", "python main.py"]