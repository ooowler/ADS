from MinHeap import MinHeap


class MinHeapLists(MinHeap):
    def get_value_to_compare(self, index):
        return self.nodes[index][0]

    def check_node(self, node_index):
        node_value = self.get_value_to_compare(node_index)
        process_node = self.nodes[node_index][1]

        left_index = self.get_left_child_index(node_index)
        right_index = self.get_right_child_index(node_index)

        if left_index and right_index:
            left_value = self.get_value_to_compare(left_index)
            right_value = self.get_value_to_compare(right_index)

            process_left = self.nodes[left_index][1]
            process_right = self.nodes[right_index][1]

            min_value = min(left_value, right_value)

            if node_value == min_value:
                process_min = min(process_right, process_left)
                if process_node > process_min:
                    if process_left == process_min:
                        self.nodes_swap(node_index, left_index)
                        self.check_node(left_index)
                    elif process_right == process_min:
                        self.nodes_swap(node_index, right_index)
                        self.check_node(right_index)

            if node_value > min_value:
                process_left_id = self.nodes[left_index][1]
                process_right_id = self.nodes[right_index][1]

                if left_value == right_value == min_value:
                    process_min_id = min(process_left_id, process_right_id)
                    if process_min_id == process_left_id:
                        self.nodes_swap(node_index, left_index)
                        self.check_node(left_index)
                    else:
                        self.nodes_swap(node_index, right_index)
                        self.check_node(right_index)

                elif left_value == min_value:
                    self.nodes_swap(node_index, left_index)
                    self.check_node(left_index)
                else:
                    self.nodes_swap(node_index, right_index)
                    self.check_node(right_index)

        elif left_index and not right_index:
            process_left = self.nodes[left_index][1]
            left_value = self.get_value_to_compare(left_index)

            if node_value == left_value:
                if process_node > process_left:
                    self.nodes_swap(node_index, left_index)
                    self.check_node(left_index)

            if node_value > left_value:
                self.nodes_swap(node_index, left_index)
                self.check_node(left_index)

        elif not left_index and right_index:
            process_right = self.nodes[right_index][1]
            right_value = self.get_value_to_compare(right_index)

            if node_value == right_value:
                if process_node > process_right:
                    self.nodes_swap(node_index, right_index)
                    self.check_node(right_index)

            if node_value > right_value:
                self.nodes_swap(node_index, right_value)
                self.check_node(right_value)
        else:
            return


processors, len_requests = map(int, input().split())
requests = list(map(int, input().split()))

processors_list = [(0, processor) for processor in range(processors)]
heap = MinHeapLists(processors, processors_list)
heap.sort_heap()
for request in requests:
    t, processor = heap.get_top_node()
    print(processor, t)
    t += request
    heap.set_top_node((t, processor))
    heap.check_top_node()
