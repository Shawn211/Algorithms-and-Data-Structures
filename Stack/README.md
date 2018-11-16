Stack
======
栈，是一个项的有序集合。其中添加移除新项总发生在同一端，这一端通常称为“顶部”，与顶部对应的端称为“底部”。最近添加的项是最先会被移除的，这种排序原则被称为 LIFO，后进先出。

示意图
------
![](image/simplereversal.png)

栈操作
------
* push(item) 添加新项到栈的顶部。item 做参数并不返回任何内容。
* pop() 删除栈的顶部第一个项。不需要参数并返回该项。
* peek() 从栈的顶部返回第一个项，并不删除该项。
* is_empty() 判断栈是否为空，并返回布尔值。
* size() 返回栈中项的数量。

栈的实现
------
* [Stack](Stack.py)

实际应用
------
* [小括号匹配](#小括号匹配)
* [多种括号匹配](#多种括号匹配)
* [十进制转换二进制](#十进制转换二进制)
* [十进制转换任意进制](#十进制转换任意进制)
* [中缀表达式转后缀](#中缀表达式转后缀)

应用展示
------
#### [小括号匹配](simpleBalancedParentheses.py)
```Python
# 小括号匹配
>>> from simpleBalancedParentheses import parentheses_check
>>> parentheses_check('(()())')
True
>>> parentheses_check(')()()(')
False
>>> parentheses_check('(--(--')
False
>>> parentheses_check('*()()*')
True
```

#### [多种括号匹配](balancedSymbols.py)
```Python
# 多种括号匹配
>>> from balancedSymbols import parentheses_check
>>> parentheses_check('{[()()]}')
True
>>> parentheses_check('}{][][)(')
False
>>> parentheses_check('*([)(])*')
False
>>> parentheses_check('(-{}{}-)')
True
```

#### [十进制转换二进制](decimalToBinary.py)
```Python
# 十进制转换二进制
>>> from decimalToBinary import binary_converter
>>> binary_converter(1)
'1'
>>> binary_converter(21)
'10101'
>>> binary_converter(211)
'11010011'
```

#### [十进制转换任意进制](decimalToAnyBase.py)
```Python
# 十进制转换任意进制
>>> from decimalToAnyBase import base_converter
>>> base_converter(211, 2)
'11010011'
>>> base_converter(211, 8)
'323'
>>> base_converter(211, 16)
'D3'
```

#### [中缀表达式转后缀](infixToPostfix.py)
```Python
# 中缀表达式转后缀
>>> from infixToPostfix import infix_to_postfix
>>> infix_to_postfix('A + B * C')
'ABC*+'
>>> infix_to_postfix('A * B + C')
'AB*C+'
>>> infix_to_postfix('A + B * C + D')
'ABC*+D+'
>>> infix_to_postfix('A * B + C * D')
'AB*CD*+'
>>> infix_to_postfix('(A + B) * (C + D)')
'AB+CD+*'
>>> infix_to_postfix('A * (B + C) * D')
'ABC+*D*'
```