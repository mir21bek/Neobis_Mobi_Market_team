ROM python:3.10

ENV PYTHONDONTWRITEBITECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000


CMD [ "bash", "-c", "./entrypoint.sh"]
