from DisjointSet import DisjointSet

table_count, requests = map(int, input().split())
tables_size = list(map(int, input().split()))

dis_joint_set = DisjointSet(table_count, tables_size)
for i in range(requests):
    destination, source = map(int, input().split())
    destination -= 1
    source -= 1
    size = dis_joint_set.union(destination, source)
    print(size)
