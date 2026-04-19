from .Graph import Graph
from .Algorithm import Algorithm

class DFS(Algorithm):
    def __init__(self, current_node, goal_nodes, name, file_name, graph):
        super().__init__(current_node, goal_nodes, name, file_name, graph)
        self.visited = set()

    def search(self):
        self.DFSUtil(self.current_node)

    def DFSUtil(self, node):
        if self.found:
            return

        self.visited.add(node)
        self.path.append(node)

        self.verify_node(node)

        if self.found:
            return

        connected = list(self.graph.return_edges(node).keys())
        connected.sort()

        for neighbour in connected:
            if neighbour not in self.visited:
                self.DFSUtil(neighbour)