class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = {}

    def add_node(self,u,v):

        key = len(self.nodes) + 1

        self.nodes[key] = (float(u), float(v))

        if key not in self.graph:
            self.graph[key] = {}

    def add_edge(self,u,v, weight):
        if u in self.graph:
            self.graph[u][v] = float(weight)
        else:
            self.graph[u] = {v: float(weight)}

    def return_edges(self, key):
        if self.graph[key] is None:
            return None
        return self.graph[key]
        
    def print_graph(self):
        print("Nodes:")
        x = 1
        for i in self.nodes.values():
            print(str(x) + ". ", i[0], i[1])
            x += 1
        
        print("Edges:")
        x = 1
        for key, value in self.graph.items():
            for k, v in value.items():
                print(str(x) + ". ", key, k, v)
                x +=1