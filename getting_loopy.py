def fruit_pluralizer(list_of_strings):
    for fruit in list_of_strings:
        if fruit[len(fruit)-1] == "y":
            print fruit[:len(fruit)-1] + "ies"
        else:
            print fruit + "s"
fruit_list = ['apple', 'berry', 'melon','bannana']
print("Single Fruit: " + str(fruit_list))
fruit_pluralizer(fruit_list)
# Right now Im adding different fruits to the fruit_list to check if the code works with different fruits.


