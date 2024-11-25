import io
from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r', encoding='utf-8')
print(file.writable())  # метод показывающий, что в файл нельзя записать
print(file.readable())  # метод показывающий, что в файл можно читать
print(file.seekable())  # метод показывающий, что в файле передвигать курсор
print(file.tell())  # метод позволяет найти позицию невидимого курсора
pprint(file.read()) # метод считывает информация текстового файла
print(file.tell())
# file.seek(5)         # метод позволяющий устанавливать невидимый курсор в определенном месте
# print(file.tell())
# file.write('\nnew text')
# print(file.tell())

file.close()