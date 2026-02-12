my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = '80'

print(my_disk)
# print(id(my_disk))  # При добалении новых ключей id не изменяется

print(my_disk.keys())
print(list(my_disk.keys()))  # Список содержит ключи словаря


# Удаляет один ключ.. к использованию не рекомендуется, удаляет последний добавленный ключ
print(my_disk.popitem())

print(my_disk)

my_disk['price'] = '80'

print(my_disk.get('type'))  # Если ключа type нет в словаре, то будет none
print(my_disk.get('type', 'hdd'))
# Вторая позиция будет выводить в терминал текст если такого ключа нет

# Используется если нужно внести изменения в словарь не изменяя оригинал
new_disk = my_disk.copy()  # Создал копию

new_disk['type'] = 'ssd'  # Добавил в новый словарь

print(my_disk)  # оригинальный словарь
print(new_disk)  # Копия  # у них будут разные ID


print(len(my_disk))  # длина 2 элемента, 2 пары ключ/значение
