FROM python:3.4.9-slim

RUN apt-get update -y 

WORKDIR /opt

ADD requirements.txt /opt
RUN pip install -r requirements.txt

ADD static /opt/static
ADD templates /opt/templates
ADD app.py /opt/

EXPOSE 5000

CMD ["/usr/local/bin/python", "/opt/app.py"]