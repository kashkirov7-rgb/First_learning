my_ores = ['iron', 'cooper', 'coal']
other_ores = ['copper', 'iron', 'coal', 'shadow']

print(my_ores == my_ores)

print(len(my_ores))

print(len(other_ores))


posts_ids = [151, 315, 687, 951]

print(posts_ids[0])

print(posts_ids[3])

print(posts_ids[-2])

posts_ids[-2] = 365

print(posts_ids[-2])


del my_ores[1]
print(my_ores)
print(len(my_ores))

print('spisok slovarey')
# список словарей


users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,  # user_id and User name это ключи
        'user_name': 'Bob'  # 831 and Bob это значения напротив ключей
    }
]
print(len(users))

print(users[1]['user_id'])  # [1] - это 831 весь элемент, словарь
# ['user_id'] - это значение которые нужно узнать в этом словаре


my_fruit = 'apple'  # можно объединять списки в один
other_fruit = 'lime'

# можно объединять списки в один, названия переменных 'my_fruits and other_fruits отсутствуют
all_fruit = [my_fruit, other_fruit]

print(all_fruit)

# IndexError: list index out of range  -  если попытаться прочесть номер которого не существует

happy_smile = []

happy_smile.append('h')  # ♦  ♣  такие символы использовать нельзя
happy_smile.append('g')  # .append добавляет в список что либо
happy_smile.append('k')

print(happy_smile)
print(len(happy_smile))

happy_smile.pop()  # .pop удаляет последний элемент из списка,  если .pop(1) то будет удалён элемент под индексом 1
print(happy_smile)

print(len(happy_smile))

# здесь будет сохраняться последний удалённый элемент в списке
# добавление .pop в конце такого хода автоматически удаляет элемент и помещает его в removed_element
removed_element = happy_smile.pop()
print(removed_element)

print(happy_smile)


posts = [654, 987, 321, 459, 327]

posts.sort()

print(posts)  # сортирует список по возрастанию

# сортирует список по убыванию  #аргумент с ключевым словом
posts.sort(reverse=True)
print(posts)

# 15.03

greeting = "Hello from python"
greeting_letters = list(greeting)  # цункция list конвертирует текст в список

print(greeting_letters)
# ['H', 'e', 'l', 'l', 'o', ' ', 'f', 'r', 'o', 'm', ' ', 'p', 'y', 't', 'h', 'o', 'n']

my_dict = {'a': 10, 'b': True}  # a and b это разделы списка
my_dict_key = list(my_dict)

print(my_dict_key)  # выводит названия ключей, а значения утеряны
# ['a', 'b']

print(min(posts))  # 321
print(max(posts))  # 987
print(sum(posts))  # 2748

print(sum(posts)/len(posts))  # сумма(sum) делится на длину списка(len)
# 549.6

my_num1 = [2.5, 5.0]
my_num2 = [3.7, 4.5, 4.9]

all_num = my_num1 + my_num2  # совмещаются 2 числовых списка
print(all_num)
# [2.5, 5.0, 3.7, 4.5, 4.9]

first_two_num = all_num[:2]  # [2.5, 5.0]
print(first_two_num)
# [5.0, 3.7, 4.5]    взяты элементы с определёнными индексами

middle_num = all_num[1:-1]
print(middle_num)

last_two_num = all_num[-2:]  # [4.5, 4.9]
print(last_two_num)

copied_all_num = all_num[:]
# создаётся не ссылка на основу а новый список за счет использования [:]
print(copied_all_num)

copied_dot = all_num.copy()  # создаёт новый список через метод .copy
print(copied_dot)

# тоже копирует но через функцию list, которая создаёт список
copied_dot1 = list(copied_dot)
print(copied_dot1)
