#FROM python:3.8

#ADD test.py .

#RUN pip install flask

#RUN pip install boto3

#CMD ["python", "test.py"]

FROM python:3.8

WORKDIR /app

#COPY test.py test.py
RUN pip3 install boto3
RUN pip3 install flask
RUN pip3 install mysql-connector-python


COPY . .
EXPOSE 5000/tcp

CMD [ "python3", "app.py"]
