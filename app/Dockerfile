FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
ENV AUTHOR=vmshay
ENV UID=079afc63-c110-40a1-8c91-7f1d21b90fe2
EXPOSE 8000
CMD ["python", "main.py"]
