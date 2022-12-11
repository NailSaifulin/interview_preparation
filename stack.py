class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return bool(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return 'stack is empty'

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return 'stack is empty'

    def size(self):
        return len(self.stack)


def balance_bkt(parentheses):
    equality = {'(': ')',
                '[': ']',
                '{': '}'}
    open_bracket = ('(', '[', '{')
    close_bracket = (')', ']', '}')
    balance = Stack()
    for iter in list(parentheses):
        if iter in open_bracket:
            balance.push(iter)
        elif iter in close_bracket and balance.is_empty() is False:
            return 'Несбалансированно'
        elif iter in close_bracket and equality[balance.peek()] == iter:
            balance.pop()
        else:
            return 'Несбалансированно'

    if balance.is_empty() is False:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    print(balance_bkt('{(())'))
