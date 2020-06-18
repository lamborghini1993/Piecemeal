FROM python:3.6
LABEL maintainer="xiaohao"
RUN apt-get update
RUN pip install flask
COPY app.py /app/
WORKDIR /app
EXPOSE 8888
CMD ["python","app.py"]
