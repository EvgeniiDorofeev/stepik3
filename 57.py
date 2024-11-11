def get_info_about_object(x):
    print(dir(x))
    print(f'Всего у объекта {len(dir(x))} атрибутов и методов')

get_info_about_object(str)