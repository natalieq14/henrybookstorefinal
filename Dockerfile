FROM python:3.10.11-slim

ENV TZ="America/New_York"
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get install -y \    
    postgresql-client \
    build-essential \
    libssl-dev \
    bash \
    git 

RUN pip install --upgrade pip && \
    pip install python-dateutil && \
    pip install -r /requirements.txt 

COPY ./app /app
COPY ./scripts /scripts
WORKDIR /app
EXPOSE 8000

RUN adduser --system --group --no-create-home django && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R django:django /vol && \
    chown -R django:django /app && \
    chmod -R 755 /vol && \
    chmod -R 755 /app && \
    chmod -R +x /scripts

ENV PATH="/scripts:$PATH"

USER django

CMD ["run.sh"]