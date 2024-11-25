def custom_write(file_name, strings):
    file_name = 'file_name.txt'
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            byte_pos = file.tell()
            file.write(string + '\n')
            strings_positions[(index, byte_pos)] = string
        return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('file_name.txt', info)
for i in result.items():
    print(i)
