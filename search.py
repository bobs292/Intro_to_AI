import sys
from algorithms import run_algorithm

if __name__ == "__main__":

    if len(sys.argv) > 2:
        run_algorithm(sys.argv[1], sys.argv[2])

    else:
        print("Invalid Arguments")