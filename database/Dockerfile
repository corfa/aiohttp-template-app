# FROM postgres

# ENV POSTGRES_USER=example_user
# ENV POSTGRES_PASSWORD=example_password
# ENV POSTGRES_DB=tasks

# COPY init.sql /docker-entrypoint-initdb.d/

FROM postgres

# Копирование .env файла в контейнер
COPY .env /app/.env

# Загрузка переменных среды из .env файла
RUN set -a && . /app/.env && set +a

# Использование переменных среды в Dockerfile
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}

# Копирование и выполнение SQL-скриптов
COPY init.sql /docker-entrypoint-initdb.d/

