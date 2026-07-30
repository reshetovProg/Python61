PATH = "resources/products.txt"
def add_product(**kwargs):
    products = dict()
    with open(PATH, "r", encoding="UTF-8") as file:
        for i in file.readlines():
            ls = i.split(",")
            products[ls[0]] = ls[1]
        products[kwargs['name']] = f"{kwargs['price']}\n"
    with open(PATH, "w", encoding="UTF-8") as file:
        for key, value in products.items():
            file.write(f"{key},{value}")
        # file.write(f"{kwargs['name']},{kwargs['price']}\n")

# def show_products():
#     with open(PATH, "r", encoding="UTF-8") as file:
#         for i in file.readlines():
#             ls = i.split(",")
#             print(f"{ls[0]} - {ls[1]}", end="")

add_product(name="котел", price=22000)

# show_products()