FROM python:3.9-bullseye

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV CONFIG_NAME=DevelopmentConfig

RUN chmod +x prestart.sh

ENTRYPOINT ["bash", "prestart.sh"]

EXPOSE 5000

CMD python app.py