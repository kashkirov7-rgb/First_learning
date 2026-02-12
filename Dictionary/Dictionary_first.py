# Dict
# Словарь это набор элементов

my_motorbike = {  # слева это названия ключей, находятся на разных строках
    'brand': 'Ducati',  # Если словарь небольшой, 2 ключа, то можно писать на одной строке
    'price': 25000,  # Разделяются запятой
    'Engine_vol': 1.2  # один и тот же ключ в один словарь не суваются
}  # порядок не имеет значения

print(my_motorbike['brand'])
# Ducati

my_motorbike['price'] = 7000  # изменения
print(my_motorbike['price'])

# Если такой ключ уже существует, то значение в нём будет перезаписано
my_motorbike['is_new'] = True

print(my_motorbike)

del my_motorbike['is_new']  # удаление ключей

print(my_motorbike)

key_name = 'brand'

my_motorbike[key_name] = 'BMW'  # Изменение ключа

print(my_motorbike)

print(my_motorbike.get('model'))
print(my_motorbike.get('model', 0))  # Вместо none теперь будет 0
print(my_motorbike.get('price'))
