ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

USER root
RUN ["chmod", "+x", "/app/docker-entrypoint.sh"]

ENTRYPOINT ["sh", "/app/docker-entrypoint.sh" ]
