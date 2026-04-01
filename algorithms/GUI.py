import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import math
from Graph import Graph

fig, ax = None, None

def draw():
    global fig, ax
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')

def draw_node(x, y, label):
    circle = Circle((x, y), radius=0.4, edgecolor='black', facecolor='lightblue', zorder=3)
    ax.add_patch(circle)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, zorder=4)

def draw_edge(x1, y1, x2, y2, weight):
    ax.plot([x1, x2], [y1, y2], 'k-', zorder=1)
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    ax.text(mid_x, mid_y, weight, ha='center', va='center',
            fontsize=8, color='red')



def draw_graph(graph):
    draw()

    drawn = set()
    for u, neighbors in graph.graph.items():
        for v, weight in neighbors.items():
            if (u, v) not in drawn and (v, u) not in drawn:
                x1, y1 = graph.nodes[u]
                x2, y2 = graph.nodes[v]
                draw_edge(x1, y1, x2, y2, weight)
                drawn.add((u, v))

    for node, (x, y) in graph.nodes.items():
        draw_node(x, y, node)

    final_setup()

def final_setup():
    plt.grid(True)
    plt.title('Weighted Graph')
    plt.show()

if __name__ == "__main__":
    g = Graph()
    g.add_node(4,1)
    g.add_node(2,2)
    g.add_node(4,4)
    g.add_node(6,3)
    g.add_node(5,6)
    g.add_node(7,5)
    g.add_edge(2, 1, 4)
    g.add_edge(3, 1, 5)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 2, 5)
    g.add_edge(4, 1, 6)
    g.add_edge(1, 4, 6)
    g.add_edge(4, 3, 5)
    g.add_edge(3, 5, 6)
    g.add_edge(5, 3, 6)
    g.add_edge(4, 5, 7)
    g.add_edge(5, 4, 8)
    g.add_edge(6, 3, 7)
    g.add_edge(3, 6, 7)
    draw_graph(g)