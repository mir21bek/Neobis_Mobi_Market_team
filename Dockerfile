FROM python:3.10

ENV PYTHONDONTWRITEBITECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt
RUN pip install -r requirements.txt

COPY MobiMarket .
COPY ../.env ./.env

EXPOSE 8000


ENTRYPOINT [ "bash", "-c", "./entrypoint.sh"]
