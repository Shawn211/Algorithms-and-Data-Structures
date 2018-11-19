Linked List
======
链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是并不会按线性的顺序存储数据，而是在每一个节点里存到下一个节点的指针(Pointer)。由于不必须按顺序存储，链表在插入的时候可以达到O(1)的复杂度，比另一种线性表顺序表快得多，但是查找一个节点或者访问特定编号的节点则需要O(n)的时间，而顺序表相应的时间复杂度分别是O(logn)和O(1)。使用链表结构可以克服数组链表需要预先知道数据大小的缺点，链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理。但是链表失去了数组随机读取的优点，同时链表由于增加了结点的指针域，空间开销比较大。

示意图
------
节点：![节点](Image/node.png)

链表：![链表](Image/linkedlist.png)

链表操作
------
#### 无序链表：
* add(item) 添加新项到链表的头部。item 做参数并不返回任何内容。
* remove(item) 在链表中删除 item 项。item 做参数并不返回任何内容。
* append(item) 添加新项到链表的尾部。item 做参数并不返回任何内容。
* pop() 从链表的尾部删除一项 item。并返回 item 内容。
* insert(pos, item) 向链表 pos 位置 插入一个新项。item 做参数并不返回任何内容。
* pop(pos) 删除链表 pos 位置的项，pos 做参数并不需要返回任何内容。
* search(item) 无序链表：搜索链表中的项目。它需要 item 作为参数，并返回一个布尔值。
* index(item) 返回项在列表中的位置。它需要 item 作为参数并返回索引。
* is_empty() 判断链表是否为空，并返回布尔值。
* size() 返回链表中项的数量。

#### 有序链表：
* add(item) 根据大小添加新项到链表中。item 做参数并不返回任何内容。
* remove(item) 在链表中删除 item 项。item 做参数并不返回任何内容。
* pop() 从链表的尾部删除一项 item。并返回 item 内容。
* pop(pos) 删除链表 pos 位置的项，pos 做参数并不需要返回任何内容。
* search(item) 根据大小搜索链表中的项目。它需要 item 作为参数，并返回一个布尔值。
* index(item) 返回项在列表中的位置。它需要 item 作为参数并返回索引。
* is_empty() 判断链表是否为空，并返回布尔值。
* size() 返回链表中项的数量。

链表实现
------
* [UnorderedLinkedList：无序链表](UnorderedLinkedList.py)
* [OrderedLinkedList：有序链表](OrderedLinkedList.py)

实现展示
------
#### [无序链表](UnorderedLinkedList.py)
```Python
# 无序链表
>>> from UnorderedLinkedList import UnorderedLinkedList, show
>>> l = UnorderedLinkedList()
>>> l.is_empty()
True
>>> l.size()
0
>>> l.add(21)
>>> l.add(1)
>>> l.add(211)
>>> show(l)
'211, 1, 21'
>>> l.remove(1)
>>> show(l)
'211, 21'
>>> l.append(711)
>>> show(l)
'211, 21, 711'
>>> l.pop()
711
>>> show(l)
'211, 21'
>>> l.insert(1, 71)
>>> show(l)
'211, 71, 21'
>>> l.pop(1)
71
>>> show(l)
'211, 21'
>>> l.search(21)
True
>>> l.index(21)
1
>>> l.is_empty()
False
>>> l.size()
2
```

#### [有序链表](OrderedLinkedList.py)
```Python
# 有序链表
>>> from OrderedLinkedList import OrderedLinkedList, show
>>> l = OrderedLinkedList()
>>> l.is_empty()
True
>>> l.size()
0
>>> l.add(21)
>>> l.add(71)
>>> l.add(11)
>>> l.add(211)
>>> l.add(1)
>>> show(l)
'1, 11, 21, 71, 211'
>>> l.search(211)
True
>>> l.search(271)
False
```