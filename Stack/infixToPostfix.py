from Stack import Stack


def infix_to_postfix(infix_expr):
    precedence = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
    }
    s = Stack()
    postfix_list = []

    for symbol in infix_expr:
        if symbol in '0123456789' or symbol in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            postfix_list.append(symbol)
        else:
            if symbol == '(':
                s.push(symbol)
            elif symbol == ')':
                while s.peek() != '(':
                    postfix_list.append(s.pop())
                s.pop()
            elif symbol in precedence.keys():
                if s.is_empty():
                    s.push(symbol)
                elif precedence[s.peek()] < precedence[symbol]:
                    s.push(symbol)
                else:
                    while not s.is_empty() and precedence[s.peek()] >= precedence[symbol]:
                        postfix_list.append(s.pop())
                    s.push(symbol)

    while not s.is_empty():
        postfix_list.append(s.pop())

    return ''.join(postfix_list)


print(infix_to_postfix('A + B * C'))
print(infix_to_postfix('A * B + C'))
print(infix_to_postfix('A + B * C + D'))
print(infix_to_postfix('A * B + C * D'))
print(infix_to_postfix('(A + B) * (C + D)'))
print(infix_to_postfix('A * (B + C) * D'))
