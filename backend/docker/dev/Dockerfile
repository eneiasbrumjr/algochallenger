FROM php:7.3-fpm-alpine3.12

COPY . /var/www/app
COPY init.sh /

RUN chmod 777 /init.sh \
    && chown :www-data /var/www/app \
    && mkdir -p /run/nginx \
    && apk --no-cache add postgresql-dev \
    && docker-php-ext-install pdo_pgsql \
    && docker-php-ext-install pgsql \
    && apk add nginx \
    && apk add postgresql-client

COPY nginx.conf /etc/nginx/nginx.conf
COPY php-fpm.conf /usr/local/etc
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"


WORKDIR /var/www/app

ENTRYPOINT [ "/init.sh" ]