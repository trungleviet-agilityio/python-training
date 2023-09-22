# Use an official Python runtime as a parent image
FROM python:3.9-alpine3.13

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app/app  # Adjust the working directory to your Django project directory

# Copy requirements files and other project files
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
COPY ./app /app

# Copy the contents of the "public" folder into /vol/web/static
COPY ./public /vol/web/static

# Create the /app/static directory and copy static files into it
RUN mkdir -p /app/app/static
COPY ./app/static /app/app/static

COPY ./gunicorn_config.py /gunicorn_config.py

# Switch to the /app directory
WORKDIR /app

# Expose port 8000
EXPOSE 8000

# Define an argument for enabling development dependencies (optional)
ARG DEV=false

# Install dependencies, collect static files, and configure the environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    /py/bin/pip install gunicorn && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

# Collect static files during the Docker image build
RUN /py/bin/python manage.py collectstatic --noinput

# Set the PATH environment variable
ENV PATH="/scripts:/py/bin:$PATH"

# Switch to the django-user user
USER django-user

# Start the Gunicorn server using the provided configuration
CMD ["gunicorn", "-c", "/gunicorn_config.py", "app.wsgi:application"]
