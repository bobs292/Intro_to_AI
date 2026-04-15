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

def draw_node(x, y, label,face_colour,edge_colour):
    circle = Circle((x, y), radius=0.4, edgecolor=edge_colour, facecolor=face_colour, zorder=3)
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
        draw_node(x, y, node, 'lightblue', 'black')

    final_setup()

def final_setup():
    plt.grid(True)
    plt.title('Weighted Graph')
    plt.show()

def draw_path(alg,graph):
    path = alg.path
    first = path[1]
    last = path [-1]
    for node in path[1:-1]:
        x, y = graph.nodes.items()
        draw_node(x, y, node, 'lightblue', 'green')
    x,y = graph.first.items()
    draw_node(x, y, first, 'green', 'green')
    x,y = graph.last.items()
    draw_node(x, y, last, 'red', 'black')