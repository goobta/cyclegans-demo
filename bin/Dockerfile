FROM python:3.8-alpine

COPY requirements.txt .

RUN pip install --upgrade wheel pip gunicorn && \
    pip install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install -r requirements.txt