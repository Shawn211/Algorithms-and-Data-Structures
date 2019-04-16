Algorithms-and-Data-Structures
======
基于 Python 轻松实现基础的算法与数据结构。

******
|Author|Repository|
|:---:|:---:
|Shawn211|[Algorithms-and-Data-Structures](https://github.com/Shawn211/Algorithms-and-Data-Structures)

******
## 目录
* 数据结构
   * [Stack：栈](#Stack-栈)
   * [Queue：队列](#Queue-队列)
   * [Deque：双端队列](#Deque-双端队列)
   * [LinkedList：链表](#LinkedList-链表)
   * [Tree：树](#Tree-树)
   * [Graph：图](#Graph-图)
* 算法
   * [Recursion：递归](#Recursion-递归)
   * [Searching：查找](#Searching-查找)
   * [Sorting：排序](#Sorting-排序)

******
[Stack 栈](Stack/README.md)
------
* 基本概念
* 栈的操作
   * push(item)
   * pop()
   * peek()
   * is_empty()
   * size()
* 栈的实现
* 实际应用
   * 小括号匹配
   * 多种括号匹配
   * 十进制转换二进制
   * 十进制转换任意进制
   * 中缀表达式转后缀
   * 后缀表达式求值
* 应用展示

******
[Queue 队列](Queue/README.md)
------
* 基本概念
* 队列操作
   * enqueue(item)
   * dequeue()
   * is_empty()
   * size()
* 队列实现
* 实际应用
   * 约瑟夫斯置换
* 应用展示

******
[Deque 双端队列](Deque/README.md)
------
* 基本概念
* Deque操作
   * add_front(item)
   * add_rear(item)
   * remove_front()
   * remove_rear()
   * is_empty()
   * size()
* Deque实现
* 实际应用
   * 回文检查
* 应用展示

******
[LinkedList 链表](LinkedList/README.md)
------
* 基本概念
* 链表操作
   * 无序链表
      * add(item)
      * remove(item)
      * append(item)
      * pop()
      * insert(pos, item)
      * pop(pos)
      * search(item)
      * index(item)
      * is_empty()
      * size()
   * 有序列表
      * add(item)
      * remove(item)
      * pop()
      * pop(pos)
      * search(item)
      * index(item)
      * is_empty()
      * size()
* 链表实现
   * 无序链表
   * 有序列表
* 实现展示

******
[Tree 树](Tree/README.md)
------
* 基本概念
* 二叉树操作
   * insert_left(new_node)
   * insert_right(new_node)
   * get_left_child()
   * get_right_child()
   * set_root_value(new_value)
   * get_root_value()
* 二叉堆操作
   * 最小堆
      * insert(value)
      * find_min()
      * del_min()
      * is_empty()
      * size()
      * build_heap(list)
   * 最大堆
      * insert(value)
      * find_max()
      * del_max()
      * is_empty()
      * size()
      * build_heap(list)
* 二叉查找树操作
   * put(key, value)
   * get(key)
   * del
   * len()
   * in
* 树实现
   * 二叉树
      * 列表表示
      * 节点表示
   * 二叉堆
   * 二叉查找树
   * AVL平衡二叉查找树
* 实际应用
   * 分析树
   * 树的遍历
   * 二叉堆排序
* 实现展示

******
[Graph 图](Graph/README.md)
------
* 基本概念
* 图操作
   * add_vertex(key)
   * add_edge(from_key, to_key)
   * add_edge(from_key, to_key, weight)
   * get_vertex(key)
   * get_vertices()
   * in
* 图实现
* 实际应用
   * 构建字梯图
   * 广度优先搜索
   * 构建骑士游历图
   * 骑士游历
   * 深度优先搜索
   * 拓扑排序
   * 强连通分量
* 应用展示

******
[Recursion 递归](Recursion/README.md)
------
* 基本概念
* 递归三定律
* 实际应用
   * 计算整数列表和
   * 十进制转换任意进制字符串
   * 可视化递归
      * 螺旋
      * 分形树
      * 谢尔宾斯基三角形
   * 汉诺塔
   * 找零
* 应用展示

******
[Searching 查找](Searching/README.md)
------
* 基本概念
* 查找实现
   * 顺序查找
      * 无序列表顺序查找
      * 有序列表顺序查找
   * 二分查找
   * HashTable
* 实现展示

******
[Sorting 排序](Sorting/README.md)
------
* 基本概念
* 排序实现
   * 冒泡排序
   * 选择排序
   * 插入排序
   * 希尔排序
   * 归并排序
   * 快速排序
* 实现展示

******
推荐书籍
------
* [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html)
* [Problem Solving with Algorithms and Data Structures using Python (中文版)](https://facert.gitbooks.io/python-data-structure-cn/)