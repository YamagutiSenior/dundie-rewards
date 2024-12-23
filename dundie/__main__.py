import os
import argparse


def load(filepath):
    try:
        with open(filepath, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError as e:
        print(f"File not found: {filepath}")

def main():
    parser = argparse.ArgumentParser(
    description='Dunder Mifflin Reward Point System',
    epilog="Enjoy and earn rewards for your hard work!",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="Subcommand to run",
        choices=("load", "show", "send"),
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="Path to the reward file",
    )
    args = parser.parse_args()
    print(args)

    try:
        globals()["args.subcommand"] = load(args.filepath)
    except KeyError:
        print(f"File not found: {args.filepath}")
        return


if __name__ == "__main__":
    main()
    #print("Hello, Running dundie...")
    #print(f"Current directory: {os.getcwd()}")
