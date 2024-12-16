from pprint import pprint

name = 'sample2.txt'

file = open(name, 'r')   # r, w, a - read, write, append
### print(file)
pprint(file.read())
file.close()

# ### ----------------
# file = open(name, 'w')
# file.write('hello')
# ### file.read()     # файл не читабельный, потому что открыт в режиме записи
# file.close()

# ### -----------------
# file = open(name, 'a')
# file.write('\n hello world 2')      ### file.write('hello world 2')
# file.close()

### ----------------
# file = open(name, 'r')
# print(file.tell())
# pprint(file.read())
# print(file.seek(10))      ### print(file.tell())
# pprint(file.read())
# file.close()