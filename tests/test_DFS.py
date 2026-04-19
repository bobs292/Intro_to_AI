from algorithms import DFS
from algorithms import parse_input

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

def test_DFS_NoPath():
    finput = "PathFinder-test4.txt"
    origin, destinations, graph = parse_input(finput)

    a = DFS(origin, destinations, "DFS", finput, graph)
    a.search()

    assert a.found == False
    assert a.path == []

def test_DFS_MultiplePaths():
    finput = "PathFinder-test3.txt"
    origin, destinations, graph = parse_input(finput)

    a = DFS(origin, destinations, "DFS", finput, graph)
    a.search()

    assert a.found == True
    assert a.path[0] == 1
    assert a.path[-1] == 4
    assert len(a.path) == 4