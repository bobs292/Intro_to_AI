from algorithms import run_algorithm
from algorithms import parse_input
import pytest

def test_invalid_path():
    with pytest.raises(ValueError):
        run_algorithm("PathFinder-test.txt", "falsealgorithm")
    
def test_invalid_path():
    with pytest.raises(FileNotFoundError):
        run_algorithm("PathFi.txt", "BFS")