source_list = []


def bubble_sotring(array):  # Пузырьковая сортировка
    for i_item in range(len(array)):
        for j_item in range(len(array) - i_item - 1):
            if array[j_item] > array[j_item + 1]:
                array[j_item], array[j_item + 1] = array[j_item + 1], array[j_item]
    return array

def binary_search(array, element, left, right):   # Бинарный поиск
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    if element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def list_input(): # Ввод массива с защитой от дурака
    arr = []
    num_inp = input('Введите несколько чисел через пробел или exit: ')
    if num_inp.lower() == 'exit':
        exit()
    try:
        arr = list(map(int, num_inp.split()))
        if not arr:
            raise ValueError
    except ValueError:
        print("Ошибка ввода! Введите только цифры через пробел!")
    return arr


def number_input():    # ввод числа с защитой от дурака
    num = input('Введите число: ')
    try:
        if not int(num):
            raise ValueError
        else:
            return int(num)
    except ValueError:
        print("Ошибка! Введите число!")
        return 0


def main():  # Главная функция - легче читать легче дебажить
    global source_list
    global index_lesser
    global index_element_or_greater
    while(not source_list):
        source_list = list_input()

    number = number_input()
    while(not number):
        number = number_input()

    print("Сортировка по возрастания: {}".format(bubble_sotring(source_list)))
###########################Бинарный поиск###############################################
    index_element_or_greater = binary_search(source_list, number, 0, source_list.index(source_list[-1]))
    index_lesser = index_element_or_greater - 1
    if index_lesser < 0:
        index_lesser = "Элемента с индексом меньше искомого нет."
    if index_element_or_greater == False:
        closest_number = min(source_list, key=lambda x: abs(x - number))
        if closest_number < number:
            index_lesser = source_list.index(closest_number)
            index_element_or_greater = index_lesser + 1
            if index_element_or_greater > source_list.index(source_list[-1]):
                index_element_or_greater = "Большего значения нет"
        else:
            index_element_or_greater = source_list.index(closest_number)
            index_lesser = index_element_or_greater - 1
            if index_lesser < 0:
                index_lesser = "Меньшего значения нет"
    print("Индекс элемента, меньше введенного числа {} в массиве - {} равен: {}"
          .format(number, source_list, index_lesser))

# Запуск здесь
main()