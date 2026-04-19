from algorithms import Greed
from algorithms import parse_input

def test_Greed_1():
    finput = "PathFinder-test.txt"
    origin, destinations, graph = parse_input(finput)

    a = Greed(origin, destinations, "Greed", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 3

def test_Greed_2():
    finput = "PathFinder-test2.txt"
    origin, destinations, graph = parse_input(finput)

    a = Greed(origin, destinations, "Greed", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 5

def test_Greed_3():
    finput = "PathFinder-test3.txt"
    origin, destinations, graph = parse_input(finput)

    a = Greed(origin, destinations, "Greed", finput, graph)
    a.search()

    res = len(a.path)

    assert res == 3