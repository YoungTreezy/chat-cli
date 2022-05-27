FROM python:3.8
ENV PYTHONUNBUFFERED 1


# установка рабочей директории в контейнере
WORKDIR /Chat-Cli

# копирование файла зависимостей в рабочую директорию
COPY requirements.txt .

# установка зависимостей
RUN pip install -r requirements.txt

# копирование содержимого локальной директории src в рабочую директорию
COPY . .

# команда, выполняемая при запуске контейнера
CMD [ "python", "./server.py" ]