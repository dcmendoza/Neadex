FROM python:3.12

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "pokedex.py"]