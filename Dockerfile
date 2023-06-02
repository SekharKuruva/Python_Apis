FROM python:3.11.0a3-alpine3.15

EXPOSE 8000

#Install funicorn and falcon
RUN pip install gunicorn requests falcon --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org

#Add demo app
COPY ./app /app

WORKDIR /app

CMD ["gunicorn" , "-b", "0.0.0.0:8000","main:api"]