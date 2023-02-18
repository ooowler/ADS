from stack_common import StackCommon

a = input()


def check_str(string: str):
    parenthesis = '(){}[]'
    valid_parenthesis = {')': '(',
                         ']': '[',
                         '}': '{'}
    stack = StackCommon()
    for i, elem in enumerate(string):
        if elem not in parenthesis:
            continue

        if elem in valid_parenthesis.values():
            stack.append((elem, i))
        else:
            if stack.is_empty():
                return i + 1

            if valid_parenthesis[elem] == stack.get_top_element()[0]:
                stack.pop()
            else:
                return i + 1

    return 'Success' if stack.is_empty() else stack.get_top_element()[1] + 1


print(check_str(a))
