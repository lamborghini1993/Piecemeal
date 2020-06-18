FROM python:3.7-alpine
LABEL maintainer="lamborghini"
ADD . /code
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt
CMD ["python3", "www/app.py"]
