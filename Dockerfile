FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install django --break-system-packages

WORKDIR /Users/82102/venv/Scripts/todo_project

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
