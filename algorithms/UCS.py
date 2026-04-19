from .Algorthims import Algorithim

class UCS(Algorithim):
    """
    Uniform Cost Search (UCS) algorithm.
    """
    def __init__(self, current_node, goal_node, name, file_name, graph):
        super().__init__(current_node, goal_node, name, file_name, graph)
        
        self.queue = []
        self.parent_map = {self.current_node: None}
        self.costs = {self.current_node: 0}
        self.counter = 0

    def search(self):
        self.queue.append((0, self.current_node, self.counter))
        self.counter += 1

        while not self.found and self.queue:

            current_data = min(self.queue, key=lambda x: (x[0], x[1], x[2]))
            self.queue.remove(current_data)

            current_cost, node_id, _ = current_data

            if node_id in self.goal_node:
                self.reconstruct_path(node_id)
                self.result()
                self.found = True
                break

            self.queue_edges(node_id, current_cost)

    def queue_edges(self, node_id, current_cost):
        connected = self.graph.return_edges(node_id)

        for child, edge_cost in connected.items():
            child = int(child)
            new_total_cost = current_cost + int(edge_cost)

            if child not in self.costs or new_total_cost < self.costs[child]:
                self.costs[child] = new_total_cost
                self.parent_map[child] = node_id
                self.queue.append((new_total_cost, child, self.counter))
                self.counter += 1
                self.nodes_created += 1

    def reconstruct_path(self, goal_node):
            finalized_path = []
            curr = goal_node
            while curr is not None:
                finalized_path.append(curr)
                curr = self.parent_map.get(curr)
            
            finalized_path.reverse()
            self.path = finalized_path