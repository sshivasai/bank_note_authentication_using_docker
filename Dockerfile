FROM continuumio/anaconda3:5.3.0
COPY . /
EXPOSE 5000
WORKDIR /
RUN pip install -r requirements.txt
CMD python app.py
