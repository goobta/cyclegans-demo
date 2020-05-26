FROM python:3.8-slim

COPY requirements.txt .

RUN pip install --upgrade wheel pip gunicorn supervisor && \
    pip install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install -r requirements.txt

COPY supervisor.conf /etc/supervisord.conf

WORKDIR /home
# ENTRYPOINT gunicorn -w 6 -b 0.0.0.0:8000 cyclegan:app  # For debugging
ENTRYPOINT supervisord -c /etc/supervisord.conf
# CMD bash