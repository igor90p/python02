__author__ =  ' Пономарев Игорь Борисович '

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):

    stringified_number = repr(number)
    signif_digits, fract_digits = stringified_number.split(".")
 
    signif_digits = [int(d) for d in signif_digits]
    fract_digits = [int(d) for d in fract_digits]
 
    while len(fract_digits) > ndigits:
        if fract_digits[-1] >= 5:
            try:
                fract_digits[-2] = fract_digits[-2] + 1
            except IndexError:
                signif_digits[-1] = signif_digits[-1] + 1
                if signif_digits[-1] == 10:
                    try:
                        signif_digits[-2] = signif_digits[-2] + 1
                        signif_digits[-1] = 0
                    except IndexError:
                        signif_digits.insert(0, 1)
        fract_digits = fract_digits[:-1]
 
    while len(fract_digits) > 0 and fract_digits[-1] == 10:
        try:
            fract_digits[-2] = fract_digits[-2] + 1
        except IndexError:
            signif_digits[-1] = signif_digits[-1] + 1
            if signif_digits[-1] == 10:
                try:
                    signif_digits[-2] = signif_digits[-2] + 1
                    signif_digits[-1] = 0
                except IndexError:
                    signif_digits.insert(0, 1)
        finally:
            fract_digits = fract_digits[:-1]
 
    signif_digits = ''.join([str(x) for x in signif_digits])
    fract_digits = ''.join([str (x) for x in fract_digits])
 
    return float(signif_digits + '.' + fract_digits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(34325.88889,3))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):

    ticket_number = repr(ticket_number)
    left_part = ticket_number[:3]
    right_part = ticket_number[-3:]
 
    def part_sum(str_part):
        counter = 0
        for n in str_part:
            counter += int(n)
        return counter
 
    if part_sum(left_part) == part_sum(right_part):
        return True
    else:
        return False
 