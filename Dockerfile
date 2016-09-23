FROM python:3.5-slim

MAINTAINER Lucas Bergognon "lucas.bergognon@gmail.com"


# Install Cryptography requirements and Sqlite3 with apt-get
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev \
    sqlite3 \
 && rm -rf /var/lib/apt/lists/*


# Install backend
COPY requirements.txt /tmp
RUN pip --version
RUN pip install --upgrade pip --proxy=$http_proxy \
 && pip --version \
 && pip install -v -r /tmp/requirements.txt --proxy=$http_proxy --timeout=60

WORKDIR /usr/src
COPY . /usr/src


# Expose used ports and entrypoint
EXPOSE 5005
ENTRYPOINT ["./entrypoint.sh"]
