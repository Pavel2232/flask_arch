FROM python:3.10.6

WORKDIR /app
COPY docker-compose.yaml .
COPY app .
RUN pip install -r requirements.txt
ENTRYPOINT ["bash", "entrypoint.sh"]



CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]




