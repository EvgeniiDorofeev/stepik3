def is_table_free(n):
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


def delete_order(*,number_table, delete_all=False, **kwargs):
    set = ["salad", "soup", "main_dish", "drink", "desert"]
    if delete_all==True:
        tables[number_table]['order'].clear()
    else:
        for i,j in kwargs.items():
            if j==True and i in set and i in tables[number_table]['order']:
                del tables[number_table]['order'][i]


tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh'}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh')
make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
make_order(2, drink='Raf', main_dish='Утка по-пекински')
make_order(2, desert='Трюфель', call='такси')
print(tables)

delete_order(number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True)
delete_order(number_table=1, soup=True, desert=True, call=True)
print(tables)