import sys
from os import path

def checkAnswer(puzzle_id, solution):
    match puzzle_id:
        case 1:
            return tower_of_hanoi(9, solution)
        case 2:
            return tower_of_hanoi2(6, solution)
        case 16:
            return True
        case 7:
            with (
                open("./puzzles/static/puzzleData/7_input.txt", "r") as f,
                open("./puzzles/static/puzzleData/7_output.txt", "r") as f1,
            ):
                input = f.read()
                output = f1.read()

            result = grade_1(input, solution, output)
            assert result != 2

            return True if result == 0 else False
        case 4:
            with open("./puzzles/static/puzzleData/4_output.txt", "r") as f:
                output = f.read()

            result = grade_2(output, solution)
            assert result != 2

            return True if result == 0 else False
        case 5:
            return True if solution == 34095 else False
        case 6:
            return True if solution == 10593 else False
        case 9:
            with (
                open("./puzzles/static/puzzleData/9_input.txt", "r") as f,
                open("./puzzles/static/puzzleData/9_output.txt", "r") as f1,
            ):
                input = f.read()
                output = f1.read()
                result = grade_3(input, solution, output)

                assert result != 2

                return True if result == 0 else False
        case 3:
            return True if solution == 849013480 else False
        case 8:
            return True if solution == 2669959738186064375 else False

def read_test_input_3(input: str):
    lines = input.splitlines()
    if len(lines) < 1:
        raise Exception("Invalid input: Expected first line, got none")

    line = lines[0].rstrip("\n")
    try:
        numbers = list(map(int, line.split()))
    except:
        raise Exception("Invalid input: First line contains non-integers")

    if len(numbers) != 2:
        raise Exception(
            "Invalid input: First line contains invalid number of arguments"
        )

    num_items, num_combinations = numbers

    if num_items < 1:
        raise Exception("Invalid input: Number of items is invalid")

    if num_combinations < 1:
        raise Exception("Invalid input: Number of combinations is invalid")

    if len(lines) < 2:
        raise Exception("Invalid input: Expected second line, got none")

    line = lines[1].rstrip("\n")
    try:
        costs = list(map(int, line.split()))
    except:
        raise Exception("Invalid input: Second line contains non-integers")

    if len(costs) != num_items:
        raise Exception(
            "Invalid input: Second line contains invalid number of arguments"
        )

    if len(lines) < 2 + num_combinations:
        raise Exception("Invalid input: Not enough lines")

    combinations = []
    for i in range(num_combinations):
        line = lines[2 + i].rstrip("\n")
        try:
            numbers = list(map(int, line.split()))
        except:
            raise Exception(f"Invalid input: Line {3 + i} contains non-integers")

        if len(numbers) < 2:
            raise Exception(f"Invalid input: Line {3 + i} contains less than 2 numbers")

        cost = numbers[0]
        num_items_in_combination = numbers[1]
        if num_items_in_combination != len(numbers) - 2:
            raise Exception(f"Invalid input: Line {3 + i} is invalid")

        combinations.append((cost, numbers[2:]))

    return num_items, num_combinations, costs, combinations


def read_contestant_output_3(output: str):
    lines = output.splitlines()
    if len(lines) < 1:
        raise Exception("Invalid contestant output: Expected first line, got none")

    line = lines[0].rstrip("\n")
    try:
        numbers = list(map(int, line.split()))
    except:
        raise Exception("Invalid contestant output: First line contains non-integers")

    if len(numbers) != 2:
        raise Exception(
            "Invalid contestant output: Second line has invalid number of arguments"
        )

    total_cost, num_items = numbers
    if num_items < 0:
        raise Exception(
            "Invalid contestant output: Number of items should be non-negative"
        )

    if len(lines) < 2:
        raise Exception("Invalid contestant output: Expected second line, got none")

    line = lines[1].rstrip("\n")
    try:
        items = list(map(int, line.split()))
    except:
        raise Exception("Invalid contestant output: Second line contains non-integers")

    if len(items) != num_items:
        raise Exception(
            "Invalid contestant output: Second line contains invalid number of arguments"
        )

    return total_cost, num_items, items


def read_output_3(output: str):
    lines = output.splitlines()
    if len(lines) < 1:
        raise Exception("Invalid output: Expected first line, got none")

    line = lines[0].rstrip("\n")
    try:
        numbers = list(map(int, line.split()))
    except:
        raise Exception("Invalid output: First line contains non-integers")

    if len(numbers) != 2:
        raise Exception("Invalid output: First line contains wrong number of arguments")

    total_cost, _ = numbers
    return total_cost


