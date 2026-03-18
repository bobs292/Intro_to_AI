import sys
from BFS import BFS
from Graph import Graph

def parse_input(finput):
    graph = Graph()
    with open(finput, 'r') as file:
        f = file.read().split('\n')

        if f[0] != "Nodes:":
            print("Invalid file.")

        origin = f[-4]
        destinations = f[-2].split('; ')

        for i in range(1, len(f) - 6):
            if f[i] == "Edges:":
                edg = i+1
                break

            l = [char for char in f[i] if char.isdigit()]
            graph.add_node(l[1], l[2])

        for i in range(edg, len(f) - 6):
            l = [char for char in f[i] if char.isdigit()]
            graph.add_edge(l[0], l[1], l[2])

    file.close()
    return origin, destinations, graph


if __name__ == "__main__":
    if len(sys.argv) > 2:
        finput = sys.argv[1]
        method = sys.argv[2]

        origin, destinations, graph = parse_input(sys.argv[1])

        if sys.argv[2] == "BFS":
            alg = BFS()

        alg.search(sys.argv[1], origin, destinations, graph)

    else:
        print("Invalid Arguments")