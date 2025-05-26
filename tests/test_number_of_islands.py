import unittest
import sys
import os

# Adjust sys.path to include the parent directory (root of the repo)
# This allows importing from the 'graph_problems' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graph_problems.number_of_islands import Solution

class TestNumberOfIslands(unittest.TestCase):

    def setUp(self):
        """Create a new Solution instance for each test."""
        self.solver = Solution()

    def run_test(self, grid_input, expected_output):
        """Helper function to run a test case.
        Creates a deep copy of the grid to avoid modification issues across tests
        if the numIslands method modifies the grid in place (which it does).
        """
        grid_copy = [row[:] for row in grid_input] if grid_input else []
        self.assertEqual(self.solver.numIslands(grid_copy), expected_output)

    def test_leetcode_example_1(self):
        """1. Basic example from LeetCode (expected: 1)."""
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        self.run_test(grid, 1)

    def test_leetcode_example_2(self):
        """2. Another common example (expected: 3)."""
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.run_test(grid, 3)

    def test_no_islands(self):
        """3. Grid with no islands (all '0's)."""
        grid = [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        self.run_test(grid, 0)

    def test_all_ones_one_island(self):
        """4. Grid with all islands (all '1's, forming one large island)."""
        grid = [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"]
        ]
        self.run_test(grid, 1)

    def test_single_cell_grid(self):
        """5. Single cell grid ('1' or '0')."""
        self.run_test([["1"]], 1)
        self.run_test([["0"]], 0)

    def test_linear_islands(self):
        """6. Linear islands (horizontal or vertical strips)."""
        # Horizontal
        grid_h = [["1", "0", "1", "0", "1"]]
        self.run_test(grid_h, 3)
        
        grid_h_connected = [["1", "1", "1", "1", "1"]]
        self.run_test(grid_h_connected, 1)

        # Vertical
        grid_v = [["1"], ["0"], ["1"], ["0"], ["1"]]
        self.run_test(grid_v, 3)
        
        grid_v_connected = [["1"], ["1"], ["1"], ["1"], ["1"]]
        self.run_test(grid_v_connected, 1)

    def test_more_complex_shapes(self):
        """7. More complex shapes."""
        grid_complex = [
            ["1", "1", "0", "0", "1"],
            ["1", "0", "0", "1", "1"],
            ["0", "0", "1", "0", "0"],
            ["1", "1", "0", "1", "1"],
            ["0", "1", "0", "1", "0"]
        ] # Should be 6 islands
          # Island 1: (0,0),(0,1),(1,0)
          # Island 2: (0,4),(1,3),(1,4)
          # Island 3: (2,2)
          # Island 4: (3,0),(3,1),(4,1)
          # Island 5: (3,3),(3,4),(4,3)
          # Island 6: (4,4) - No, (4,3) connects to (3,3), (3,4)
          # Let's trace carefully:
          # (0,0) -> 1,1 ; 1,0. Island 1. Grid: [[0,0,0,0,1],[0,0,0,1,1]...]
          # (0,4) -> 1,3; 1,4. Island 2. Grid: [[0,0,0,0,0],[0,0,0,0,0]...]
          # (2,2) -> Island 3. Grid: [...,[0,0,0,0,0]...]
          # (3,0) -> 3,1; 4,1. Island 4. Grid: [...,[0,0,0,1,1],[0,0,0,1,0]]
          # (3,3) -> 3,4; 4,3. Island 5. Grid: [...,[0,0,0,0,0],[0,0,0,0,0]]
        self.run_test(grid_complex, 5) # Recalculated, it's 5 islands. (4,4) is part of island starting at (3,3)
        
        grid_u_shape = [
            ["1","0","1"],
            ["1","0","1"],
            ["1","1","1"]
        ]
        self.run_test(grid_u_shape, 1)

        grid_disconnected_parts = [
            ["1","0","0","1"],
            ["0","0","0","0"],
            ["1","0","0","1"]
        ]
        self.run_test(grid_disconnected_parts, 4)


    def test_edge_case_empty_grid(self):
        """8. Edge case: Empty grid []."""
        self.run_test([], 0)

    def test_edge_case_grid_with_empty_rows(self):
        """9. Edge case: Grid with empty rows (e.g. [[]]).
           The Solution's check `if not grid or not grid[0]:` handles this.
        """
        self.run_test([[]], 0) # A grid containing one empty row
        self.run_test([[],[]], 0) # A grid containing multiple empty rows (less common definition)

    def test_grid_with_internal_water_not_splitting_island(self):
        grid = [
            ["1","1","1"],
            ["1","0","1"],
            ["1","1","1"]
        ]
        self.run_test(grid, 1)

    def test_diagonal_not_connected(self):
        grid = [
            ["1","0","0"],
            ["0","1","0"],
            ["0","0","1"]
        ]
        self.run_test(grid, 3)

if __name__ == '__main__':
    unittest.main()
