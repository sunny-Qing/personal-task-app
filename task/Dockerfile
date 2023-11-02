FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PORT 5002
EXPOSE 5002
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
