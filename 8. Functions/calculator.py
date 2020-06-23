# объявление функции
def get_shipping_cost(quantity):
    return (quantity - 1) * 120 + 1000


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
