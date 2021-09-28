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
    with open('data.txt', encoding='utf8') as file:
        book = {}
        for line in file:
            dish = file.readline().strip()
            book[dish] = []
            counter = int(file.readline())
            for _ in range(counter):
                ingredient, amount, unit = file.readline().strip().split(' | ')
                amount = int(amount)
                diction = {'ingridient_name': ingredient, 'quantity': amount, 'measure': unit}
                book[dish].append(diction)
        return book


def get_shop_list_by_dishes(dishes, persons):
    cook_book = (open_and_read())
    temp_book = {}
    for dish in dishes:
        for index, _ in enumerate(cook_book[dish]):
            cook_book[dish][index]['quantity'] *= persons
            temp_book[cook_book[dish][index]['ingridient_name']] = {'quantity': cook_book[dish][index]['quantity'],
                                                                    'measure': cook_book[dish][index]['measure']}
    return temp_book


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 10))