def grade_3(input: str, contestant_output: str, output: str):
    try:
        num_items, num_combinations, costs, combinations = read_test_input_3(input)

    except Exception as e:
        print(e, file=sys.stderr)
        return 2

    assert len(costs) == num_items and len(combinations) == num_combinations

    try:
        optimal_cost = read_output_3(output)
    except Exception as e:
        print(e, file=sys.stderr)
        return 2

    try:
        total_cost, num_items_taken, items = read_contestant_output_3(contestant_output)
    except Exception as e:
        print(e, file=sys.stderr)
        return 3

    assert len(items) == num_items_taken

    if optimal_cost != total_cost:
        print("Wrong answer: Jury found better answer", file=sys.stderr)
        return 4

    for item in items:
        if item < 1 or item > num_items:
            print("Wrong answer: Invalid item id", file=sys.stderr)
            return 4

    sorted_items = items.copy()
    if sorted_items != items:
        print("Wrong answer: List of items is not sorted", file=sys.stderr)
        return 4

    prev_el = None
    for el in items:
        if el == prev_el:
            print("Wrong answer: Duplicate items in list", file=sys.stderr)
            return 4

        prev_el = el

    is_item_taken = [False for _ in range(num_items)]
    for el in items:
        is_item_taken[el - 1] = True

    real_cost = 0
    for cost, items_in_combination in combinations:
        is_taken = True
        for el in items_in_combination:
            if not is_item_taken[el - 1]:
                is_taken = False
                break

        if is_taken:
            real_cost += cost

    for item in items:
        real_cost -= costs[item - 1]

    if real_cost != total_cost:
        print(f"Real cost is {real_cost}")
        print(f"Total cost is {total_cost}")
        print(
            "Wrong answer: Constestant's total cost doesn't match reality",
            file=sys.stderr,
        )
        return 4

    print("Correct answer", file=sys.stderr)
    return 0


def read_contestant_output_2(output: str):
    lines = output.splitlines()

    if len(lines) < 1:
        raise Exception("Invalid contestant output: Expected first line, got none")

    line = lines[0].rstrip("\n")

    for ch in line:
        if ch != "(" and ch != ")":
            raise Exception(
                "Invalid contestant output: Unrecognized symbol in sequence"
            )

    return line


def read_output_2(output: str):
    lines = output.splitlines()

    if len(lines) < 1:
        raise Exception("Invalid output: Expected first line, got none")

    line = lines[0].rstrip("\n")

    for ch in line:
        if ch != "(" and ch != ")":
            raise Exception("Invalid output: Unrecognized symbol in sequence")

    return line


def grade_2(solution: str, contestant_solution: str):
    try:
        solution = read_output_2(solution)
    except Exception as e:
        print("Invalid output", file=sys.stderr)
        print(e, file=sys.stderr)
        return 2

    try:
        contestant_solution = read_contestant_output_2(contestant_solution)
    except Exception as e:
        print("Invalid contestant output", file=sys.stderr)
        print(e, file=sys.stderr)

    if len(contestant_solution) != len(solution):
        print("Wrong answer: Invalid sequence length", file=sys.stderr)
        return 4

    if contestant_solution != solution:
        print("Wrong answer", file=sys.stderr)
        return 4

    print("Correct answer", file=sys.stderr)
    return 0

'''
def read_test_input_1(input: str):
    solution = int(input)
    match (solution):
        case 7:
            with (
                open("./puzzles/static/puzzleData/7_input.txt", "r") as f,
                open("./puzzles/static/puzzleData/7_output.txt", "r") as f1,
            ):
                input = f.read()
                output = f1.read()

            result = grade_1(input, solution, output)
            assert result != 2

            return True if result == 0 else False
        case 4:
            with open("./puzzles/static/puzzleData/4_output.txt", "r") as f:
                output = f.read()

            result = grade_2(output, solution)
            assert result != 2

            return True if result == 0 else False
        case 5:
            return True if solution == 34095 else False
        case 6:
            return True if solution == 10593 else False
        case 9:
            with (
                open("./puzzles/static/puzzleData/9_input.txt", "r") as f,
                open("./puzzles/static/puzzleData/9_output.txt", "r") as f1,
            ):
                input = f.read()
                output = f1.read()
                result = grade_3(input, solution, output)

                assert result != 2

                return True if result == 0 else False
        case 3:
            return True if solution == 849013480 else False
        case 8:
            return True if solution == 2669959738186064375 else False
'''

