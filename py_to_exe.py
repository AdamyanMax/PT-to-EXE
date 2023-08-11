import argparse


def hello_world(string: str):
    print(f"Hello {string}")


def list_sum(lst: list):
    print(sum(lst))


def input_asker():
    print(input("Whats your name? "))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--hw', type=str, help='Argument for hello_world function')
    parser.add_argument('--ls', type=int, nargs='+', help='Argument for list_sum function')
    parser.add_argument('--ia', action='store_true', help='Flag for input_asker function')
    args = parser.parse_args()

    if args.hw:
        hello_world(args.hw)
    if args.ls:
        list_sum(args.ls)
    if args.ia:
        input_asker()

