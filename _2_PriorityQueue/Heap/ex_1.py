from MinHeap import MinHeap
from MaxHeap import MaxHeap

length = int(input())
array_read = (list(map(int, input().split())))
heap_min = MaxHeap(length, array_read)


def solution(heap):
    changes = heap.sort_heap()

    if not changes:
        print(0)
    else:
        print(len(changes))
        for elem in changes:
            print(elem[0], elem[1])


solution(heap_min)