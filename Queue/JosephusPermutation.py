from Queue import Queue


def permutation(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num - 1):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


print(permutation([num for num in range(1, 6)], 11))
print(permutation([num for num in range(1, 21)], 71))
print(permutation(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 11))
