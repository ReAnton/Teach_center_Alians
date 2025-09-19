marks = [5, 2, 3]  # список с оценками
print(marks)

empty_list: list = []  # пустой список
print(empty_list)

print(len(empty_list))  # длинна списка

print(sorted(marks))  # сортировка списка

print(sorted(marks, reverse=True))  # обратная сортировка

data = input('Ввведите числа: ').split()  # ввод списка

map(int, input('Введите число: ').split())  # преобразование списка в числа

list(map(int, input('Введите число: ').split()))  # тк с мар невозможно работать, преобразуем его в лист
