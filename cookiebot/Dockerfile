FROM ghcr.io/home-assistant/amd64-base-python:3.12

WORKDIR /app

RUN apk add --no-cache \
    bash \
    chromium \
    nss \
    freetype \
    harfbuzz \
    ttf-freefont

ENV PLAYWRIGHT_BROWSERS_PATH=/usr/lib/chromium/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY cookie_bot.py /app/
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]