def read_test_input_3(input: str):
    lines = input.splitlines()
    if len(lines) < 1:
        raise Exception("Invalid input: Expected first line, got none")

    line = lines[0].rstrip("\n")
    try:
        numbers = list(map(int, line.split()))
    except:
        raise Exception("Invalid input: First line contains non-integers")

    if len(numbers) != 2:
        raise Exception(
            "Invalid input: First line contains invalid number of arguments"
        )

    num_items, num_combinations = numbers

    if num_items < 1:
        raise Exception("Invalid input: Number of items is invalid")

    if num_combinations < 1:
        raise Exception("Invalid input: Number of combinations is invalid")

    if len(lines) < 2:
        raise Exception("Invalid input: Expected second line, got none")

    line = lines[1].rstrip("\n")
    try:
        costs = list(map(int, line.split()))
    except:
        raise Exception("Invalid input: Second line contains non-integers")

    if len(costs) != num_items:
        raise Exception(
            "Invalid input: Second line contains invalid number of arguments"
        )

    if len(lines) < 2 + num_combinations:
        raise Exception("Invalid input: Not enough lines")

    combinations = []
    for i in range(num_combinations):
        line = lines[2 + i].rstrip("\n")
        try:
            numbers = list(map(int, line.split()))
        except:
            raise Exception(f"Invalid input: Line {3 + i} contains non-integers")

        if len(numbers) < 2:
            raise Exception(f"Invalid input: Line {3 + i} contains less than 2 numbers")

        cost = numbers[0]
        num_items_in_combination = numbers[1]
        if num_items_in_combination != len(numbers) - 2:
            raise Exception(f"Invalid input: Line {3 + i} is invalid")

        combinations.append((cost, numbers[2:]))

    return num_items, num_combinations, costs, combinations


def read_contestant_output_3(output: str):
    lines = output.splitlines()
    if len(lines) < 1:
        raise Exception("Invalid contestant output: Expected first line, got none")

    line = lines[0].rstrip("\n")
    try:
        numbers = list(map(int, line.split()))
    except:
        raise Exception("Invalid contestant output: First line contains non-integers")

    if len(numbers) != 2:
        raise Exception(
            "Invalid contestant output: Second line has invalid number of arguments"
        )

    total_cost, num_items = numbers
    if num_items < 0:
        raise Exception(
            "Invalid contestant output: Number of items should be non-negative"
        )

    if len(lines) < 2:
        raise Exception("Invalid contestant output: Expected second line, got none")

    line = lines[1].rstrip("\n")
    try:
        items = list(map(int, line.split()))
    except:
        raise Exception("Invalid contestant output: Second line contains non-integers")

    if len(items) != num_items:
        raise Exception(
            "Invalid contestant output: Second line contains invalid number of arguments"
        )

    return total_cost, num_items, items


def read_output_3(output: str):
    lines = output.splitlines()
    if len(lines) < 1:
        raise Exception("Invalid output: Expected first line, got none")

    line = lines[0].rstrip("\n")
    try:
        numbers = list(map(int, line.split()))
    except:
        raise Exception("Invalid output: First line contains non-integers")

    if len(numbers) != 2:
        raise Exception("Invalid output: First line contains wrong number of arguments")

    total_cost, _ = numbers
    return total_cost


def grade_3(input: str, contestant_output: str, output: str):
    try:
        num_items, num_combinations, costs, combinations = read_test_input_3(input)

    except Exception as e:
        print(e, file=sys.stderr)
        return 2

    assert len(costs) == num_items and len(combinations) == num_combinations

    try:
        optimal_cost = read_output_3(output)
    except Exception as e:
        print(e, file=sys.stderr)
        return 2

    try:
        total_cost, num_items_taken, items = read_contestant_output_3(contestant_output)
    except Exception as e:
        print(e, file=sys.stderr)
        return 3

    assert len(items) == num_items_taken

    if optimal_cost != total_cost:
        print("Wrong answer: Jury found better answer", file=sys.stderr)
        return 4

    for item in items:
        if item < 1 or item > num_items:
            print("Wrong answer: Invalid item id", file=sys.stderr)
            return 4

    sorted_items = items.copy()
    if sorted_items != items:
        print("Wrong answer: List of items is not sorted", file=sys.stderr)
        return 4

    prev_el = None
    for el in items:
        if el == prev_el:
            print("Wrong answer: Duplicate items in list", file=sys.stderr)
            return 4

        prev_el = el

    is_item_taken = [False for _ in range(num_items)]
    for el in items:
        is_item_taken[el - 1] = True

    real_cost = 0
    for cost, items_in_combination in combinations:
        is_taken = True
        for el in items_in_combination:
            if not is_item_taken[el - 1]:
                is_taken = False
                break

        if is_taken:
            real_cost += cost

    for item in items:
        real_cost -= costs[item - 1]

    if real_cost != total_cost:
        print(f"Real cost is {real_cost}")
        print(f"Total cost is {total_cost}")
        print(
            "Wrong answer: Constestant's total cost doesn't match reality",
            file=sys.stderr,
        )
        return 4

    print("Correct answer", file=sys.stderr)
    return 0


