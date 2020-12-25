FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
        libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 80
CMD ["gunicorn", "--bind=0.0.0.0:80", "--access-logfile=-", "bob:create_app()"]
