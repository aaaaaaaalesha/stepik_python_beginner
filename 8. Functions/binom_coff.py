def factorial(num):
    if num == 0 or num == 1:
        return 1
    return factorial(num - 1) * num


def compute_binom(n_, k_):
    return factorial(n_) / (factorial(k_) * factorial(n_ - k_))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(int(compute_binom(n, k)))
