from typing import List

SUBMARINE_SIGN = 1


class Submarines:
    grid: List[List[int]]

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def check_neighbours(self, i: int, j: int) -> bool:
        # Check if top or left is a submarine too - if so, return False
        if i == 0 and j == 0:
            return True
        if i > 0 and self.grid[i - 1][j] == SUBMARINE_SIGN:
            return False
        if j > 0 and self.grid[i][j - 1] == SUBMARINE_SIGN:
            return False
        return True

    def count_submarines_naive_way(self) -> int:
        count = 0
        for i, row in enumerate(self.grid):
            for j, point in enumerate(row):
                if point == SUBMARINE_SIGN and self.check_neighbours(i, j):
                    count += 1
        return count

    def count_submarines_better_way(self) -> int:
        count = 0
        width = len(self.grid[0])
        for i, row in enumerate(self.grid):
            j = 0
            while j < width:
                if row[j] == SUBMARINE_SIGN and self.check_neighbours(i, j):
                    """
                    If we found a submarine - we don't need to check the neighbours of this point
                    because we don't care if they 1 or zero - anyway we don't need add the counter.
                    """
                    count += 1
                    j += 1
                j += 1
        return count

