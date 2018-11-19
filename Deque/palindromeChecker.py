from Deque import Deque


def pal_checker(pal_string):
    d = Deque()
    for letter in pal_string:
        d.add_rear(letter)

    equal = True

    while d.size() > 1 and equal:
        if not d.remove_front() == d.remove_rear():
            equal = False

    return equal


print(pal_checker('Shawn2112nwahS'))
print(pal_checker('Deadpool'))
print(pal_checker('Shawn21112nwahS'))
