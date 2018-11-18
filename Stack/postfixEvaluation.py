from Stack import Stack


def postfix_eval(postfix_expr):
    s = Stack()
    for symbol in postfix_expr:
        if symbol in '0123456789':
            s.push(int(symbol))
        else:
            operands2 = s.pop()
            operands1 = s.pop()
            result = do_math(symbol, operands1, operands2)
            s.push(result)
    return s.pop()


def do_math(operator, operands1, operands2):
    if operator == '*':
        return operands1 * operands2
    elif operator == '/':
        return operands1 / operands2
    elif operator == '+':
        return operands1 + operands2
    elif operator == '-':
        return operands1 - operands2


print(postfix_eval('11+'))
print(postfix_eval('21*21--'))
print(postfix_eval('21/21*/'))
