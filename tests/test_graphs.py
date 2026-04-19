from algorithms import BFS, Greed, DFS, Beam
from algorithms import parse_input

def test_BFS():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = BFS(origin, destinations, "BFS", finput, graph)
    a.search()
    res = len(a.path)

    assert res == 4
def test_Greed_1():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = Greed(origin, destinations, "Greed", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 3

def test_Greed_1():
    finput = "PathFinder-test2.txt"
    origin, destinations, graph = parse_input(finput)

    a = Greed(origin, destinations, "Greed", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 5

def test_DFS_1():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = DFS(origin, destinations, "DFS", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 4

def test_DFS_2():
    finput = "PathFinder-test2.txt"
    origin, destinations, graph = parse_input(finput)

    a = DFS(origin, destinations, "DFS", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 11

def test_Beam_1():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = Beam(origin, destinations, "Beam Search", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 3

def test_Beam_2():
    finput = "PathFinder-test2.txt"
    origin, destinations, graph = parse_input(finput)

    a = Beam(origin, destinations, "Beam Search", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 5