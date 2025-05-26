from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Counts the number of islands in a 2D grid.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        Assumes all four edges of the grid are surrounded by water.

        Args:
            grid: A list of lists of strings, where '1' represents land and '0' represents water.
                  The input grid is modified by this function (visited '1's are turned to '0's).

        Returns:
            The total number of islands.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            """
            Performs Depth-First Search to find all connected land cells
            and marks them as visited (by changing '1' to '0').
            """
            if not is_valid(r, c) or grid[r][c] == '0':
                return

            grid[r][c] = '0'  # Mark as visited by sinking the land

            # Explore neighbors
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        def bfs(r_start, c_start):
            """
            Performs Breadth-First Search (alternative to DFS).
            Not used by default in this implementation if dfs is called.
            """
            q = deque([(r_start, c_start)])
            grid[r_start][c_start] = '0' # Mark as visited
            
            while q:
                r, c = q.popleft()
                
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc) and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr,nc))


        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found an unvisited piece of land
                    island_count += 1
                    dfs(r, c)  # Explore and mark all parts of this island
                    # bfs(r,c) # Alternatively, use BFS

        return island_count

if __name__ == "__main__":
    solver = Solution()

    # Example 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    # Create a deep copy for mutable operations if you want to reuse the original grid
    grid1_copy = [row[:] for row in grid1]
    print(f"Grid 1: Number of islands = {solver.numIslands(grid1_copy)}") # Expected: 1

    # Example 2
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    grid2_copy = [row[:] for row in grid2]
    print(f"Grid 2: Number of islands = {solver.numIslands(grid2_copy)}") # Expected: 3

    # Example 3: No islands
    grid3 = [
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    grid3_copy = [row[:] for row in grid3]
    print(f"Grid 3 (no islands): Number of islands = {solver.numIslands(grid3_copy)}") # Expected: 0

    # Example 4: All '1's (one big island)
    grid4 = [
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    grid4_copy = [row[:] for row in grid4]
    print(f"Grid 4 (all '1's): Number of islands = {solver.numIslands(grid4_copy)}") # Expected: 1
    
    # Example 5: Empty grid
    grid5 = []
    grid5_copy = [row[:] for row in grid5]
    print(f"Grid 5 (empty): Number of islands = {solver.numIslands(grid5_copy)}") # Expected: 0

    # Example 6: Grid with empty rows
    grid6 = [[]] # This is an invalid grid structure based on typical problem constraints (list of lists of STRINGS)
                # A more valid "empty row" grid might be [[]] if the problem setter allows it,
                # or grid = [["0"],[]] which is also ill-defined.
                # The code handles `if not grid or not grid[0]:` which covers `[]` and `[[]]`.
    grid6_copy = [row[:] for row in grid6]
    print(f"Grid 6 (empty row): Number of islands = {solver.numIslands(grid6_copy)}") # Expected: 0
    
    grid7 = [["1"]]
    grid7_copy = [row[:] for row in grid7]
    print(f"Grid 7 (single '1'): Number of islands = {solver.numIslands(grid7_copy)}") # Expected: 1

    grid8 = [["0"]]
    grid8_copy = [row[:] for row in grid8]
    print(f"Grid 8 (single '0'): Number of islands = {solver.numIslands(grid8_copy)}") # Expected: 0
    
    grid9 = [
        ["1","0","1","0","1"]
    ]
    grid9_copy = [row[:] for row in grid9]
    print(f"Grid 9 (linear horizontal): Number of islands = {solver.numIslands(grid9_copy)}") # Expected: 3

    grid10 = [
        ["1"],
        ["0"],
        ["1"],
        ["0"],
        ["1"]
    ]
    grid10_copy = [row[:] for row in grid10]
    print(f"Grid 10 (linear vertical): Number of islands = {solver.numIslands(grid10_copy)}") # Expected: 3
```
