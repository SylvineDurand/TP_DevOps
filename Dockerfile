# Use an ARG instruction to set a default value
ARG DEFAULT_NAME="prenom"

FROM python:3-alpine
WORKDIR /app

# Use an ENV instruction to set an environment variable with the ARG value
ENV NAME=$DEFAULT_NAME

# Copie le script dans le conteneur, dans le répertoire /app
COPY script.py script-hello-world.py
COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN source venv/bin/activate

RUN pip install -r requirements.txt

# Exécute le script
CMD ["python", "/app/script-hello-world.py"]

HEALTHCHECK --interval=10s \
  CMD curl -f http://localhost/ || exit 1