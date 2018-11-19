Deque
======
双端队列，是一个项的有序集合。其有两个端部，首部和尾部，并且项在集合中保持不变。既可以在前面或后面添加新项，也可以在任一端移除项。在某种意义上，这种混合线性结构提供了单个数据结构中的栈和队列的所有能力。

示意图
------
![](Image/basicdeque.png)

Deque操作
------
* add_front(item) 添加新项到 deque 的首部。item 做参数并不返回任何内容。
* add_rear(item) 添加新项到 deque 的尾部。item 做参数并不返回任何内容。
* remove_front() 从首部移除项，不需要参数并返回该项。
* remove_rear() 从尾部移除项，不需要参数并返回该项。
* is_empty() 判断 deque 是否为空，并返回布尔值。
* size() 返回 deque 中项的数量。

Deque实现
------
* [Deque](Deque.py)

实际应用
------
* [回文检查](#回文检查)

应用展示
------
#### [回文检查](palindromeChecker.py)
```Python
# 回文检查
>>> from palindromeChecker import pal_checker
>>> pal_checker('Shawn2112nwahS')
True
>>> pal_checker('Deadpool')
False
>>> pal_checker('Shawn21112nwahS')
True
```