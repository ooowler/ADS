from collections import deque
from stack_with_max_support import StackMaxSupport


def swap_stacks(stack1, stack2):
    tmp_max_stack_out = stack1[-1][0]
    while stack1:
        elem = stack1.pop()
        tmp_max_stack_out = max(tmp_max_stack_out, elem[0])
        stack2.append((elem[0], tmp_max_stack_out))

    print(stack2.pop()[1], end=' ')


def solution(n: int, nums: list, k: int):
    if n == k:
        print(max(nums))
        return

    if k == 1:
        print(*nums)
        return

    tmp_max = nums[0]
    stack_in = deque()  # O(1) pop
    stack_out = deque()  # O(1) pop
    i = 0
    while i < n:
        if len(stack_in) == 0 and len(stack_out) == 0:
            tmp_max = nums[i]
            while len(stack_in) != k:
                tmp_max = max(tmp_max, nums[i])
                stack_in.append((nums[i], tmp_max))
                i += 1

            swap_stacks(stack_in, stack_out)
            tmp_max = 0

        if len(stack_in) == k - 1 and len(stack_out) == 0:
            stack_in.append((nums[i], tmp_max))
            swap_stacks(stack_in, stack_out)
            tmp_max = 0
            i += 1
            continue

        tmp_max = max(tmp_max, nums[i])
        stack_in.append((nums[i], tmp_max))
        stack_pop_elem = stack_out.pop()
        print(max(stack_in[-1][1], stack_pop_elem[1]), end=' ')

        i += 1


n = int(input())
nums = list(map(int, input().split()))
k = int(input())

# 8
# 2 7 3 1 5 2 6 2
# 4

solution(n, nums, k)
