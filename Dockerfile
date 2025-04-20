FROM python:3.13-slim


# Копирование кода приложения
COPY . /app

# Установка рабочего каталога
WORKDIR /app
# Установка зависимостей
RUN pip install -r requirements.txt

# Запуск миграций


# Запуск приложения
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000"]