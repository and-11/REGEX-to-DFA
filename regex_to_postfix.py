def is_operator(c):
    return c in "*+?|."

def order(op):
    return {
        '*': 3,
        '+': 3,
        '?': 3,
        '.': 2,
        '|': 1
    }.get(op, 0)

def need_dot(prev, curr):
    if prev == '' or prev in '(' or curr == ')' or prev == '|':
        return False
    if curr in '*+?|':
        return False
    return True

def insert_concatenation(regex):
    ans = []
    prev = ''
    for ch in regex:
        if need_dot(prev,ch) :
            ans.append('.')
        ans.append(ch)
        prev = ch
    return ans

def to_postfix(regex):

    regex = insert_concatenation(regex)
    ans = []
    stack = []

    for ch in regex:
        if ch == '(' :
            stack.append( ch )
        elif ch == ')' :
            while stack and stack[-1] != '(' :
                ans.append( stack.pop() )
            stack.pop()
        elif is_operator(ch) :
            while len( stack ) and stack[-1] != '(' and order( stack[-1] ) >= order( ch ) :
                ans.append( stack.pop() )
            stack.append( ch )
        else :
            ans.append( ch )
    while stack :
        ans.append( stack.pop() )

    return ans 

# regex = input()
# postfix = to_postfix(regex)
# print(postfix)