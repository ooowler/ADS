class Tree:
    def __init__(self, nodes: list):
        self.n = len(nodes)
        self.children = {}
        self.nodes = nodes

        for index, node in enumerate(nodes):
            if node in self.children:
                self.children[node].append(index)
            else:
                self.children[node] = [index]

        self.root = self.get_parent_value()

    def get_children_list(self, parent: int) -> list:
        if parent in self.children:
            return self.children[parent]
        else:
            return []

    def get_parent(self, kid):
        if kid < self.n:
            return self.nodes[kid]
        else:
            raise Exception('index out of range')

    def get_parent_value(self):
        root = self.get_children_list(-1)
        if not root:
            raise IOError('No root in Tree')

        if len(root) != 1:
            raise IOError('Too many roots')

        return root[0]

    def get_height(self, parent=-1):
        height = 1

        if parent == -1:
            children = self.get_children_list(self.root)
        else:
            children = self.get_children_list(parent)

        for kid in children:
            height = max(height, 1 + self.get_height(kid))

        return height


example_tree = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
# example_tree = [-1, 0, 4, 0, 3]

some_tree = Tree(example_tree)
print(some_tree.get_height())
