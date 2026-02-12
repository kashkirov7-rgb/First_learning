other_items = ['10', 'coal', '2', 'fun', 'gray']

del other_items[2]  # other_items.pop(2)
print(other_items)

print(len(other_items))

other_items.sort(reverse=True)  # other_items.reverse
print(other_items)

new_items = ['iron', 'knife']

other_items = other_items + new_items  # other_items.extend(new_items)
print(other_items)
