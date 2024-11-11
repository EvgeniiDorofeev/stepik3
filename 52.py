def print_goods(models):
    a=sorted(models, key=lambda item: (str(item['color']).lower(), -item['model']))
    for i in a:
        print(f"Производитель: {i.get('make')},",

              f"модель: {i.get('model')},",

              f"цвет: {i.get('color')}")

models = [{'make': 'Nokia', 'model': 2, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 3, 'color': 'red'},
          {'make': 'Samsung', 'model': 5, 'color': 'Yellow'},
          {'make': 'Apple', 'model': 10, 'color': 'RED'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'BLACK'},
          {'make': 'Honor', 'model': 3, 'color': 'black'},
          {'make': 'Nothing Phone', 'model': 7, 'color': 'Yellow'}]
print_goods(models)