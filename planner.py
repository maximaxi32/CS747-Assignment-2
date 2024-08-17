from MDPSolver import *
import argparse

parser = argparse.ArgumentParser()


def main():
    parser.add_argument("--mdp", type=str)
    parser.add_argument("--algorithm", type=str, default="vi")
    parser.add_argument("--policy", type=str, required=False)
    args = parser.parse_args()
    MDPSolver(args.mdp, args.algorithm, args.policy)


if __name__ == "__main__":
    main()
