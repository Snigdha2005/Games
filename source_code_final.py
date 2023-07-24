WHITE, BLACK, EMPTY = ".", "#", " "
GRID_ORDER = 5

def make_grid_empty(grid_order : int) -> list[list[str]]:
    return [[WHITE for i in range(grid_order)] for j in range(grid_order)]

def clue_solve_sum_4(grid_row : list[str], single_line_clue : list[str]) -> list[str]:
    clue = ["4", "22", "13", "31"]
    row = [[WHITE, BLACK, BLACK, BLACK, WHITE], [BLACK, BLACK, EMPTY, BLACK, BLACK], [BLACK, EMPTY, BLACK, BLACK, BLACK], [BLACK, BLACK, BLACK, EMPTY, BLACK]]
    sure_black = dict(zip(clue, row))
    return sure_black[''.join(single_line_clue)]

def int_to_str(clue : list[int] ) -> list[str]:
    return list(map(str, clue))

def clue_solve_sum_3(grid_row : list[str], single_line_clue : list[str]) -> list[str]:
    clue = ["3", "12", "21", "111"]
    row = [[WHITE, WHITE, BLACK, WHITE, WHITE], [WHITE, WHITE, WHITE, BLACK, WHITE], [WHITE, BLACK, WHITE, WHITE, WHITE], [BLACK, EMPTY, BLACK, EMPTY, BLACK]]
    sure_black = dict(zip(clue, row))
    return sure_black[''.join(single_line_clue)]

def row_wise_initial_solve(grid : list[list[str]], row_clues : list[list[int]]) -> list[list[str]]:
    for pos, single_line_clue in enumerate(row_clues):
        if sum(single_line_clue) == GRID_ORDER:
            grid[pos] = [BLACK, BLACK, BLACK, BLACK, BLACK]
        elif sum(single_line_clue) == GRID_ORDER - 1:
            grid[pos] = clue_solve_sum_4(grid[pos], int_to_str(single_line_clue))
        elif sum(single_line_clue) == GRID_ORDER - 2:
            grid[pos] = clue_solve_sum_3(grid[pos], int_to_str(single_line_clue))
    return grid

def transpose(grid : list[list[str]]) -> list[list[str]]:
    return [[line[j] for line in grid] for j in range(GRID_ORDER)]

def column_wise_initial_solve(grid : list[list[str]], column_clues : list[list[int]]) -> list[list[str]]:
    return transpose(row_wise_initial_solve(transpose(grid), column_clues))

def combine_grids_if_one_black(column_grid : list[list[str]], row_grid : list[list[str]]) -> list[list[str]]:
    return [[BLACK if column_grid[pos][place] == BLACK else row_grid[pos][place] for place in range(GRID_ORDER)] for pos in range(GRID_ORDER)]

def after_initial_solving(grid_line : list[str], single_line_clue : list[str]) -> list[str]:
    clue2 = ["2", "11"]
    clue1 = ["1"]
    clue3 = ["3"]
    if ''.join(single_line_clue) in clue2:
        if grid_line.count(BLACK) == 2 :
            return list((''.join(grid_line)).replace(WHITE, EMPTY))
        elif grid_line.count(BLACK) < 2 :
            return list((''.join(grid_line)).replace(WHITE, BLACK))
    elif ''.join(single_line_clue) in clue1:
        if grid_line.count(BLACK) == 1:
            return list((''.join(grid_line)).replace(WHITE, EMPTY))
        elif grid_line.count(BLACK) < 1:
            return list((''.join(grid_line).replace(WHITE, BLACK)))
    elif ''.join(single_line_clue) in clue3:
        if grid_line.count(BLACK) == 3:
            return list((''.join(grid_line)).replace(WHITE, EMPTY))
        elif grid_line.count(BLACK) < 3:
            return list((''.join(grid_line)).replace(WHITE, BLACK))
    return grid_line

def row_final_solving(grid : list[list[str]], row_clues : list[list[int]]) -> list[list[str]]:
    for pos, single_line_clue in enumerate(row_clues):
        grid[pos] = after_initial_solving(grid[pos], int_to_str(single_line_clue))
    return grid

def column_final_solving(grid : list[list[str]], column_clues : list[list[int]]) -> list[list[str]]:
    return transpose(row_final_solving(transpose(grid), column_clues))

def combine_grids_if_both_black(column_grid : list[list[str]], row_grid : list[list[str]]) -> list[list[str]]:
    return [[BLACK if column_grid[pos][place] == BLACK and row_grid[pos][place] == BLACK else EMPTY for place in range(GRID_ORDER)] for pos in range(GRID_ORDER)]

def computer_solve(row_clues : list[list[int]], column_clues : list[list[int]]) -> list[list[str]]:
    grid = make_grid_empty(GRID_ORDER)
    grid = combine_grids_if_one_black(column_wise_initial_solve(grid, column_clues), row_wise_initial_solve(grid, row_clues))
    grid = combine_grids_if_both_black(column_final_solving(grid, column_clues), row_final_solving(grid, row_clues))
    return grid

def formatting_grid(grid : list[list[str]]):
    return '\n'.join([' '.join(row) for row in grid])

def main_game(row_clues : list[list[int]], column_clues : list[list[int]]):
    return formatting_grid(computer_solve(row_clues, column_clues))

row_clues = [[3], [2, 2], [1, 1], [2, 2], [3]]
column_clues = [[3], [2, 2 ], [1, 1], [2, 2], [3]]
print(main_game(row_clues, column_clues))
