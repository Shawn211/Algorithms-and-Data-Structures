Queue
======
队列，是一个项的有序集合。其中添加新项的一端称为“队尾”，移除项的一端称为“队首”。最近添加的项必须在队尾等待，而集合中生存最久的项在队首，这种排序原则被称为 FIFO，先进先出。

示意图
------
![](Image/basicqueue.png)

栈操作
------
* enqueue(item) 添加新项到队列的队尾。item 做参数并不返回任何内容。
* dequeue() 从队首移除项，不需要参数并返回该项。
* is_empty() 判断队列是否为空，并返回布尔值。
* size() 返回队列中项的数量。

栈的实现
------
* [Queue](Queue.py)

实际应用
------
* [约瑟夫斯置换](#约瑟夫斯置换)

应用展示
------
#### [约瑟夫斯置换](JosephusPermutation.py)
```Python
# 约瑟夫斯置换
>>> from JosephusPermutation import permutation
>>> permutation([num for num in range(1, 6)], 11)
5
>>> permutation([num for num in range(1, 21)], 71)
12
>>> permutation(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 11)
'A'
```