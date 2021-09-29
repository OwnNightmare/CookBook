import os
from pprint import pprint


def open_and_read():
    with open('data.txt', 'r', encoding='utf8') as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            cook_book[dish] = []
            counter = int(file.readline())
            for _ in range(counter):
                ingredient, amount, unit = file.readline().strip().split(' | ')
                amount = int(amount)
                diction = {'ingredient_name': ingredient, 'quantity': amount, 'measure': unit}
                cook_book[dish].append(diction)
            file.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, persons):
    cook_book = (open_and_read())
    shop_list = {}
    for dish in dishes:
        for index, _ in enumerate(cook_book[dish]):
            cook_book[dish][index]['quantity'] *= persons
            ingredient_value = cook_book[dish][index]['ingredient_name']
            quantity_value = cook_book[dish][index]['quantity']
            measure_value = cook_book[dish][index]['measure']
            if not shop_list.get(ingredient_value):
                shop_list[ingredient_value] = {'quantity': quantity_value, 'measure': measure_value}
            else:
                current_amount = shop_list[ingredient_value].get('quantity')
                shop_list[ingredient_value] = {'quantity': current_amount + quantity_value, 'measure': measure_value}
    return shop_list


def show(something):
    pprint(something)


show(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 10))
show(open_and_read())
