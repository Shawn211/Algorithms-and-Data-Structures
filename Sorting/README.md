Sorting
======
排序是以某种顺序从集合中放置元素的过程。

示意图
------
冒泡排序：

![冒泡排序](Image/TheBubbleSort.png)

选择排序：

![选择排序](Image/TheSelectionSort.png)

插入排序：

![插入排序](Image/TheInsertionSort.png)

希尔排序：

![希尔排序](Image/TheShellSort.png)

归并排序：

![归并排序](Image/TheMergeSort1.png)

![归并排序](Image/TheMergeSort2.png)

快速排序：

![快速排序](Image/TheQuickSort1.png)

![快速排序](Image/TheQuickSort2.png)

排序实现
------
* [冒泡排序](#冒泡排序)
* [选择排序](#选择排序)
* [插入排序](#插入排序)
* [希尔排序](#希尔排序)
* [归并排序](#归并排序)
* [快速排序](#快速排序)

实现展示
------
#### [冒泡排序](bubbleSort.py)
```Python
# 冒泡排序
>>> from bubbleSort import bubble_sort
>>> test_list = [211, 21, 71, 711, 11]
>>> bubble_sort(test_list)
>>> test_list
[11, 21, 71, 211, 711]
```

#### [选择排序](bubbleSort.py)
```Python
# 选择排序
>>> from selectionSort import selection_sort
>>> test_list = [211, 21, 71, 711, 11]
>>> selection_sort(test_list)
>>> test_list
[11, 21, 71, 211, 711]
```

#### [插入排序](insertionSort.py)
```Python
# 插入排序
>>> from insertionSort import insertion_sort
>>> test_list = [211, 21, 71, 711, 11]
>>> insertion_sort(test_list)
>>> test_list
[11, 21, 71, 211, 711]
```

#### [希尔排序](shellSort.py)
```Python
# 希尔排序
>>> from shellSort import shell_sort
>>> test_list = [211, 21, 71, 711, 11]
>>> shell_sort(test_list)
>>> test_list
[11, 21, 71, 211, 711]
```

#### [归并排序](mergeSort.py)
```Python
# 归并排序
>>> from mergeSort import merge_sort
>>> test_list = [211, 21, 71, 711, 11]
>>> merge_sort(test_list)
>>> test_list
[11, 21, 71, 211, 711]
```

#### [快速排序](quickSort.py)
```Python
# 快速排序
>>> from quickSort import quick_sort
>>> test_list = [211, 21, 71, 711, 11]
>>> quick_sort(test_list)
>>> test_list
[11, 21, 71, 211, 711]
```