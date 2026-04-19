from algorithms import UCS
from algorithms import parse_input

def test_UCS_path_length_1():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = UCS(origin, destinations, "UCS", finput, graph)
    a.search()
    res = len(a.path)

    assert res == 3

def test_UCS_path_length_2():
    finput = "PathFinder-test2.txt"
    origin, destinations, graph = parse_input(finput)

    a = UCS(origin, destinations, "UCS", finput, graph)
    a.search()
    res = len(a.path)

    assert res == 5

def test_UCS_path_length_3():
    finput = "PathFinder-test3.txt"
    origin, destinations, graph = parse_input(finput)

    a = UCS(origin, destinations, "UCS", finput, graph)
    a.search()
    res = len(a.path)

    assert res == 3

def test_UCS_NoPath():
    finput = "PathFinder-test4.txt"
    origin, destinations, graph = parse_input(finput)

    a = UCS(origin, destinations, "BFS", finput, graph)
    a.search()

    assert a.found == False
    assert a.path == []