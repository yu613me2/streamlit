FROM python:3.13-slim

# Установка необходимых библиотек
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода приложения
COPY . .

# Команда для запуска приложения
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
