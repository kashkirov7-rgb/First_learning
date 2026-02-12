first_list = ['32', '54', '68']
sec_list = ['speed', 'fly', 'stand']

third_list = first_list + sec_list
print(third_list)

third_list = first_list.__add__(sec_list)
print(third_list)
