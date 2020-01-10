FROM python:3.4.9

ENV TZ=America/Sao_Paulo

RUN apt-get update -y ; \
	    apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev

WORKDIR /opt

ADD requirements.txt /opt
RUN pip install -r requirements.txt

ADD static /opt/static
ADD templates /opt/templates
ADD app.py /opt/

EXPOSE 5000

CMD ["/usr/local/bin/python", "/opt/app.py"]