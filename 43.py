def is_table_free(n):#Резервация столов: изменение требований
    if tables[n] == None:
        return True
    return False

def make_order(n, **kwargs):
    set=["salad", "soup", "main_dish", "drink", "desert"]
    order={}
    for i,j in kwargs.items():
        if i in set:
            tables [n]['order'][i] = j


def reserve_table(a, b, c=False, order={}):
    if is_table_free(a) == True:
        tables[a] = {}
        tables[a]['name'] = b
        tables[a]['is_vip'] = c
        tables[a]['order'] = {}


#r=(salad, soup, main_dish, drink, desert)

tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}
make_order(1, soup='Borsh')
make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
make_order(2, drink='Raf', main_dish='Утка по-пекински')
make_order(2, desert='Трюфель', call='такси')
print(tables)