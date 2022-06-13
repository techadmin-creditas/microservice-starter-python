FROM python:alpine3.10

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/openapi
RUN mkdir -p /usr/src/configs
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

# install the modules
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY /openapi/. /usr/src/openapi
COPY /src/. /usr/src/app
COPY /configs/. /usr/src/configs

# This just copies the sample files, share the folder as volume and copy the desired configs
# COPY /configs/. /usr/src/configs

EXPOSE 5001

ENTRYPOINT ["python3"]
CMD ["app.py"]