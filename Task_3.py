# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной 
# части элементов.
# минимальное значение дробной части отличное от нуля, у целых 
# чисел дробной части нет их в расчет не берем
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fractionalPart (list):
    fractionalPartList = []
    for i in range(len(list)):
        if (list[i] % 1 != 0):
            fractionalPartList.append(list[i] % 1)
        # print(fractionalPartList)
    return max(fractionalPartList) - min(fractionalPartList)

myList = [1.10, 1.20, 3.10, 5, 10.01]
result = round(fractionalPart(myList), 2)
print(f'{myList} => {result}')