# Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def descimalTobinary (number):
    binary = ''
    num = number
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    print (f'{number} -> {binary}')

number = int(input('Введите число: '))
descimalTobinary (number)