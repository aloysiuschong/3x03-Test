#!/usr/bin/env sh

set -x
docker run -d -p 80:80 --name my-apache-php-app -v C:\\Users\\aloys\\Desktop\\3x03 Labs\\3x03 Lab\\src:/var/www/html php:7.2-apache
sleep 1
set +x

echo 'Now...'
echo 'Visit http://localhost to see your PHP application in action.'

