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

    def count_submarines_better_way2(self) -> int:
        count = 0
        width = len(self.grid[0])
        for i, row in enumerate(self.grid):
            j = 0
            submarines_in_row = []

            while j < width:
                if i != 0 and old_submarines and old_submarines[0][0] <= j:
                    """
                    Check if in the previous row has a submarine in the same column - and continue to the next column
                    """
                    current_submarine = old_submarines.pop(0)
                    if row[j] == SUBMARINE_SIGN:
                        """
                        If we found a submarine - we need to add this for the next row
                        """
                        submarines_in_row.append(current_submarine)
                    j = current_submarine[1]
                    if j >= width:
                        break
                    continue

                if row[j] == SUBMARINE_SIGN:

                    if 0 == j or row[j - 1] != SUBMARINE_SIGN:
                        """
                        check if the left point is not a submarine too - if so, add 1 to the counter,
                        and add the submarine to the list of submarines in this row
                        """
                        count += 1
                        submarines_in_row.append([j])

                else:
                    """
                    if we don't find a submarine - we need to check if is end of submarine and add it to the list
                    """
                    if submarines_in_row and len(submarines_in_row[-1]) == 1:
                        submarines_in_row[-1].append(j)

                j += 1

            old_submarines = submarines_in_row
            if submarines_in_row and len(submarines_in_row[-1]) == 1:
                """if the last submarine in the row is not closed - we need to add it"""
                submarines_in_row[-1].append(j)
        return count


if __name__ == '__main__':
    from Test_Submarine import s2

    print(s2.count_submarines_better_way2())
