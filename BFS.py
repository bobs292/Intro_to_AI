from Graph import Graph

class BFS:
    def __init__(self):
        self.name = "BFS"

        self.found = False
        self.queue = []
        self.path = []

    def search(self, finput, origin, destinations, graph):
        self.finput = finput
        self.destinations = destinations
        self.g = graph

        self.queue.append(origin)

        while(self.found ==False and len(self.queue) > 0):
            self.path.append(self.queue[0])
            self.verify_node(self.queue[0])

            self.queue_edges()
            self.queue.pop(0)

    def queue_edges(self):
        connected = list(self.g.return_edges(self.queue[0]).keys())
        connected.sort()

        for i in connected:
            if i in self.path or i in self.queue:
                connected.remove(i)

        self.queue += connected

    
    def verify_node(self, node):
        if node in self.destinations:
            self.result(node, len(self.path), self.path)
            self.found = True
        
    def result(self, goal, n_nodes, path):
        print(self.finput, self.name)
        print(goal, n_nodes)
        print(path)