from algorithms import Beam
from algorithms import parse_input

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

def test_Beam_NoPath():
    finput = "PathFinder-test4.txt"
    origin, destinations, graph = parse_input(finput)

    a = Beam(origin, destinations, "Beam Search", finput, graph)
    a.search()

    assert a.found == False
    assert a.path == []

def test_Beam_MultiplePaths():
    finput = "PathFinder-test3.txt"
    origin, destinations, graph = parse_input(finput)

    a = Beam(origin, destinations, "Beam Search", finput, graph)
    a.search()

    assert a.found == True
    assert a.path[0] == 1
    assert a.path[-1] == 4
    assert len(a.path) == 3