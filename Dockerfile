FROM python:3

RUN git clone https://github.com/um-computacion-tm/final-2023-02-08-manolo2829.git

WORKDIR /final-2023-02-08-manolo2829

RUN pip install -r requirements.txt

CMD ["python3", "-m", "unittest"]