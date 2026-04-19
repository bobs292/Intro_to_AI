from .Algorthims import Algorithim

class UCS(Algorithim):
    def __init__(self, current_node, goal_node, name, file_name, graph):
        super().__init__(current_node, goal_node, name, file_name, graph)
        
        self.queue = []
        self.parent_map = {self.current_node: None}
        self.costs = {self.current_node: 0}

    def search(self):
        self.queue.append((self.current_node, 0))

        while not self.found and len(self.queue) > 0:

            current_data = min(self.queue, key=lambda x: x[1])
            self.queue.remove(current_data)

            node_id, current_cost = current_data

            if node_id in self.goal_node:
                self._reconstruct_path(node_id)

            if self.found:
                break

            self.queue_edges(node_id, current_cost)

    def queue_edges(self, node_id, current_cost):
        connected = self.graph.return_edges(node_id)

        for child, edge_cost in connected.items():
            new_total_cost = current_cost + int(edge_cost)

            if child not in self.costs or new_total_cost < self.costs[child]:
                self.costs[child] = new_total_cost
                self.parent_map[child] = node_id
                self.queue.append((child, new_total_cost))

    def _reconstruct_path(self, goal_node):
            finalized_path = []
            curr = goal_node
            while curr is not None:
                finalized_path.append(curr)
                curr = self.parent_map.get(curr)
            
            finalized_path.reverse()
            self.path = finalized_path