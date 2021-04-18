FROM nginx:stable-alpine as production-stage
RUN mkdir /app && mkdir /src
COPY . /src
RUN cd /src && apk add npm && npm install
COPY init.sh /docker-entrypoint.d
COPY ./docker/nginx.conf /etc/nginx/nginx.conf