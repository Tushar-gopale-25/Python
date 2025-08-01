''';my_tuple = (1, 2, 3)

new_item = 4

new_tuple = my_tuple + (new_item)

print("Original tuple:", my_tuple)

print("Tuple after adding an item:", new_tuple)'''

my_tuple =(1, 2, 3, 4, 5)

temp_list = list(my_tuple)

temp_list.append(6)

new_tuple = tuple(temp_list)

print("Orignal tuple: ", my_tuple)
print("Tuple after adding item", new_tuple)
