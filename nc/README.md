# Связный список

#### Определение

Кэш -- это такая эвристическая (эмпирическая) структура данных, которая используется для оптимизации систем, где происходит выборка множества повторяющихся записей. Причём одни записи выбираются чаще, а другие реже, и заранее нельзя представить, какие именно.

Это своеобразная хэш-таблица, используемая в схемах, когда количество элементов в ней на большие порядки меньше, чем общее количество значений. Например, мы хотим уместить в табличку размером 1000 элементов хэш на миллионы ключей. В таких ситуациях хэш-таблица обычно быстро полностью заполняется, поэтому требуются механизмы удаления наименее "ценного" элемента.

Активно используется концепция кэша в процессорах, когда доступ к оперативной памяти -- к наиболее "популярным" адресам, кэшируется в небольшом, но очень быстром буфере.

Основное отличие кэшей от других структур данных, основанных на хэш-таблицах, в том, что для кэша надо реализовать схему вытеснения некоторого элемента, когда она вся заполнена. Классическая модель хэш-таблицы будет выдавать отказ в обслуживании, а нам требуется создать на её основе новый класс, который в случае отсутствия свободных слотов будет освобождать один из слотов.

#### Задача

Реализовать на основе словаря класс `NativeCache`, который дополнительно будет учитывать количество обращений к каждому ключу. Когда хэш-таблица заполняется и найти свободное место не удаётся, вытесняется элемент с наименьшим количеством обращений.

#### Дано

Шаблон нового класса:

```python
class NativeCache:
    def __init__(self, sz):
        self.size = sz  # размер кэша
        self.slots = [None] * self.size  # массив для хранения ключей библиотеки
        self.values = [None] * self.size  # массив для хранения значений, соответствующих ключам
        self.hits = [0] * self.size  # массив для хранения кол-ва обращений к соответствующим элементам словаря
```

#### Реализация

Основная сложность задачи -- подобрать наиболее эффективный алгоритм нахождения минимального значения в массиве `hits`.

Исходя из условий задачи данный массив не может быть сортированным, так как его индексы должны соответствовать индексам элементов библиотеки. Поэтому необходимо реализовать поиск наименьшего значений по данному массиву.

Можно несколько оптимизировать процесс нахождения наименьшего значения -- уменьшить кол-во случаев, когда необходимо выполнять такой поиск.

Для этого можно использовать небольшой буфер, в котором бы хранились указатели на элементы с наименьшими значениями, которые вычислялись бы непосредственно в момент получения, добавления или удаления элементов в библиотеку.

```python
class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self._min_hits = [0, 1]  # индексы элементов с минимальным кол-м обращений
```

Во многих случаях будет достаточно взять элемент с наименьшим количеством запросов по такой ссылке без выполнения затратной операции поиска. То есть сложность операции сводится к `O(1)`. Однако не получается сделать так, чтобы это происходило во всех случаях.

Предположим в массиве `hits` все значения равны 0 и в буфере `_min_hits` элементы будут ссылаться на первые элементы в массиве `hits`.

При всех запросах к элементам кэша содержимое буфера `_min_hits` будет соответствовать действительности, кроме тех случаев, когда запрос будет адресован к тем, элементам, на которые хранятся ссылки в рассматриваемом буфере. В этот момент у данного элемента библиотеки кол-во обращений увеличится и мы не можем гарантировать, что в массиве `hits` нет меньшего значения, без выполнения поиска.

В буфере `_min_hits` мы будем хранить более, чем одно значение. Рассмотрим реализацию с двумя значениями.

Допустим первое из них примем за ссылку на элемент с минимальным количеством обращений, а второй элемент примем за ссылку на еще один элемент с минимальным количеством обращений, равным или большим первому.

Тогда мы можем нивелировать рассмотренную ранее проблему -- первый элемент всегда будет ссылаться на элемент с минимальным количеством обращений. Если некий запрос увеличит это кол-во у элемента, на который ссылается первая ссылка буфера, то мы сделаем сверку этого элемента со вторым элементом буфера. Если окажется, что второй элемент ссылается на элемент с меньшим количеством обращений, чем первый, то поменяем местами элементы в буфере и тогда первый элемент буфера по-прежнему будет ссылаться на элемент кэша с минимальным значением.

Однако если запрос увеличит кол-во обращений у элемента, на который ссылается вторая ссылка буфера, то необходимо сделать поиск минимального значения по всем элементам массива `hits`, чтобы гарантировать, что этот элемент ссылается на минимальное значение.

Такое решение, как показали тесты, уменьшает вероятность запуска поиска минимального значения до менее чем 3%.