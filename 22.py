def show_list(include_quantities=True):
    if include_quantities==True:
        for i in shopping_list:
            print(f'{shopping_list[i]}x{i}')
    else:
        for i in shopping_list:
            print(f'{i}')
shopping_list = {'Bread': 13, 'Potato': 5, 'Milk': 2, 'Orange': 5}
show_list(include_quantities=False)