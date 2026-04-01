from .Algorthims import Algorithim

class UCS(Algorithim):
    def __init__(self, current_node, goal_node, name, file_name, graph):
        super().__init__(current_node, goal_node, name, file_name, graph)
        
        self.queue = []
        self.path = []

        self.costs = {}

    def search(self):
        self.queue.append((self.current_node, 0))

        while(self.found == False and len(self.queue) > 0):

            self.current_node = min(self.queue, key=lambda x: x[1])
            self.queue.remove(self.current_node)

            self.path.append(self.current_node[0])
            self.verify_node(self.current_node[0])
            self.queue_edges()

    def queue_edges(self):
        connected = self.graph.return_edges(self.current_node[0])

        for child, cost in connected.items():
            if child in self.path:
                continue

            t_cost = self.current_node[1] + int(cost)

            if child not in self.costs or t_cost < self.costs[child]:
                self.costs[child] = t_cost

                self.queue.append((child, t_cost))