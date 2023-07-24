WHITE, BLACK = ".", "#"
GRID_ORDER = 5
def make_gridA(grid_order : int) -> list[list[str]]:
    grid = []
    for i in range(GRID_ORDER):
        grid_row = []
        for j in range(GRID_ORDER):
            grid_row.append(WHITE)
        grid.append(grid_row)
    return grid

def make_gridB(grid_order : int) -> list[list[str]]:
    return [[WHITE for i in range(grid_order)] for j in range(grid_order)]

def clue_wise_solve(grid_row : list[str], single_row_clue : list[int]) -> list[str]:
    clue = [4, 22, 13, 31]
    row = [[WHITE, BLACK, BLACK, BLACK, WHITE], [BLACK, BLACK, WHITE, BLACK, BLACK], [BLACK, WHITE, BLACK, BLACK, BLACK], [BLACK, BLACK, BLACK, WHITE, BLACK]]
    sure_black = dict(zip(clue, row))
    return sure_black[''.join(single_row_clue)]

def row_wise_solve(grid : list[list[str]], row_clues : list[list[int]]) -> list[list[str]]:
    for pos, single_row_clue in enumerate(row_clues):
        if sum(single_row_clue) == GRID_ORDER:
            (' '.join(grid[pos])).replace(WHITE, BLACK)
        elif sum(single_row_clue) == GRID_ORDER - 1:
            
