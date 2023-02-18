class StackCommon:
    def __init__(self):
        self.stack = []

    def append(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty!')

        return self.stack.pop()

    def get_top_element(self):
        if self.is_empty():
            raise Exception('Stack is empty!')

        return self.stack[-1]

    def is_empty(self) -> bool:
        return True if len(self.stack) == 0 else False
