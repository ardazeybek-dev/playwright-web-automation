FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install playwright
RUN playwright install --with-deps chromium

CMD ["python", "proje.py"]