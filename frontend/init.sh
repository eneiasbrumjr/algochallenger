#!/bin/sh

# env > /app/.env
cd /src
rm .env
npm run build
mv /src/dist/* /app

