import sys
from algorithms import run_algorithm

if __name__ == "__main__":

    if len(sys.argv) == 3:
        run_algorithm(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--gui":
            run_algorithm(sys.argv[1], sys.argv[2], gui=True)
    else:
        print("Invalid Arguments")