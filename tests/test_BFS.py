from algorithms import BFS
from algorithms import parse_input

def test_BFS():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = BFS(origin, destinations, "BFS", finput, graph)
    a.search()
    res = len(a.path)

    assert res == 4

    