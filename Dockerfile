FROM python:2.7-slim

WORKDIR /app

ADD . /app

RUN pip install -- trusted-host pypi.python.org -r requiremens.txt

EXPOSE 80

CMD ["python","app.py"]
