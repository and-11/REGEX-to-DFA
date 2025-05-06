def is_operator(c):
    return c in {'*', '+', '?', '|', '.'}

def precedence(op):
    return {
        '*': 3,
        '+': 3,
        '?': 3,
        '.': 2,
        '|': 1
    }.get(op, 0)

def needs_concat(prev, curr):
    if prev == '' or prev == '(' or curr == ')' or curr == '|':
        return False
    if curr in '*+?':
        return False
    return True

def insert_concatenation(regex):
    result = []
    prev = ''
    for c in regex:
        if needs_concat(prev, c):
            result.append('.')
        result.append(c)
        prev = c
    return ''.join(result)

def to_postfix(regex):
    regex = insert_concatenation(regex)
    output = []
    stack = []

    for c in regex:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # scoate '('
        elif is_operator(c):
            while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(c):
                output.append(stack.pop())
            stack.append(c)
        else:
            output.append(c)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


# regex = input()
# postfix = to_postfix(regex)
# print(postfix)