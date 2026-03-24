from Graph import Graph

#TODO comments, unsure if its required in the rubric, but ill probably add some in later <3

class DFS:
    def __init__(self):
        self.name = "DFS"

        self.found = False
        self.path = []
        self.visited = set()

    def search(self, finput, origin, destinations, graph):
        self.finput = finput
        self.destinations = destinations
        self.g = graph

        self.DFSUtil(origin)

    def DFSUtil(self, node):
        if self.found:
            return

        self.visited.add(node)
        self.path.append(node)

        self.verify_node(node)

        if self.found:
            return

        connected = list(self.g.return_edges(node).keys())
        connected.sort()

        for neighbour in connected:
            if neighbour not in self.visited:
                self.DFSUtil(neighbour)

    def verify_node(self, node):
        if node in self.destinations:
            self.result(node, len(self.path), self.path)
            self.found = True

    def result(self, goal, n_nodes, path):
        print(self.finput, self.name)
        print(goal, n_nodes)
        print(path)