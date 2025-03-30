# -*- coding: cp1251 -*-
import os
#D:\gitClone\KhamzinRadik\python-2.5\9\task3\main.py
size=0
path_cotol_fil=os.path.join('9')
path=os.path.join('9','task3')
file_n_path=os.path.abspath(path).replace('\\','\\\\')
path_cotol_fil=os.path.abspath(path_cotol_fil).replace('\\','\\\\')
print(file_n_path)
for el in os.scandir(file_n_path):
    size+=os.path.getsize(el)
size=float(size/1024)
count=0
print('Размер каталога (в Кбайтах): ',size)

folder_count=0
for papki in os.listdir(path_cotol_fil): # перебор всех файлов [1](https://tr-page.yandex.ru/translate?lang=en-ru&url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F29769181%2Fcount-the-number-of-folders-in-a-directory-and-subdirectories)
    if os.path.isdir(os.path.join(path_cotol_fil, papki)): # если это каталог [1](https://tr-page.yandex.ru/translate?lang=en-ru&url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F29769181%2Fcount-the-number-of-folders-in-a-directory-and-subdirectories)
        folder_count += 1
print("Количество подкаталогов :",folder_count)

for root_dir, cur_dir, files in os.walk(path_cotol_fil):
    count += len(files)
print('Количество файлов:  :', count)