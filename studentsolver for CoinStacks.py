def in_range(x, l, r):
    return l <= x and x < r


def get_neighbors(i, j, i_dir, j_dir):
    return ((i - i_dir, j), (i, j - j_dir), (i - i_dir, j - j_dir))


def get_max_height_map(height_map, i_dir, j_dir):
    i_len, j_len = len(height_map), len(height_map[0])
    i_range = range(i_len) if i_dir > 0 else range(i_len - 1, -1, i_dir)
    j_range = range(j_len) if j_dir > 0 else range(j_len - 1, -1, j_dir)
    max_height_map = [[0]*j_len for _ in range(i_len)]
    for i in i_range:
        for j in j_range:
            max_height = height_map[i][j]
            for (i_, j_) in get_neighbors(i, j, i_dir, j_dir):
                if in_range(i_, 0, i_len) and in_range(j_, 0, j_len):
                    max_height = max(max_height, max_height_map[i_][j_])
            max_height_map[i][j] = max_height
    return max_height_map


def print_grid(grid):
  for line in grid:
    print(' '.join([str(value) for value in line]))


def solve(grid):
    quadrant_to_max_height_map = {}
    quadrant_to_max_height_map[0] = get_max_height_map(grid, +1, +1)
    quadrant_to_max_height_map[1] = get_max_height_map(grid, -1, +1)
    quadrant_to_max_height_map[2] = get_max_height_map(grid, +1, -1)
    quadrant_to_max_height_map[3] = get_max_height_map(grid, -1, -1)

    to_add = 0
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            min_to_add = quadrant_to_max_height_map[0][i][j]
            for d in range(1, 4):
                min_to_add = min(min_to_add, quadrant_to_max_height_map[d][i][j])
            to_add += max(min_to_add - grid[i][j], 0)
            grid[i][j] = max(min_to_add, grid[i][j])
    print_grid(grid)
    return to_add

