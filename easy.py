__author__ =  " Пономарев Игорь Борисович "

# easy

import os 
import shutil
import sys
 
 # Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


# Создание директорий
def new_path(name):
    path = os.path.join(name)
    try:
        os.makedirs(path)
        print("Создана папка " + name)
    except FileExistsError:
         print("Директория с таким именем уже существует")
          
if __name__ == "__main__":
    for i in range(1, 10):
                          new_path('{}_{}'.format("dir", i))