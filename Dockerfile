# python:3.11-slim image from dockerhub
FROM python:3.11-slim

# prevent python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /app

# install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project content into container app/
COPY app/ /app/

# expose port
EXPOSE 8000

# command to run after container starts
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]