# Builder staging to install all libraries
FROM python:3.11 as builder

RUN pip3 install poetry 

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
# RUN poetry add psycopg2

# Run stage
FROM python:3.11

WORKDIR /app

# ENV JAVA_HOME=/opt/java/openjdk
# COPY --from=eclipse-temurin:8-jdk $JAVA_HOME $JAVA_HOME
# ENV PATH="${JAVA_HOME}/bin:${PATH}"

RUN apt-get update -y && \
    apt-get install -y gcc
# Install JAVA 8, bash and krb5
RUN apt-get update && apt-get install -y bash

# Copy from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY .. .

ENV FLASK_HOST=0.0.0.0 \
    FLASK_PORT=5010
    # JAVA_HOME=/opt/java/openjdk

EXPOSE ${FLASK_PORT}

CMD python3 -m run.dev
