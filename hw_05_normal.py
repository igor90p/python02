# normal

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import easy

while True:
    print("[1] - Перейти в папку")
    print("[2] - Просмотреть содержимое текущей папки")
    print("[3] - Удалить папку")
    print("[4] - Создать папку")
    print("[5] - Выход")
 
    errflag = False
    menu = 0
    try:
        menu = int(input("Выберите действие:"))
    except ValueError:
        errflag = True
 
    if menu == 1:
        dirname = input("Введите имя папки:")
        try:
            easy.change_directory(dirname)
        except Exception as _:
            print("Успешно перешел в папку " + dirname)
 
    if menu == 2:
        easy.list_directory()
 
    if menu == 3:
        dirname = input("Введите имя папки:")
        try:
            easy.remove_directory(dirname)
        except Exception as _:
            print("Успешно удалил папку " + dirname)
 
    if menu == 4:
        dirname = input("Введите имя папки:")
        try:
            easy.make_directory(dirname)
        except Exception as _:
            print("Успешно создал папку " + dirname)
 
    if menu == 5:
        break