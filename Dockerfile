
FROM python:3.13-slim 
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY food_ex /food_ex
WORKDIR /food_ex

RUN pip install --no-cache-dir -r requirements.txt
 
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]