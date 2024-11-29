import os

print('Текущая директория: ', os.getcwd())

if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
print('Текущая директория: ', os.getcwd())

# os.makedirs(r'third\fourth')
print(os.listdir())
# for i in os.walk('.'):
#     print(i)

os.chdir(r'/home/user_idel/urban_univer/module_7')
print('Текущая директория: ', os.getcwd())
# print(os.listdir())

file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(file)

print(os.stat(file[-1]))
os.system('pip install random2')