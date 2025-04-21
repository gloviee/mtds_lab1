def read_file(filepath: str) -> list | None:
    try:
        values = []
        with open(filepath, "r") as file:
            str_values = file.readline().strip().split()
        if len(str_values) != 3:
            print("Invalid file format")
        for i, str_value in enumerate(str_values):
            try:
                value = float(str_value)
                if i == 0 and value == 0:
                    print("Error. a cannot be 0")
                else:
                    values.append(value)
            except ValueError:
                print(f"Error. Expected a valid real number, got {str_value} instead")

        print(get_equation(parameters))
        return parameters

    except FileNotFoundError:
        print(f"file {filepath} does not exist")
        return None

def get_equation(parameters):
    parameters_dict = dict(zip(("a", "b", "c"), parameters))
    return f"Equation is: ({parameters_dict.get('a')}) x^2 + ({parameters_dict.get('b')}) x + ({parameters_dict.get('c')}) = 0"