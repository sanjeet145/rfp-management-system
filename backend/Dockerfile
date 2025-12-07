FROM python:3.13.9

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 3000
# CMD ["gunicorn","--bind 0.0.0.0:8000","-w 4","app:app"]
CMD ["python", "app.py"]
