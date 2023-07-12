FROM python:alpine3.17

WORKDIR /home

COPY hello_world.py $WORKDIR
RUN pip install pymysql
CMD ["python", "hello_world.py"]