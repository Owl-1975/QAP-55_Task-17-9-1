#Напишите программу, которой на вход подается последовательность чисел через пробел,
# а также запрашивается у пользователя любое число.
#В качестве задания повышенного уровня сложности можете выполнить проверку соответствия
#указанному в условии ввода данных.
#Далее программа работает по следующему алгоритму:
#- Преобразование введённой последовательности в список
#- Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
#- Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий
#  за ним больше или равен этому числу.
#- При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен
#  в этом модуле. Реализуйте его также отдельной функцией.

#Помните, что у вас есть числа, которые могут не соответствовать заданному условию.
#В этом случае необходимо вывести соответствующее сообщение

entered_array = input("Введите список чисел, разделенных пробелом: ").split()
array = [int(i) for i in entered_array]
print("Вы ввели следующие числа: ", array)

while True:
    try:
        element = int(input("Введите целое положительное число от 1 до 99: "))
        if element < 0 or element > 99:
            raise Exception
        break
    except ValueError:
        print("Введите число цифрами")
    except Exception:
        print("Введенное число выходит за пределы заданного диапазона")

array.append(element)

count = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        count += 1
    array[idx] = x

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if element == array[middle + 1]:
        return middle
    elif element < array[middle + 1]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

a = array.index(element)
b_search = binary_search(array, element, 0, len(array))

print("Список после сортировки и дополнения: ", array)
print("Счетчик итераций при сортировке элементов списка: ", count)
print("Номер позиции добавленного в список элемента: ID = ", a)

if b_search > 0:
    print("Ответ: номер позиции элемента, который меньше введенного пользователем числа: ID = ",
          binary_search(array, element, 0, len(array)))
else:
    print("Перед введенным числом элементы в списке отсутствуют!")