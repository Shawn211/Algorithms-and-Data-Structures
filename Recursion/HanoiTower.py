class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


from_pole_stack = Stack()
to_pole_stack = Stack()
with_pole_stack = Stack()
s = dict()
s[str(from_pole_stack)] = 'FromPole'
s[str(to_pole_stack)] = 'ToPole'
s[str(with_pole_stack)] = 'WithPole'


def move_tower(height, from_pole, to_pole, with_pole):
    if height > 0:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    disk = fp.pop()
    tp.push(disk)
    print(f'moving "{disk}" from {s[str(fp)]} to {s[str(tp)]}')


def hanoi_tower(num):
    disks_num = num
    disks = [str(i) for i in range(1, disks_num+1)]
    disks.reverse()
    for disk in disks:
        from_pole_stack.push(disk)

    move_tower(disks_num, from_pole_stack, to_pole_stack, with_pole_stack)


def main():
    hanoi_tower(6)


if __name__ == '__main__':
    main()
