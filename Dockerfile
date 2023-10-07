FROM python:3.9-slim-buster
RUN echo "deb http://mirrors.aliyun.com/debian/ buster main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y lsof net-tools curl
WORKDIR /app
ADD . /app
EXPOSE 80
CMD ["python", "main.py"]