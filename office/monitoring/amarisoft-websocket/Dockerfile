FROM python:3.8.11-alpine3.14

COPY amarisoft-sf.py app/

ENV TARGET_ENB="192.168.88.53:9001"
ENV TARGET_MME="192.168.88.53:9000"
ENV INTERVAL=5.0
ENV LOG="/var/log/amarisoft.log"

WORKDIR /app

RUN pip install prometheus-client websockets

CMD ["python", "-u", "amarisoft-sf.py"]
