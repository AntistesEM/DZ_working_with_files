print('-----Задача №1-----')
with open('recipes.txt', 'rt', encoding='utf-8') as recipes:
    cook_book = {}
    for line in recipes:
        dish = line.strip()
        cook_book.setdefault(dish, [])
        for i in range(int(recipes.readline())):
            compound = recipes.readline().strip()
            ingredient_name, quantity, measure = compound.split(' | ')
            cook_book[dish].append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        recipes.readline()
for k, v in cook_book.items():
    print('\n' + k + ':', *v, sep='\n')
print('\n-----Задача №2-----\n')


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish_2 in dishes:
        for el in cook_book[dish_2]:
            if el['ingredient_name'] not in res.keys():
                res.setdefault(el['ingredient_name'], {
                    'measure': el['measure'],
                    'quantity': el['quantity'] * person_count
                })
            else:
                res.get(el['ingredient_name'])['quantity'] += \
                    el['quantity'] * person_count
    return res


shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(*[f'{k}: {v}' for k, v in shop_list.items()], sep='\n')

print('\n-----Задача №3-----\n')
line_count = {
    '1.txt': str(sum(1 for line in open('1.txt', encoding='utf-8'))),
    '2.txt': str(sum(1 for line in open('2.txt', encoding='utf-8'))),
    '3.txt': str(sum(1 for line in open('3.txt', encoding='utf-8'))),
}
sorted_line_count = {}
for key in sorted(line_count, key=line_count.get):
    sorted_line_count[key] = line_count[key]
with open('123.txt', 'w', encoding='utf-8') as result:
    for k in sorted_line_count.keys():
        with open(k, encoding='utf-8') as file:
            result.writelines('\n'.join(
                [k, sorted_line_count[k], file.read() + '\n']
            ))
print('Получен файл: 123.txt')
