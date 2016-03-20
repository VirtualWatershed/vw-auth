FROM ubuntu:14.04

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y git build-essential python-dev curl python-pip libpq-dev
RUN pip install -U pip
RUN apt-get install -y libssl-dev libffi-dev

RUN curl -sL https://deb.nodesource.com/setup_4.x | sh -
RUN apt-get install -y nodejs
RUN npm install -g bower

COPY . /var/www/vw-auth
WORKDIR /var/www/vw-auth

ENV VWAUTH_SECRET vw-auth

RUN pip install -r requirements/dev.txt
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN bower install

EXPOSE 5000

CMD python manage.py runserver -h 0.0.0.0 -p 5000
