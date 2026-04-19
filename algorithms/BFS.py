from .Graph import Graph
from .Algorthims import Algorithim

class BFS(Algorithim):
    def __init__(self,current_node, goal_node, name, file_name, graph):
        super().__init__(current_node, goal_node, name,file_name,graph)
        self.queue = []

    def search(self):
        self.queue.append(self.current_node)

        while(self.found ==False and len(self.queue) > 0):
            self.path.append(self.queue[0])
            self.verify_node(self.queue[0])

            self.queue_edges()
            self.queue.pop(0)

    def queue_edges(self):
        connected = list(self.graph.return_edges(self.queue[0]).keys())
        connected.sort()

        for i in connected:
            if i in self.path or i in self.queue:
                connected.remove(i)

        self.queue += connected
        
    