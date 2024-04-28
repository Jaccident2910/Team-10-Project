def checkAnswer(puzzle_id, solution):
    match puzzle_id:
        case 0:
            return tower_of_hanoi(5, solution)
        case 16:
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
