from DisjointSet import DisjointSet


def solution():
    n, e, d = map(int, input().split())
    dis_joint_set = DisjointSet(n)

    for _ in range(e):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        dis_joint_set.union(i, j)

    for _ in range(d):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        if dis_joint_set.is_one_set(i, j):
            return 0

    return 1


print(solution())

# 4 6 0
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4


# x1 x2 x3 x4
# 1  1  -  -
# 1  1  1  -
# 1  1  1  1
# -  -  -  -
# -  -  -  -
# -  -  -  -
