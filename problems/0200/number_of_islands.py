"""
Solution for Number of Islands.

Idea:
BFS or DFS.
"""


# Solution.
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            queue = [(i, j)]
            while queue:
                i, j = queue.pop()
                grid[i][j] = "0"
                if i + 1 < r and grid[i + 1][j] == "1": queue.append((i + 1, j))
                if i - 1 >= 0 and grid[i - 1][j] == "1": queue.append((i - 1, j))
                if j + 1 < c and grid[i][j + 1] == "1": queue.append((i, j + 1))
                if j - 1 >= 0 and grid[i][j - 1] == "1": queue.append((i, j - 1))

        if not grid: return 0
        r, c, num = len(grid), len(grid[0]), 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num += 1
        return num

# Main.
if __name__ == "__main__":
    grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
            ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
            ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
            ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
            ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    print(Solution().numIslands(grid))
