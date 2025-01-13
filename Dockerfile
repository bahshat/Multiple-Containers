FROM python:3.9-slim

WORKDIR /app

COPY /app/app.py .

RUN pip install flask sqlalchemy psycopg2-binary

ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--reload", "--host=0.0.0.0", "--port=5000"]