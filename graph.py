class Graph:
    def __init__(self):
        self.graph = {}
        

    def add_edge(self,u,v, distance):
        if u in self.graph:
            self.graph[u][v] = distance
        else:
            self.graph[u] = {v: distance}
        if v in self.graph:
            self.graph[v][u] = distance
        else:
            self.graph[v] = {u: distance}
        

    def print_graph(self):
        #Remove or edit AI generatated and poorly done.
        if not self.graph:
            print("Graph is empty")
            return

        nodes = sorted(self.graph.keys())
        print("Adjacency list (node: neighbor(weight))")
        for u in nodes:
            neighbors = self.graph[u]
            items = sorted(neighbors.items())
            line = ", ".join(f"{v}({w})" for v, w in items)
            print(f"{u}: {line}")

        print("\nAdjacency matrix (0 = no edge)")
        header = "    " + " ".join(f"{n:>3}" for n in nodes)
        print(header)
        for u in nodes:
            row = [f"{self.graph[u].get(v, 0):>3}" for v in nodes]
            print(f"{u:>3} " + " ".join(row))

def main():
    mat = Graph()
    mat.add_edge(0,2,4)
    mat.add_edge(4,2,6)
    mat.add_edge(0,3,2)
    mat.add_edge(4,0,1)
    mat.add_edge(1,2,6)
    mat.print_graph()


main()
