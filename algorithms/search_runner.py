import sys
from .BFS import BFS
from .UCS import UCS
from .Greed import Greed
from .AS import AS
from .DFS import DFS
from .Beam import Beam
from .Graph import Graph
from .GUI import draw_graph
from .GUI import draw_path

def parse_input(finput):
    graph = Graph()
    with open(finput, 'r') as file:
        f = file.read().split('\n')

        if f[0] != "Nodes:":
            raise ValueError("Invalid file: File must start with 'Nodes:'")

        origin = f[-4]
        print(f[-2])
        destinations = [int(x) for x in f[-2].strip().split('; ')]
        print(destinations)
        for i in range(1, len(f) - 6):
            if f[i] == "Edges:":
                edg = i+1
                break

            parts = f[i].split(':')

            coords = parts[1].strip().strip('()').split(',')
            x = coords[0]
            y = coords[1]

            graph.add_node(x, y)

        for i in range(edg, len(f) - 6):
            parts = f[i].split(':')
            weight = int(parts[1].strip())

            nodes = parts[0].strip().strip('()').split(',')
            n1 = nodes[0]
            n2 = nodes[1]

            graph.add_edge(n1, n2, weight)

    file.close()
    return origin, destinations, graph

def run_algorithm(finput, method):
    origin, destinations, graph = parse_input(finput)

    match method.lower():
        case "bfs":
            alg = BFS(origin, destinations, "BFS", finput, graph)
        case "dfs":
            alg = DFS(origin, destinations, "DFS", finput, graph)
        case "greed":
            alg = Greed(origin, destinations, "Greed first search", finput, graph)
        case "ucs":
            alg = UCS(origin, destinations, "UCS", finput, graph)
        case "as":
            alg = AS(origin, destinations, "A*", finput, graph)
        case "beam":
            alg = Beam(origin, destinations, "Beam Search", finput, graph)
        case _:
            return print("Unknown Algorithm")
 
    alg.search()
    draw_graph(graph)
    draw_path(alg, graph)