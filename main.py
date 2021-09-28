import os
from pprint import pprint
# with open('data.txt', 'w') as file:
#     file.write('Hello bitches' + '\n')
#     file.write('Fuck off')
#
# with open('data.txt') as file:
#     Hi = file.read()
#     act = file.read()
#     print(Hi)
#     print(act)
#
# print(os.getcwd())
# print('Suck')

# with open('data.txt', 'w', encoding='utf 8') as file:
#     file.write('Wanna eat!' + '\n')
#     file.write('I dont!' + '\n')
#     file.write('I m in')
#     file.write('\n' + '\n')
#     file.write('Hi')


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
                diction = {'ingridient_name': ingredient, 'quantity': amount, 'measure': unit}
                cook_book[dish].append(diction)
            file.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, persons):
    cook_book = (open_and_read())
    shop_list = {}
    for dish in dishes:
        for index, _ in enumerate(cook_book[dish]):
            cook_book[dish][index]['quantity'] *= persons
            ingr = cook_book[dish][index]['ingridient_name']
            quan = cook_book[dish][index]['quantity']
            meas = cook_book[dish][index]['measure']
            if not shop_list.get(ingr):
                shop_list[ingr] = {'quantity': quan, 'measure': meas}
            else:
                current_amount = shop_list[ingr].get('quantity')
                shop_list[ingr] = {'quantity': current_amount + quan, 'measure': meas}

    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 10))