FROM python:3.11.5-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a user 'appuser' and switch to it
RUN groupadd appuser && useradd -m -g appuser -l appuser
USER appuser

# Set work directory
WORKDIR /code

# Copy and install dependencies
COPY --chown=appuser:appuser ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY --chown=appuser:appuser . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]