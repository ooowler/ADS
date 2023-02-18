class StackMaxSupport:
    def __init__(self):
        self.stack = []
        self.stack_max = []
        self.length = 0

    def push(self, value):
        self.stack.append(value)

        if len(self.stack_max) == 0:
            self.stack_max.append(value)
        else:
            if value >= self.stack_max[-1]:
                self.stack_max.append(value)
            else:
                self.stack_max.append(self.stack_max[-1])

        self.length += 1

    def pop(self):
        if len(self.stack) == 0:
            raise Exception('Stack is empty')

        self.stack.pop(-1)
        self.stack_max.pop(-1)
        self.length -= 1

    def is_empty(self):
        return True if self.length == 0 else False

    def get_length(self):
        return self.length

    def get_max_elem(self):
        if self.is_empty():
            return

        return self.stack_max[-1]

    def print_max(self):
        print(self.stack_max[-1]) if len(self.stack_max) > 0 else print(0)
