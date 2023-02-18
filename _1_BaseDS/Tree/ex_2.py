import sys
from Tree import Tree

sys.setrecursionlimit(20000)

n = int(input())
nodes = list(map(int, input().split()))

tree = Tree(nodes)
print(tree.get_height())
