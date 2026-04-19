from algorithms import AS
from algorithms import parse_input

def test_AS_1():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = AS(origin, destinations, "A*", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 3

def test_AS_2():
    finput = "PathFinder-test2.txt"
    origin, destinations, graph = parse_input(finput)

    a = AS(origin, destinations, "A*", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 5

def test_AS_3():
    finput = "PathFinder-test3.txt"
    origin, destinations, graph = parse_input(finput)

    a = AS(origin, destinations, "A*", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 3