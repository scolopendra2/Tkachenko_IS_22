"""перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге.
Имена вложенных подкаталогов выводить не нужно.
 перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
Файл из ПЗ7 переименовать в PZ_7_1.py. Вывести в консоль информацию о размере файлов в папке test.
 перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
консоль. Использовать функцию basename () (os.path.basename()).
 перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
привязанной к нему программе. Использовать функцию os.startfile().
 удалить файл PZ_7_1.py."""


import os


os.chdir('../PZ_11')
files_in_directory = [f for f in os.listdir()]
print('Все файлы ПЗ_11:')
for file in files_in_directory:
    print(file)

# ------------------------------------------------------------

os.chdir('..')
os.makedirs("test/test1", exist_ok=True)
os.chdir('./PZ_6')
os.replace('PZ_6_1.py', '../test/PZ_6_1.py')
os.replace('PZ_6_2.py', '../test/PZ_6_2.py')
os.chdir('../PZ_7')
os.replace('PZ_7_2.py', '../test/test1/test.txt')
os.chdir('../test')
print("Размер файла PZ_6_1:", os.stat("PZ_6_1.py").st_size)
print("Размер файла PZ_6_2:", os.stat("PZ_6_2.py").st_size)

# ----------------------------------------------------------

os.chdir('../PZ_11')
files = os.listdir('.')
shortest_name_file = min(files, key=lambda x: len(os.path.basename(x)))
print(f'\nФайл из ПЗ_11 с самым коротким именем: {os.path.basename(shortest_name_file)}')
os.chdir('../reports')
pdf_file = 'PZ_3.pdf'
os.startfile(pdf_file)

# ----------------------------------------------------------------

# os.remove("../PZ_7/PZ_7_1.py")
