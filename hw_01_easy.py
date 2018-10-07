__author__ = 'Пономарев Игорь Борисович'


# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

number = int(input("Введите целое число от 0 до 100: "))
while number <= 100:
	print(number)
	number = number + 2

print("Программа завершена")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print("A = ", A, "B = ", B)
A, B = B, A
print("A = ", A, "B = ", B)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Пожалуйста укажите ваш возраст: '))
if age < 18:
	print("Извините, пользование данным ресурсом только с 18 лет")
	access = False
else:
	print("Доступ разрешен")
	access = True