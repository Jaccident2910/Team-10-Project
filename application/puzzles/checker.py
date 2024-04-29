from os import path

def checkAnswer(puzzle_id, solution):
    match puzzle_id:
        case 0:
            return tower_of_hanoi(5, solution)
        case 5:
            print(input)
            print(output)
            print(grade(input, solution, output))
            return True if grade(input, solution, output) == 0 else False
        case 16:
            return True
        case 17:
            return True
        case 18:
            return True
        case 19:
            return True
        case 20:
            return True
        case _:
            return puzzle_id


def tower_of_hanoi(n, inmoves):
    from ast import literal_eval
    moves = literal_eval(inmoves)
    a = []
    b = []
    c = []
    for i in range(n):
        a.append(i+1)
    for move in moves:
        match move[0]:
            case 'A':
                if(len(a) == 0):
                    return False
                else:
                    currentDisk = a[-1]
                    a.pop()
            case 'B':
                if(len(b) == 0):
                    return False
                else:
                    currentDisk = b[-1]
                    b.pop()
            case 'C':
                if(len(c) == 0):
                    return False
                else:
                    currentDisk = c[-1]
                    c.pop()
            case _:
                return False
                
        match move[1]:
            case 'A':
                if((len(a) != 0) and (a[-1] > currentDisk)):
                    return False
                else:
                    a.append(currentDisk)
            case 'B':
                if((len(b) != 0) and b[-1] > currentDisk):
                    return False
                else:
                    b.append(currentDisk)
            case 'C':
                if((len(c) != 0) and c[-1] > currentDisk):
                    return False
                else:
                    c.append(currentDisk)
                    if(len(c) == n):
                        return True
            case _:
                return False

    

def read_test_input(input: str):
    lines = input.splitlines()
    if len(lines) < 1:
        raise Exception("Invalid input: Expected first line, got none")

    line = lines[0]
    try:
        numbers = list(map(int, line.split()))
    except:
        raise Exception("Invalid input: First line contains non-numbers")

    if len(numbers) != 3:
        raise Exception(
            "Invalid input: First line contains invalid number of arguments"
        )

    num_rows, num_columns, num_houses = numbers

    if len(lines) < 1 + num_rows:
        raise Exception("Invalid input: Not enough lines")

    actual_num_houses = 0
    try:
        grid = [lines[i + 1].rstrip("/n") for i in range(num_rows)]
    except:
        raise Exception("Invalid input: Not enough lines in input")

    for row_id in range(num_rows):
        if len(grid[row_id]) != num_columns:
            raise Exception("Invalid input: Row has unexpected number of columns")

        for column_id in range(num_columns):
            if (
                grid[row_id][column_id] != "."
                and grid[row_id][column_id] != "*"
                and grid[row_id][column_id] != "H"
            ):
                raise Exception("Invalid input: Unrecognized symbol in grid")

            if grid[row_id][column_id] == "H":
                actual_num_houses += 1

    if actual_num_houses != num_houses:
        raise Exception(
            "Invalid input: Number of houses doesn't match actual number of houses"
        )

    return num_rows, num_columns, num_houses, grid


def read_contestant_output(output: str):
    lines = output.splitlines()

    if len(lines) < 1:
        raise Exception("Invalid contestant output: Expected first line, got none")

    line = lines[0].rstrip("/n")
    try:
        route_length = int(line)
    except:
        raise Exception(
            "Invalid contestant output: First line doesn't contain a number"
        )

    if len(lines) < 2:
        raise Exception("Invalid contestant output: Expected second line, got none")

    line = lines[1].rstrip("/n")
    try:
        numbers = list(map(int, line.split()))
    except:
        raise Exception("Invalid contestant output: Second line contains non-numbers")

    if len(numbers) != 2:
        raise Exception(
            "Invalid contestant output: Second line contains invalid number of arguments"
        )

    starting_row, starting_column = numbers
    if len(lines) < 3:
        raise Exception("Invalid contestant output: Expected a third line, got none")

    directions = lines[2].rstrip("/n")
    for dir in directions:
        if dir != "L" and dir != "R" and dir != "U" and dir != "D":
            raise Exception(
                "Invalid contestant output: Unrecognized symbol in directions"
            )

    return route_length, starting_row, starting_column, directions


def read_output(output: str):
    lines = output.splitlines()

    if len(output) < 1:
        raise Exception("Invalid output: Expected first line, got none")

    line = lines[0].rstrip("/n")
    try:
        optimal_length = int(line)
    except:
        raise Exception("Invalid output: First line doesnt't contain a number")

    return optimal_length


def grade(input: str, contestant_output: str, output: str):
    try:
        num_rows, num_columns, num_houses, grid = read_test_input(input)
    except Exception as e:
        return 2

    try:
        optimal_length = read_output(contestant_output)
    except Exception as e:
        return 2

    try:
        route_length, starting_row, starting_column, directions = (
            read_contestant_output(output)
        )
    except Exception as e:
        return 3

    if route_length != optimal_length:
        return 4

    if len(directions) != route_length:
        return 4

    if (
        starting_row < 0
        or starting_row >= num_rows
        or starting_column < 0
        or starting_column >= num_columns
    ):
        return 4

    houses = [
        (row, column)
        for row in range(num_rows)
        for column in range(num_columns)
        if grid[row][column] == "H"
    ]
    is_visited = [False for _ in range(len(houses))]

    current_row = starting_row
    current_column = starting_column
    if grid[current_row][current_column] == "H":
        is_visited[houses.index((current_row, current_column))] = True

    for dir in directions:
        if dir == "L":
            current_column -= 1
        elif dir == "R":
            current_column += 1
        elif dir == "U":
            current_row -= 1
        else:
            assert dir == "D"
            current_row += 1

        if (
            current_row < 0
            or current_row >= num_rows
            or current_column < 0
            or current_column >= num_columns
        ):
            return 4

        if grid[current_row][current_column] == "*":
            return 4

        if grid[current_row][current_column] == "H":
            is_visited[houses.index((current_row, current_column))] = True

    for el in is_visited:
        if el == False:
            return 4

    return 0

with open(path.join(path.dirname(__file__), f"in"), "r") as f, open(path.join(path.dirname(__file__), f"out"), "r") as f1:
    input = f.read()
    output = f1.read()
