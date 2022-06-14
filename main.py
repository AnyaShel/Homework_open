from pprint import pprint as a

name_list = ['ingredient_name', 'quantity', 'measure']


def read_recipe(path):
    with open(path, encoding='utf-8') as file:
        cook_book = {}
        for one_dish in file:
            cook_book[one_dish.strip()] = []
            number_of_ingredients = file.readline()
            for i in range(int(number_of_ingredients)):
                ingredient_name = file.readline().strip().split(' | ')
                zip_ = {}
                for ingredient, amount in zip(name_list, ingredient_name):
                    zip_[ingredient] = amount
                cook_book[one_dish.strip()].append(zip_)
            file.readline()
        return cook_book


def shop_list_for_dishes(dishes, person_count, path):
    cook_book = read_recipe(path)
    shopping_list = {}
    for dish in dishes:
        for k in cook_book[dish]:
            if k[name_list[0]] in shopping_list.keys():
                quantity = int(shopping_list[k[name_list[0]]][name_list[1]]) + int(k[name_list[1]]) * person_count
                shopping_list[k[name_list[0]]] = {name_list[2]: k[name_list[2]], name_list[1]: quantity}
            else:
                quantity = int(k[name_list[1]]) * person_count
                shopping_list[k[name_list[0]]] = {name_list[2]: k[name_list[2]], name_list[1]: quantity}
    a(shopping_list, sort_dicts=False)


shop_list_for_dishes(['Омлет', 'Запеченный картофель'], 2, 'recipes.txt')


catalog = ['1.txt', '2.txt', '3.txt']
text = []
dict = {}
flag = True

for log in catalog:
    calc = 0
    with open(log, encoding='utf-8') as file:
        tmp = []
        for i in file.read().split('\n'):
            tmp.append(i)
            calc += 1
        dict[log] = calc
        print(dict)
        text.append(tmp)
    text.sort(reverse=True)

with open('result.txt', mode='w', encoding='utf-8') as r_file:
    for i in text:
        for val, num in list(dict.items()):
            if len(i) == num:
                r_file.write(f'{val}\n')
                r_file.write(f'{num}\n')
                for j in i:
                    r_file.write(f'{j}\n')