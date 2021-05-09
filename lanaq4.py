def grid_escape_wrapper(B, i, j, path):
    n = len(B)
    while B[i][j] > -1:
        upperbound = n * 3  # we'd like to have some kind oh an upper bound for the number of steps we made
        # op1 = True
        # op2 = True
        value = B[i][j]
        if move_right(B, i, j):  # if we're allowed to more right
            op1 = grid_escape_wrapper(B, i + value, j, path + value)
        if move_up(B, i, j):  # if we're allowed to more up
            op2 = grid_escape_wrapper(B, i, j + value, path + value)
        return op1 and op2
    return False


def move_right(B, i, j):
    n = len(B)
    no_of_steps = B[i][j]
    if j >= n:
        return False
    else:
        # valid_right = B[i + no_of_steps][j] == -1
        c1 = i + no_of_steps < n
        # return valid_right or c1
        return c1


def move_up(B, i, j):
    n = len(B)
    no_of_steps = B[i][j]
    if i < n:
        # valid_up = B[i][j + no_of_steps] == -1
        c2 = j + no_of_steps < n
        # return valid_up or c2
        return c2
    else:
        return False


def grid_escape_b(B):
    return grid_escape_wrapper(B, 0, 0, 0)


B1 = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]  # T
B2 = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]  # F
B3 = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]  # F

print(grid_escape_b(B3))
# print(len(B1))
