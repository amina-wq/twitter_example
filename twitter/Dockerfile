FROM python:3.10

WORKDIR /opt/twitter

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

COPY . .

ENTRYPOINT [ "sh", "entrypoint.sh" ]