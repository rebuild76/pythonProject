# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def is_leap_year(x):
    return (x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# str = input("Bla: ")

# try:
#     str = int(str)
# except:
#     print("Fuck Up! Be not so stupid!!!!")
# else:
#     print("Вы ввели {}".format(str))
# finally:
#     print("Exit mother fucker now!")

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
#
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#     return False
#
# print(check_user('hesoyam', 'tgm'))

# def make_adder(x):
#    print(x, " До")
#    def adder(n):
#        print("Внутри adder", x, n)
#        return x + n # захват переменной "x" из nonlocal области
#    print(x, "Псоле")
#    return adder  # возвращение функции в качестве результата


#add_5 = make_adder(5)
#c = add_5(10)

# def linear_solve(a, b):
#     if a:
#         return b/a
#     elif not a and not b:
#         print("Бесконечное количество корней")
#     else:
#         print("Нет корней")
#
# print(linear_solve(0, 0))
"""Вычисление длины списка рекурсией"""
# def minimal(L):
#     if len(L) == 1:
#         return L[0]
#     else:
#         return L[0] if L[0] < minimal(L[1:]) else minimal(L[1:])
#
# a = [4, 5, 6, 13, 34, 333]
#
# print(minimal(a))
"""Зеркальный переворот числа через рекурсию"""
# number = 123456
#
# def mirror_number(num, res=0):
#     if num == 0:
#         return res
#     else:
#         return mirror_number(num // 10, res * 10 + num % 10)
#
# print(mirror_number(number))

"""Сравнение суммы 2-х чисел и возврат"""
# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)
#
# print(equal(211212, 212228))

"""Генератор для вычисление числа Эйлера с заданной точностью"""
#
# def e():
#     n = 1
#     while True:
#         yield (1 + 1/n)**n
#         n += 1
#
# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого - завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение

# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
#
# sorted(data, key=lambda x: x[0] / x[1] ** 2)
#
# print(sorted(data))

# myFile = open('namefile.txt', 'w')
# myFile.write('tttt')
# print(' Hello, sakjddskv lsjdknPAODQ0W-9FINJKSDZN?dc', file=myFile)
# myFile.close()
