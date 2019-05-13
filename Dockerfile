FROM python::alpine3.7
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY counter_app.py /app
EXPOSE 5000
CMD python ./counter_app.py
