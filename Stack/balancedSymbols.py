from Stack import Stack


def parentheses_check(par_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(par_string) and balanced:
        if par_string[index] in '{[(':
            s.push(par_string[index])
        elif par_string[index] in '}])':
            if s.is_empty():
                balanced = False
            else:
                symbol = s.pop()
                if not matches(symbol, par_string[index]):
                    balanced = False
        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


def matches(left, right):
    lefts = '{[('
    rights = '}])'
    return lefts.index(left) == rights.index(right)


print(parentheses_check('{[()()]}'))
print(parentheses_check('}{][][)('))
print(parentheses_check('*([)(])*'))
print(parentheses_check('(-{}{}-)'))
