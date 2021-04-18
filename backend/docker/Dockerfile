FROM php:7.3-fpm-alpine3.12

COPY init.sh /

RUN chmod 777 /init.sh \
    && mkdir /var/www/app \
    && chown :www-data /var/www/app \
    && mkdir -p /run/nginx \
    && apk --no-cache add postgresql-dev \
    && docker-php-ext-install pdo_pgsql \
    && docker-php-ext-install pgsql \
    && apk add nginx \
    && apk add postgresql-client

COPY . /var/www/app

RUN rm /var/www/app/.env

COPY nginx.conf /etc/nginx/nginx.conf
COPY php-fpm.conf /usr/local/etc

WORKDIR /var/www/app
ENV PHP_EXTRA_CONFIGURE_ARGS=null
ENV PHP_CFLAGS=null
ENV PHP_CPPFLAGS=null
ENV PHPIZE_DEPS=null
ENV GPG_KEYS=null
ENV PHP_LDFLAGS=null

ENTRYPOINT [ "/init.sh" ]