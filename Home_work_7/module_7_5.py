import os
import time

# укажите директорию для обхода
directory = '.'

# Обход директории с использованием os.walk
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Формируем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Формируем время в удобочитаемый вид
        formatted_time = time.strftime("%d. %m. %Y %:%M", time.localtime(filetime))

        # Получаем размер файла
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        patern_dir = os.path.dirname(filepath)

        # Выводим найденные данные о файле
        print(
            f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {formatted_time}, Родительская директория: {patern_dir}")
