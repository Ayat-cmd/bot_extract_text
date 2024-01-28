FROM python:3.8.11-bullseye

RUN apt-get install git -y

RUN git clone https://github.com/Ayat-cmd/bot_extract_text.git

WORKDIR /bot_extract_text

RUN pip install -r requirements.txt

CMD ["bash", "-c", "python main.py"]