def read_contestant_output_2(output: str):
    lines = output.splitlines()

    if len(lines) < 1:
        raise Exception("Invalid contestant output: Expected first line, got none")

    line = lines[0].rstrip("\n")

    for ch in line:
        if ch != "(" and ch != ")":
            raise Exception(
                "Invalid contestant output: Unrecognized symbol in sequence"
            )

    return line


def read_output_2(output: str):
    lines = output.splitlines()

    if len(lines) < 1:
        raise Exception("Invalid output: Expected first line, got none")

    line = lines[0].rstrip("\n")

    for ch in line:
        if ch != "(" and ch != ")":
            raise Exception("Invalid output: Unrecognized symbol in sequence")

    return line


def grade_2(solution: str, contestant_solution: str):
    try:
        solution = read_output_2(solution)
    except Exception as e:
        print("Invalid output", file=sys.stderr)
        print(e, file=sys.stderr)
        return 2

    try:
        contestant_solution = read_contestant_output_2(contestant_solution)
    except Exception as e:
        print("Invalid contestant output", file=sys.stderr)
        print(e, file=sys.stderr)

    if len(contestant_solution) != len(solution):
        print("Wrong answer: Invalid sequence length", file=sys.stderr)
        return 4

    if contestant_solution != solution:
        print("Wrong answer", file=sys.stderr)
        return 4

    print("Correct answer", file=sys.stderr)
    return 0


def read_test_input_1(input: str):
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
        grid = [lines[i + 1].rstrip("\n") for i in range(num_rows)]

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



def read_contestant_output_1(output: str):
    lines = output.splitlines()

    if len(lines) < 1:
        raise Exception("Invalid contestant output: Expected first line, got none")

    line = lines[0].rstrip("\n")
    line = lines[0].rstrip("\n")
    try:
        route_length = int(line)
    except:
        raise Exception(
            "Invalid contestant output: First line doesn't contain a number"
        )

    if len(lines) < 2:
        raise Exception("Invalid contestant output: Expected second line, got none")

    line = lines[1].rstrip("\n")
    line = lines[1].rstrip("\n")
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

    directions = lines[2].rstrip("\n")
    directions = lines[2].rstrip("\n")
    for dir in directions:
        if dir != "L" and dir != "R" and dir != "U" and dir != "D":
            raise Exception(
                "Invalid contestant output: Unrecognized symbol in directions"
            )

    return route_length, starting_row, starting_column, directions



def read_output_1(output: str):
    lines = output.splitlines()

    if len(output) < 1:
        raise Exception("Invalid output: Expected first line, got none")

    line = lines[0].rstrip("\n")
    line = lines[0].rstrip("\n")
    try:
        optimal_length = int(line)
    except:
        raise Exception("Invalid output: First line doesnt't contain a number")

    return optimal_length



def grade_1(input: str, contestant_output: str, output: str):
    try:
        num_rows, num_columns, _, grid = read_test_input_1(input)
    except Exception as e:
        print(e, file=sys.stderr)

        return 2

    try:
        optimal_length = read_output_1(output)
    except Exception as e:
        print(e, file=sys.stderr)
        return 2

    try:
        route_length, starting_row, starting_column, directions = (
            read_contestant_output_1(contestant_output)
        )
    except Exception as e:
        print(e, file=sys.stderr)
        return 3

    if route_length != optimal_length:
        print("Contestant found incorrect route length", file=sys.stderr)
        return 4

    if len(directions) != route_length:
        print("Contestant's direction sequence has invalid length", file=sys.stderr)
        return 4

    if (
        starting_row < 0
        or starting_row >= num_rows
        or starting_column < 0
        or starting_column >= num_columns
    ):
        print("Contestant's starting position is outside of the grid", file=sys.stderr)
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
            print("Contestant trying to go outside of grid", file=sys.stderr)
            return 4

        if grid[current_row][current_column] == "*":
            print("Contestant trying to get into a blocked square", file=sys.stderr)
            return 4

        if grid[current_row][current_column] == "H":
            is_visited[houses.index((current_row, current_column))] = True

    for el in is_visited:
        if el == False:
            print("Contestant's route doesn't visit all the houses", file=sys.stderr)
            return 4

    return 0


