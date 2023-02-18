class DisjointSet:
    parent = []
    rank = []
    size = []
    size_max = 0

    def __init__(self, number_of_tables: int, tables_size: list = None):
        if not tables_size:
            tables_size = [1 for i in range(number_of_tables)]

        if len(tables_size) != number_of_tables:
            raise IOError('Invalid args')

        self.size_max = max(tables_size)

        for i in range(number_of_tables):
            self.parent.append(i)
            self.rank.append(0)
            self.size.append(tables_size[i])

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def is_one_set(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        return True if i_id == j_id else False

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return self.size_max

        if self.rank[i_id] > self.rank[j_id]:
            self.size[i_id] += self.size[j_id]
            self.size_max = max(self.size_max, self.size[i_id])
            self.parent[j_id] = i_id
            return self.size_max
        else:
            self.size[j_id] += self.size[i_id]
            self.size_max = max(self.size_max, self.size[j_id])
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

            return self.size_max
