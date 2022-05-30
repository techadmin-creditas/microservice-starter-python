FROM python:alpine3.10

RUN apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    nginx

RUN mkdir -p /usr/src/app /usr/src/openapi /var/log/supervisor /etc/supervisord.d /opt/logs
WORKDIR /usr/src/app



COPY requirements.txt /usr/src/app/

## install the modules
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install supervisor

COPY /config/supervisord /etc/rc.d/init.d/supervisord
ADD  /config/services/* /etc/supervisord.d/
COPY /config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY /config/uwsgi/uwsgi_params /etc/nginx/uwsgi_params
COPY /config/uwsgi/uwsgi_params /etc/nginx/conf.d/uwsgi_params
COPY /config/uwsgi/microservice_uwsgi.ini /etc/microservice_uwsgi.ini
COPY /config/nginx/microservice.conf /etc/nginx/conf.d/microservice.conf

COPY /openapi/. /usr/src/openapi
COPY /src/. /usr/src/app

#EXPOSE 5001
EXPOSE 80

RUN chmod 755 /etc/rc.d/init.d/supervisord



#ENTRYPOINT ["python3"]
#CMD ["app.py"]

CMD ["/usr/local/bin/supervisord", "-n", "-c", "/etc/supervisord.d/web_service.conf"]
