from stack_with_max_support import StackMaxSupport

stack_max_support = StackMaxSupport()

n = int(input())
for _ in range(n):
    '''
    Commands:
    push [int] - push value in the stack
    pop - return the value at the top of the stack
    max - print maximum value in the stack
    '''

    query = input().split()
    command = query[0]
    if command == 'push':
        if len(query) == 2 and query[1].isdigit():
            stack_max_support.push(query[1])
        else:
            raise IOError(f'Invalid format push\nWas: {command}, but expected: push [int]')
    elif command == 'pop':
        stack_max_support.pop()
    elif command == 'max':
        stack_max_support.print_max()
    else:
        raise IOError(f'Unknown command')
