FROM python

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver"]
