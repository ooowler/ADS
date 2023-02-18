class MinHeap:
    def __init__(self, n: int, array: list):
        self.changes = []
        self.n = n
        self.nodes = array

    def get_top_node(self):
        i = 0
        if self.__check_node_exists(i):
            return self.nodes[i]

    def set_top_node(self, node):
        self.nodes[0] = node

    def get_value_to_compare(self, index):
        return self.nodes[index]

    def __check_node_exists(self, index) -> bool:
        return True if index < self.n else False

    def get_parent_index(self, index):
        parent_index = (index - 1) // 2
        if self.__check_node_exists(parent_index):
            return parent_index

        return

    def get_left_child_index(self, parent_index):
        left_child_index = 2 * parent_index + 1
        if self.__check_node_exists(left_child_index):
            return left_child_index

        return

    def get_right_child_index(self, parent_index):
        right_child_index = 2 * parent_index + 2
        if self.__check_node_exists(right_child_index):
            return right_child_index

        return

    def nodes_swap(self, index1, index2):
        if self.__check_node_exists(index1) and self.__check_node_exists(index2):
            self.nodes[index1], self.nodes[index2] = self.nodes[index2], self.nodes[index1]
            self.changes.append((index1, index2))

        return

    def check_node(self, node_index):
        node_value = self.get_value_to_compare(node_index)

        left_index = self.get_left_child_index(node_index)
        right_index = self.get_right_child_index(node_index)

        if left_index and right_index:
            left_value = self.get_value_to_compare(left_index)
            right_value = self.get_value_to_compare(right_index)

            min_value = min(left_value, right_value)

            if node_value > min_value:
                if left_value == min_value:
                    self.nodes_swap(node_index, left_index)
                    self.check_node(left_index)
                else:
                    self.nodes_swap(node_index, right_index)
                    self.check_node(right_index)

        elif left_index and not right_index:
            left_value = self.get_value_to_compare(left_index)
            if node_value > left_value:
                self.nodes_swap(node_index, left_index)
                self.check_node(left_index)

        elif not left_index and right_index:
            right_value = self.get_value_to_compare(right_index)
            if node_value > right_value:
                self.nodes_swap(node_index, right_value)
                self.check_node(right_value)
        else:
            return

    def check_top_node(self):
        self.check_node(0)

    def sort_heap(self):
        index = self.n - 1
        while index >= 0:
            self.check_node(index)
            index -= 1

        return self.changes

    def print_changes(self):
        for change in self.changes:
            print(change[0], change[1])

    def print_heap(self):
        for elem in self.nodes:
            print(elem)
