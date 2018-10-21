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

                          # Удаление директорий
def path_remove(path_to_remove):
    ui_sure = input("{} {} {}".format("Вы уверены, что хотите удалить ", path_to_remove, "? Y/N"))
 
    if ui_sure == "y" or ui_sure == "Y":
        try:
            os.removedirs(path_to_remove)
            print("Вы успешно удалили " + path_to_remove)
        except (TypeError, FileNotFoundError):
            print("Не верно указан путь")
    else:
        print("Операция отменена")
 
if __name__ == "__main__":
    for i in range(1, 10):
                          path_remove("{}_{}".format("dir", i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()
 
list_dir(main_path)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(first_file,backup_file):
    shutil.copy(first_file,backup_file)
 
first_file = sys.argv[0]
backup_file = first_file + ".backup"
copy_file(first_file,backup_file)
 
 
def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path + " - такой директории нет")

 
def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + " - текущая директория")
    except:
        print(dir_path + " - такой директории нет")
 
dir_path = "D:\\python02\\"
change_dir(dir_path)
