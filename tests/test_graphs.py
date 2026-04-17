from algorithms import BFS, Greed
from algorithms import parse_input

def test_BFS():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = BFS(origin, destinations, "BFS", finput, graph)
    a.search()
    res = len(a.path)

    assert res == 4
def test_dfs():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = Greed(origin, destinations, "BFS", finput, graph)
    a.search()

    