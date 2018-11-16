from Stack import Stack


def parentheses_check(par_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(par_string) and balanced:
        if par_string[index] == '(':
            s.push(par_string[index])
        elif par_string[index] == ')':
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


print(parentheses_check('(()())'))
print(parentheses_check(')()()('))
print(parentheses_check('(--(--'))
print(parentheses_check('*()()*'))
