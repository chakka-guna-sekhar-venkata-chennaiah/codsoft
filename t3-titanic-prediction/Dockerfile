FROM python:3.7
WORKDIR /titanic-prediction
COPY . .
RUN python3 -m pip install -r requirements.txt
RUN python3 source/components/data_loading.py
EXPOSE 9993
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"] 
