def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

#20 35 40 33 1 12 78 125 10 8

array = list(map(int,input("Введите числа через пробел: \n").split()))
element = int(input("Введите любое число: \n"))
array = sorted(array)
left = int(array[0])
right = int(array[-1])
if element < left or element > right:
    print("Введеное число находится вне указанного диапазона из списка.")
else:
    print(binary_search(array, element, left, right))






