from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    """
        Design a stack that includes a max operation, in addition to push and pop.
        The max method should return the maximum value stored in the stack.

        Have:
            * Four methods and their definitions:
                empty
                max
                pop
                push

        Logic:
            * empty:
                Create length attribute, reference and use implicit boolean.
            * max:
                Create a second stack attr to keep track of max of each state
                    in stack.
            * pop:
                Built in list type pop method, i.e. pop() for main stack.
                We'll also pop from max stack attr to keep consistent state.
            * push:
                Build in list type append method, for main stack.
                We'll also append the max of current value and latest max stack value.
    """
    def __init__(self) -> None:
        self.main_stack = []
        self.max_stack = []
        self.length = 0
        
    def empty(self) -> bool:
        return False if self.length else True

    def max(self) -> int:
        return self.max_stack[-1]

    def pop(self) -> int:
        result = self.main_stack.pop()
        _ = self.max_stack.pop()
        self.length -= 1
        return result

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        self.length += 1
        try:
            new_max = max(self.max_stack[-1], x)
            self.max_stack.append(new_max)
        except IndexError:
            self.max_stack.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
