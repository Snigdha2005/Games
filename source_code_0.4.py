WHITE, BLACK, EMPTY = ".", "#", " "
GRID_ORDER = 5

def make_gridB(grid_order : int) -> list[list[str]]:
    return [[WHITE for i in range(grid_order)] for j in range(grid_order)]

def clue_wise_solve4(grid_row : list[str], single_row_clue : list[str]) -> list[str]:
    clue = ["4", "22", "13", "31"]
    row = [[WHITE, BLACK, BLACK, BLACK, WHITE], [BLACK, BLACK, EMPTY, BLACK, BLACK], [BLACK, EMPTY, BLACK, BLACK, BLACK], [BLACK, BLACK, BLACK, EMPTY, BLACK]]
    sure_black = dict(zip(clue, row))
    return sure_black[''.join(single_row_clue)]

def int_to_str(clue : list[int] ) -> list[str]:
    return list(map(str, clue))

def clue_wise_solve3(grid_row : list[str], single_row_clue : list[str]) -> list[str]:
    clue = ["3", "12", "21", "111"]
    row = [[WHITE, WHITE, BLACK, WHITE, WHITE], [WHITE, WHITE, WHITE, BLACK, WHITE], [WHITE, BLACK, WHITE, WHITE, WHITE], [BLACK, EMPTY, BLACK, EMPTY, BLACK]]
    sure_black = dict(zip(clue, row))
    return sure_black[''.join(single_row_clue)]

def row_wise_initial_solve(grid : list[list[str]], row_clues : list[list[int]]) -> list[list[str]]:
    for pos, single_row_clue in enumerate(row_clues):
        if sum(single_row_clue) == GRID_ORDER:
            (' '.join(grid[pos])).replace(WHITE, BLACK)
            grid[pos] = list(grid[pos])
        elif sum(single_row_clue) == GRID_ORDER - 1:
            grid[pos] = clue_wise_solve4(grid[pos], int_to_str(single_row_clue))
        elif sum(single_row_clue) == GRID_ORDER - 2:
            grid[pos] = clue_wise_solve3(grid[pos], int_to_str(single_row_clue))
    return grid

def transpose(grid : list[list[str]]) -> list[list[str]]:
    return [[ele[j] for ele in grid] for j in range(GRID_ORDER)]

def column_wise_initial_solve(grid : list[list[str]], column_clues : list[list[int]]) -> list[list[str]]:
    return transpose(row_wise_initial_solve(transpose(grid), column_clues))

def combine_gridsB(column_grid : list[list[str]], row_grid : list[list[str]]) -> list[list[str]]:
    return [[BLACK if column_grid[pos][place] == BLACK else row_grid[pos][place] for place in range(GRID_ORDER)] for pos in range(GRID_ORDER)]

def after_initial_solving(grid : list[list[str]], single_row_clue : list[str]) -> list[str]:
        clue = ["2", "11"]
        for i in grid:
            if single_row_clue in clue:
                if i.count(BLACK) == "2" :
                    s = (' '.join(i)).replace(WHITE, EMPTY)
                    i = s.split()
                if i.count(EMPTY) == "3" :
                    (' '.join(i)).replace(WHITE, BLACK)
        clue = ["1"]
        for i in grid:
            if single_row_clue in clue:
                if i.count(BLACK) == "1":
                    (' '.join(i)).replace(WHITE, EMPTY)
       return grid

def row_final_solving(grid : list[list[str]], row_clues : list[list[int]]) -> list[list[str]]:
    for pos, single_row_clue in enumerate(row_clues):
        grid = after_initial_solving(grid, single_row_clue)
    return grid

def column_final_solving(grid : list[list[str]], column_clues : list[list[int]]) -> list[list[str]]:
    return transpose(row_final_solving(transpose(grid), column_clues))

def computer_solve(row_clues : list[list[int]], column_clues : list[list[int]]) -> list[list[str]]:
    grid = make_gridB(GRID_ORDER)
    grid = combine_gridsB(column_wise_initial_solve(grid, column_clues), row_wise_initial_solve(grid, row_clues))
    grid = combine_gridsB(column_final_solving(grid, column_clues), row_final_solving(grid, row_clues))
    return grid

def formatting_grid(grid : list[list[str]]):
    return '\n'.join([' '.join(row) for row in grid])

def main_game(row_clues : list[list[int]], column_clues : list[list[int]]):
    return formatting_grid(computer_solve(row_clues, column_clues))
