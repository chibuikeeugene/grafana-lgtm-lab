# define base image
FROM python:3.12-slim
# setup working directory
WORKDIR /app
# copy package requirements files
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy application files
COPY app.py .

EXPOSE 8022

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8022" ]


