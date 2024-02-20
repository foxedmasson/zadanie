FROM python:3.10-slim

WORKDIR /test_app

COPY rev_avto/deps.txt .

RUN pip install -r deps.txt

COPY rev_avto .
COPY startup.sh .

CMD ["sh",  "startup.sh"]
