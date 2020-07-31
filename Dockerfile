FROM mysql

ENV MYSQL_ROOT_PASSWORD=toor

RUN apt update && apt upgarde -y
RUN apt install python3

COPY . /home/compor-plus

WORKDIR  /home/compor-plus

python3