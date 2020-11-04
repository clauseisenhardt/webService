FROM tecadmin/ubuntu-ssh:16.04

RUN apt-get update \
   && apt-get install -y apache2

COPY index.html /var/www/html/
COPY *.js /var/www/html/
COPY *.ico /var/www/html/
COPY style.css /var/www/html/
WORKDIR /var/www/html
CMD ["apachectl", "-D", "FOREGROUND"]
EXPOSE 80

