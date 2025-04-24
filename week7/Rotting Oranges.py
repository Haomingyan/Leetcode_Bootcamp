class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        rotten_lst = [] 
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_lst.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0

        while rotten_lst:
            r, c, minute = rotten_lst.pop(0)
            minutes = max(minutes, minute)

            for row, column in directions:
                nr, nc = r + row, c + column
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    rotten_lst.append((nr, nc, minute + 1))

        return minutes if fresh == 0 else -1
