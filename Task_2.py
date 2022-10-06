# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний 
# и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def myList (num):          # метод создания списка (рандом)
    import random
    myList = []
    for i in range (num):
        myList.append (random.randint (1, 10))
    # print(myList)
    return myList

def MultiPairNumbers (list):
    resultList = []
    lastEl = len(list) - 1
    if (len(list) % 2 == 0):
        for i in range(len(list) // 2):
            resultList.append(list[i] * list[lastEl])
            lastEl -= 1
    elif (len(list) % 2 != 0):
        for i in range((len(list) // 2) + 1):
            resultList.append(list[i] * list[lastEl])
            lastEl -= 1
    # print (positionList)
    print (f'{list} -> {resultList}')

number = int (input("Введите количество элементов списка: "))
list_res = myList (number)  
print (list_res)  
MultiPairNumbers (list_res)