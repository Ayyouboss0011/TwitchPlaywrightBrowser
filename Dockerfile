# For more information, please refer to https://aka.ms/vscode-docker-python
FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Install playwright
RUN python -m pip install playwright && playwright install && playwright install chrome

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["sh", "-c", "xvfb-run --auto-servernum --server-args='-screen 0 1280x720x24' python main.py > output.log 2>&1 && tail -f output.log"]
CMD ["sh", "-c", "Xvfb :99 -screen 0 1280x720x24 & export DISPLAY=:99 && python main.py"]

#CMD ["python", "main.py"]