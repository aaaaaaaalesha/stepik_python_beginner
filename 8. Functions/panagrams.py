# объявление функции
def is_pangram(txt):
    txt = ''.join(txt.lower().split())
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for c in txt:
        if c in alphabet:
            alphabet.remove(c)

    return len(alphabet) == 0


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
