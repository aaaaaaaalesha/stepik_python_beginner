# Задания

### Задание 1. Список четных.

На вход программе подается четное число n, n ≥ 2. Напишите программу, которая выводит список четных чисел

 `[2, 4, 6, ..., n]`.

##### Формат входных данных

На вход программе подается четное натуральное число.

##### Формат выходных данных

Программа должна текст в соответствии с условием задачи.

**Sample Input:**

`8`

**Sample Output:**

`[2, 4, 6, 8]`

**_Solution:_**
```python
print([i for i in range(2, int(input()) + 1, 2)])
```

### Задание 2. Сумма двух списков.

На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел `L` и `M`. Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков `L` и `M`. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 символ пробел.

##### Формат входных данных

На вход программе подаются две строка текста, содержащие целые числа, разделенные символом пробела.

##### Формат выходных данных

Программа должна текст в соответствии с условием задачи.

**Примечание.** Количество чисел в обоих строках одинаковое.

**Sample Input:**

`3 1 4`

`1 5 9`

**Sample Output:**

`4 6 13`

**_Solution:_**
```python
l_ = input().split()
m_ = input().split()

for i in range(len(l_)):
    print(int(l_[i]) + int(m_[i]), end=" ")
```

### Задание 3. Сумма чисел.

На вход программе подается строка текста, содержащая натуральные числа. Напишите программу, которая вставляет между каждым числом знак `+`, а затем вычисляет сумму полученных чисел.

##### Формат входных данных

На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела.

##### Формат выходных данных

Программа должна текст в соответствии с условием задачи.

**Примечание.** Строковый метод `join()` работает только со списком строк.

**Sample Input:**

`2 5 11 33 55`

**Sample Output:**

`2+5+11+33+55=106`

**_Solution:_**
```python
nums = input().split()

print('+'.join(nums) + '=', end="")
sum = 0

for n in nums:
    sum += int(n)
print(sum)
```

### Задание 4. Валидный номер 🌶🌶.

На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная строка корректным телефоным номером. Строка текста является корректным телефоным номером если она имеет формат:

 - `abc-def-hijk`
 
 или
 
  - `7-abc-def-hijk`
  
  где `a, b, c, d, e, f, h, i, j, k` – цифры от 0 до 9.

##### Формат входных данных

На вход программе подается строка текста.

##### Формат выходных данных

Программа должна вывести `YES` если строка является корректным телефоным номером и `NO` в противном случае.

**Примечание.** Телефонный номер должен содержать только цифры и символ `-`, а количество цифр в каждой группе должны быть правильным.

**Sample Input 1:**

`7-301-447-5820`

**Sample Output 1:**

`YES`

**Sample Input 2:**

`301-447-5820`

**Sample Output 2:**

`YES`

**Sample Input 3:**

`3X1-447-5820`

**Sample Output 3:**

`NO`

**Sample Input 4:**

`3014475820`

**Sample Output 4:**

`NO`

**_Solution:_**
```python
numbers = input().split('-')

if len(numbers) == 4:
    if numbers[0] == '7' and numbers[1].isdigit() and len(numbers[1]) == 3 and numbers[2].isdigit() and len(
            numbers[2]) == 3 and numbers[3].isdigit() and len(numbers[3]) == 4:
        print("YES")
    else:
        print("NO")
elif len(numbers) == 3:
    if (numbers[0].isdigit() and len(numbers[0]) == 3) and (numbers[1].isdigit() and len(numbers[1]) == 3) and (
            numbers[2].isdigit() and len(numbers[2]) == 4):
        print("YES")
    else:
        print("NO")

else:
    print("NO")
```

### Задание 5. Самый длинный.

На вход программе подается строка текста. Напишите программу, **использующую списочное выражение**, которая находит длину самого длинного слова.

##### Формат входных данных

На вход программе подается строка текста.

##### Формат выходных данных

Программа должна текст в соответствии с условием задачи.

**Sample Input:**

`проспал почти всю ночь`

**Sample Output:**

`7`

**_Solution:_**
```python
print(max([len(w) for w in input().split()]))
```

### Задание 6. Молодежный жаргон.

На вход программе подается строка текста. Напишите программу, **использующую списочное выражение**, которая преобразует каждое слово введенного текста в "молодежный жаргон" по следующему правилу:

   1) первая буква каждого слова удаляется и ставится в конец слова; 
   2) затем в конец слова добавляется слог "ки".

##### Формат входных данных

На вход программе подается строка текста на русском языке.

##### Формат выходных данных

Программа должна текст в соответствии с условием задачи.

**Sample Input:**

`проспал почти всю ночь`

**Sample Output:**

`роспалпки очтипки сювки очьнки`

**_Solution:_**
```python
print(*[w[1:] + w[0] + "ки" for w in input().split()])
```
