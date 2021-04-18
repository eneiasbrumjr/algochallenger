#!/bin/sh

if [ ! -f "/var/www/app/.env" ]; then
    env > /var/www/app/.env
fi
until PGPASSWORD=$DB_PASSWORD psql -h "db" -U "$DB_USERNAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
  
>&2 echo "Postgres is up - executing command"

php artisan key:generate
php artisan jwt:secret
php artisan migrate --seed
chmod -R 777 /var/www/app/storage
nginx
php-fpm
