FROM python:3

WORKDIR /usr/app

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .
EXPOSE 80

CMD ["python3", "-u", "manage.py", "runserver"]
