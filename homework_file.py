from pprint import pprint
import os

cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        name = line.strip()
        quantity = int(file_obj.readline().strip())
        res = []
        for item in range(quantity):
            lines = {}
            ing = file_obj.readline().split('|')
            lines['ingredient_name'] = ing[0].strip()
            lines['quantity'] = int(ing[1].strip())
            lines['measure'] = ing[2].strip()
            res.append(lines)
        file_obj.readline()
        cook_book[name] = res

pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    list_1 = []
    for items in dishes:
        list_1.append(items)
    dict_1 = {}
    for keys, values in cook_book.items():
        if keys in list_1:
            for item in values:
                dict_2 = item.copy()
                del dict_2['ingredient_name']
                dict_2['quantity'] *= person_count
                dict_1[item['ingredient_name']] = dict_2

    pprint(dict_1)

get_shop_list_by_dishes(['Омлет','Утка по-пекински'], 3)















