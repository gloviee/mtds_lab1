from solver import calculate
from file_reader import read_file
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("filepath", default=None, nargs="?")
    args = parser.parse_args()

    parameters = read_file_input(args.filepath) if args.filepath else read_interactive_input()
    if parameters:
        result = calculate(*parameters)
        print(format_output(result))

def interactive_input() -> list:
    parameters = []
    names = ("a", "b", "c")
    for i, name in enumerate(names):
        while True:
            value = input(f"{name} = ")
            try:
                value = float(value)
                if name == "a" and value == 0:
                    print("Error. a cannot be 0")
                else:
                    parameters.append(value)
                    break
            except ValueError:
                print(f"Error. Expected a valid real number, got {value} instead")
    print(get_equation(parameters))
    return parameters

def format_output(result: list) -> str:
    output = f"{len(result)} roots found"
    for i, x in enumerate(result):
        output += f"\nx{i + 1} = {x}"
    return output


if __name__ == '__main__':
    main()