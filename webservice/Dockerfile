from python:3.6.4-slim-jessie
RUN pip install pandas
RUN pip install CherryPy
RUN pip install cherrypy-cors
COPY myprocessor.py .
COPY ws.py .
EXPOSE 8081
ENTRYPOINT ["python", "ws.py"]
