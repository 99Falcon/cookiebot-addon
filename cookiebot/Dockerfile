FROM mcr.microsoft.com/playwright/python:v1.54.0-jammy

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY cookie_bot.py /app/
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]
