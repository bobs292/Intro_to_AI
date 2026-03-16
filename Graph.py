class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = {}

    def add_node(self,u,v):
        key_num = len(list(self.nodes.keys())) + 1
        self.nodes[key_num] = [u,v]

    def add_edge(self,u,v, weight):
        if u in self.graph:
            self.graph[u][v] = weight
        else:
            self.graph[u] = {v: weight}
        if v in self.graph:
            self.graph[v][u] = weight
        else:
            self.graph[v] = {u: weight}