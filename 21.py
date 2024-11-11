shopping_list = {}
def add_item(a, n=1):
    if shopping_list.get(a):
        shopping_list[a]+=n
    else:
        shopping_list.update({a:n})
    return shopping_list

add_item("Bread", 10)
add_item("Potato", 5)
add_item("Milk")
add_item("Orange", 3)
add_item("Orange", 2)
add_item("Milk")
add_item("Bread", 3)

print(shopping_list)