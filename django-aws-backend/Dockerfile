FROM python:3.10-slim-buster

# Open HTTP port
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

# Install pip and Gunicorn
RUN pip install --no-cache-dir --upgrade pip
RUN pip install gunicorn==20.1.0

# Install dependencies from requirements.txt
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Set the working directory for the application
WORKDIR /app

# Copy the rest of the application files
COPY . /app

# Ensure manage.py is executable (just in case)
RUN chmod +x manage.py

# Set static file directory
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput || echo "collectstatic failed"

# Start the Gunicorn server
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "django_aws.wsgi:application"]