def tower_of_hanoi(n, inmoves):
    from ast import literal_eval
    try:
        moves = literal_eval(inmoves)
        a = []
        b = []
        c = []
        for i in range(n):
            a.append(i + 1)
        for move in moves:
            match move[0]:
                case "A":
                    if len(a) == 0:
                        return False
                    else:
                        currentDisk = a[-1]
                        a.pop()
                case "B":
                    if len(b) == 0:
                        return False
                    else:
                        currentDisk = b[-1]
                        b.pop()
                case "C":
                    if len(c) == 0:
                        return False
                    else:
                        currentDisk = c[-1]
                        c.pop()
                case _:
                    return False

            match move[1]:
                case "A":
                    if (len(a) != 0) and (a[-1] > currentDisk):
                        return False
                    else:
                        a.append(currentDisk)
                case "B":
                    if (len(b) != 0) and b[-1] > currentDisk:
                        return False
                    else:
                        b.append(currentDisk)
                case "C":
                    if (len(c) != 0) and c[-1] > currentDisk:
                        return False
                    else:
                        c.append(currentDisk)
                        if len(c) == n:
                            return True
                case _:
                    return False
    except:
        return False
    


def tower_of_hanoi2(n, inmoves):
    from ast import literal_eval
    moves = literal_eval(inmoves)
    a = [] 
    b = []
    c = []
    d = []
    for i in range(n):
        a.append((i+1, 'R'))
        c.append((i+1, 'B'))
    for move in moves:
        match move[0]:
            case 'A':
                if(len(a) == 0):
                    print("Illegal Move - Rod A is Empty")
                    return False
                else:
                    currentDisk = a[-1]
                    a.pop()
            case 'B':
                if(len(b) == 0):
                    print("Illegal Move - Rod B is Empty")
                    return False
                else:
                    currentDisk = b[-1]
                    b.pop()
            case 'C':
                if(len(c) == 0):
                    print("Illegal Move - Rod C is Empty")
                    return False
                else:
                    currentDisk = c[-1]
                    c.pop()
            case 'D':
                if(len(d) == 0):
                    print("Illegal Move - Rod C is Empty")
                    return False
                else:
                    currentDisk = d[-1]
                    d.pop()         
            case _:
                print("Illegal Input")
                return False

        match move[1]:

            case 'A':

                if((len(a) != 0) and (a[-1][0] > currentDisk[0])):

                    print("Illegal Move - you are placing a larger disk over a smaller disk on Rod A.")

                    return False

                else:

                    a.append(currentDisk)

                    if(len(a) and len(c) == n):

                        if(checkRedBlue(a,c,n)):

                            print('Move disk {} from rod {} to rod {}.'.format(currentDisk, move[0], move[1]))       

                            if(len(moves) == exponent(2,n+1) - 1):

                                print("Solved in Minimum Steps!")

                                return True

                            else:

                                print("Solved, but not in Minimum Steps.")

                                return False  

            case 'B':

                if((len(b) != 0) and b[-1][0] > currentDisk[0]):

                    print("Illegal Move - you are placing a larger disk over a smaller disk on Rod B. ")

                    return False

                else:

                    b.append(currentDisk)

            case 'C':

                if((len(c) != 0) and c[-1][0] > currentDisk[0]):

                    print("Illegal Move - you are placing a larger disk over a smaller disk on Rod C")

                    return False

                else:

                    c.append(currentDisk)

                    if(len(a) and len(c) == n):

                        if(checkRedBlue(a,c,n)):

                            print('Move disk {} from rod {} to rod {}.'.format(currentDisk, move[0], move[1]))       

                            if(len(moves) == exponent(2,n+1) - 1):

                                print("Solved in Minimum Steps!")

                                return True

                            else:

                                print("Solved, but not in Minimum Steps.")

                                return False

            case 'D':

                if((len(d) != 0) and d[-1][0] > currentDisk[0]):

                    print("Illegal Move - you are placing a larger disk over a smaller disk on Rod D. ")

                    return False

                else:

                    d.append(currentDisk)

            case _:

                print("Illegal Input")

                return False

               

        print('Move disk {} from rod {} to rod {}.'.format(currentDisk, move[0], move[1]))

       

    return False

 

def exponent(c,n):

    if(n == 0):

        return 1

    return (c * exponent(c,n-1))

 

def checkRedBlue(a,c,n):

    for i in range(n):

        if((a[i])[1] != 'B' or (c[i])[1] != 'R'):

           return False

    return True

'''with open(path.join(path.dirname(__file__), f"in"), "r") as f, open(path.join(path.dirname(__file__), f"out"), "r") as f1:
    input = f.read()
    output = f1.read()
'''