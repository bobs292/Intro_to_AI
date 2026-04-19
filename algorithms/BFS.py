from .Graph import Graph
from .Algorthims import Algorithim

class BFS(Algorithim):
    def __init__(self,current_node, goal_node, name, file_name, graph):
        super().__init__(current_node, goal_node, name,file_name,graph)
        self.queue = []
        self.parent_map = {self.current_node: None}

    def search(self):
        self.queue.append(self.current_node)

        while not self.found and len(self.queue) > 0:
            current = self.queue.pop(0)
            
            if current in self.goal_node:
                self.reconstruct_path(current)
                self.result()
                self.found = True

            self.queue_edges(current)

    def queue_edges(self, current):
        connected = list(self.graph.return_edges(current).keys())
        connected.sort()

        for neighbor in connected:
            if neighbor not in self.parent_map:
                self.parent_map[neighbor] = current
                self.queue.append(neighbor)

    def reconstruct_path(self, goal_node):
        finalized_path = []
        curr = goal_node
        
        while curr is not None:
            finalized_path.append(curr)
            curr = self.parent_map[curr]

        finalized_path.reverse()

        self.path = finalized_path
        
    