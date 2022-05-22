FROM python:3.10
WORKDIR /code
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "./run_api.py"]