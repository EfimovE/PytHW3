# Задайте список из нескольких чисел. Напишите программу, которая
#  найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from turtle import position


def myList (num):          # метод создания списка (рандом)
    import random
    myList = []
    for i in range (num):
        myList.append (random.randint (- 10, 10))
    print(myList)
    return myList

def sumOddPositions (list):
    positionList = []
    sum = 0
    for i in range(len(list)):
        # print (i)
        if (i % 2 != 0):
            sum += list[i]
            positionList.append(list[i])
    print (positionList)
    print (f'{list_res} -> на нечётных позициях {positionList}, ответ: {sum}')

number = int (input("Введите количество элементов списка: "))
list_res = myList (number)  
print (list_res)  
sumOddPositions (list_res)



