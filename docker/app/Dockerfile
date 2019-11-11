FROM python:3.6
RUN mkdir -p /usr/src/app/src
ADD docker/app/requirements.txt /usr/src/app/
ADD src /usr/src/app/src/
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
WORKDIR /usr/src/app/src
CMD [ "gunicorn", "simple_app.wsgi", "-b", "0.0.0.0:8080" ]