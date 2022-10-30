FROM python

WORKDIR server

COPY . .
RUN pip install mongoengine flask

CMD [ "python", "api.py" ]