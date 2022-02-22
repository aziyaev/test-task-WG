**Тестовое задание для Junior Python Programmer (стажер)**

**Задание 1:**

1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

```python 
def isEven(value):
  return value % 2 == 0
```

[Source Task 1](https://github.com/aziyaev/test-task-WG/blob/master/task1.py)

Плюсы / Минусы

Как известно, языки высокого уровня - надстройка над ассемблером. Проверяемое значение будет переведено в двоичный код. Так же известно, что четные числа оканчиваются на ноль, а нечетные - на единицу.

``` 0 : 000
1 : 001
2 : 010
3 : 011
4 : 100
5 : 101
6 : 110
7 : 111
```
Сложно ответить, сколько необходимо операций ассемблера, чтобы вернуть остаток от деления. В то же время легко понять, что потребуется всего 1 такт для совершения одной операции И. Что является более эффективным действием.

Соответственно, можем провести замеры работы программы на достаточно больших данных.
```
Division method  0:00:00.229685
Bit operation method 0:00:00.190323
```

**Задание 2:**

2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

1.  Массив

[Source Task 2.1](https://github.com/aziyaev/test-task-WG/blob/master/CyclesBufferQueue_task2.py)

2. Связный список

[Source Task 2.2](https://github.com/aziyaev/test-task-WG/blob/master/CyclesBufferList_task2.py)

**Задание 3:

3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.
