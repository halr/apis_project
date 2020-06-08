# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
# Gunicorn must be included in the requirements.txt file.
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

ENV APIS_SERVER_ADDRESS apistest5.azurewebsites.net

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder:apis_project. Please enter the Python path to wsgi file.
# If your project does not follow Django's default project structure 
# (that is, a workspace folder and a wsgi.py file within a subfolder named the same as the workspace) 
# you must overwrite the Gunicorn entry point in the Dockerfile to locate the correct wsgi.py file.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "web_project.wsgi"]
