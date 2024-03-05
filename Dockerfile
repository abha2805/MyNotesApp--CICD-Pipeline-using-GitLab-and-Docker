FROM python:latest
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apt-get update -y
RUN pip3 install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["/bin/bash"]
CMD ["-c", "python3 /app/manage.py makemigrations && python3 /app/manage.py migrate && python3 /app/manage.py runserver 0.0.0.0:8080"]
