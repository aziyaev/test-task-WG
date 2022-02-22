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

Соответственно, можем провести замеры времени работы программы на достаточно больших данных (1000000).
```
Division method  0:00:00.229685
Bit operation method 0:00:00.190323
```

**Задание 2:**

2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

*  Массив

[Source Task 2.1](https://github.com/aziyaev/test-task-WG/blob/master/CyclesBufferQueue_task2.py)

Метод push(item)
* Добавление элемента в очередь.
* Сложность O(1)
```python
  def push(self, item):
      if self.is_full():
          raise Exception("Buffer is full")

      self.items[self.head_index] = item
      self.count += 1
      self.head_index = self.move_index(self.head_index)
```

Метод pop()
* Удаляет элемент из начала очереди и возвращает его.
* Сложность O(1)
```python
  def pop(self):
      if self.is_empty():
          raise Exception("Buffer is empty")

      item = self.items[self.tail_index]
      self.count -= 1
      self.tail_index = self.move_index(self.tail_index)

      return item
```

* Связный список

[Source Task 2.2](https://github.com/aziyaev/test-task-WG/blob/master/CyclesBufferList_task2.py)

Метод push(el)
* Добавление элемента в очередь.
* Сложность O(1)
```python
  def push(self, el):
      if self.isListFull():
          raise Exception("Buffer is full")

      self.head_el.set_data(el)
      self.count += 1
      self.head_el = self.head_el.get_next_el()
```

Метод pop()
* Удаляет элемент из начала очереди и возвращает его.
* Сложность O(1)
```python
  def pop(self):
      if self.isListEmpty():
          raise Exception("Buffer is empty")

      item = self.tail_el.get_data()
      self.count -= 1
      self.tail_el = self.tail_el.get_next_el()

      return item
```

Как можно заметить, обе реализации имеют в среднем равное время выполнения методов push() и pop() ```O(1)```. Возможно, есть смысл сравнить с Deques, которые поддерживают эффектиные по памяти операции добавления и извлечения элементов с любой стороны с примерно одинаковой скоростью ```O(1)```. Так же не стоит забывать и о том, что связные списки могут занимать больше места, так как имеют указатели на следующий элемент.


**Задание 3:**

3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.


