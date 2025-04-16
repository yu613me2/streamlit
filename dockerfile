FROM python:3.13-slim
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "main.py","tips.py"]