Searching
======
搜索是在项集合中查找特定项的算法过程。搜索通常对于项是否存在返回 True 或 False。有时它可能返回项被找到的地方。

搜索实现
------
* 顺序查找
   * [无序列表顺序查找](#无序列表顺序查找)
   * [有序列表顺序查找](#有序列表顺序查找)
* [二分查找](#二分查找)
* [HashTable](#HashTable)

实现展示
------
#### [无序列表顺序查找](sequentialSearch.py)
```Python
# 无序列表顺序查找
>>> from sequentialSearch import sequential_search
>>> test_list = [211, 21, 71, 711, 11]
>>> sequential_search(test_list, 11)
True
```

#### [有序列表顺序查找](orderedSequentialSearch.py)
```Python
# 有序列表顺序查找
>>> from orderedSequentialSearch import ordered_sequential_search
>>> test_list = [11, 21, 71, 211, 711]
>>> ordered_sequential_search(test_list, 271)
False
```

#### [二分查找](binarySearch.py)
```Python
# 二分查找
>>> from binarySearch import binary_search
>>> test_list = [11, 21, 71, 211, 711]
>>> binary_search(test_list, 71)
True
```

#### [HashTable](HashTable.py)
```Python
# HashTable
>>> from HashTable import HashTable
>>> h = HashTable(7)
>>> h[11] = '一'
>>> h[21] = '二'
>>> h[71] = '三'
>>> h[211] = '四'
>>> h[271] = '五'
>>> h[711] = '六'
>>> h.slots
[21, 71, 211, None, 11, 271, 711]
>>> h.data
['二', '三', '四', None, '一', '五', '六']
>>> h[888]
None
>>> h[711]
'六'
>>> h[711] = '七'
>>> h[711]
'七'
>>> h.data
['二', '三', '四', None, '一', '五', '七']
```