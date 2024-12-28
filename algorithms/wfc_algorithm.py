# Wave function collapse algorithm
from grid import Grid
import parameters
from algorithms.wfc_cell import WFCCell
# 1 - See
# 2 - Sand
# 3 - Field
# 4 - Forest
# 5 - Mountain

# The posibilitys of each cell are gona be represented this way:
# Place : (North, East, South, West)
# Keys  : (0    , 1   , 2    , 3   )

# The base function:
# some = {
#     1 : ([1, 2], [1, 2], [1, 2], [1, 2]),
#     2 : ([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]),
#     3 : ([2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]),
#     4 : ([3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5]),
#     5 : ([4], [4], [4], [4]),
# }

# This can be used for test c:
some = {
    1 : ([1, 2], [1, 2], [1, 2], [1, 2]),
    2 : ([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]),
    3 : ([2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]),
    4 : ([3, 4, 5], [3, 4, 5], [3, 4, 5], [3, 4, 5]),
    5 : ([4, 5], [4, 5], [4, 5], [4, 5]),
}

# This for now it's only going to work with ihis first 5 colors (they will be hardcoded)
class WFCAlgorithm:
    def __init__(self, grid):
        self.grid = grid

        posibilities = [1, 2, 3, 4, 5]

        self.cells = [[WFCCell(row, col, posibilities) for col in range(parameters.columns)] for row in range(parameters.rows)]

    def get_lowest_entropy(self):
        min_entropy = float('inf')
        min_position = (-1, -1)
        for row in self.cells:
            for cell in row:
                if cell.entropy < min_entropy and cell.collapsed == False:
                    min_entropy = cell.entropy
                    min_position = (cell.row, cell.column)
        return min_position

    def update_neighbors(self, pos):
        # Ask to every neighbor to update using this cell as reference
        cell_posibilities = self.cells[pos[0]][pos[1]].posibilities
        # North
        if pos[0] - 1 >= 0 and not self.cells[pos[0]-1][pos[1]].collapsed:
            self.update_cell((pos[0]-1, pos[1]), cell_posibilities, 0)
        # East
        if pos[1] + 1 < parameters.columns and not self.cells[pos[0]][pos[1]+1].collapsed:
            self.update_cell((pos[0], pos[1]+1), cell_posibilities, 1)
        # South
        if pos[0] + 1 < parameters.rows and not self.cells[pos[0]+1][pos[1]].collapsed:
            self.update_cell((pos[0]+1, pos[1]), cell_posibilities, 2)
        # West
        if pos[1] - 1 >= 0 and not self.cells[pos[0]][pos[1]-1].collapsed:
            self.update_cell((pos[0], pos[1]-1), cell_posibilities, 3)

    def update_cell(self, pos, update_posibilities, direction):
        # Use the before cell direction posibilities to made a new list of posibilities
        direction_posibilities = []
        # For if it not collapsed
        for posibility in update_posibilities:
            for direction_posibility in some[posibility][direction]:
                if direction_posibility not in direction_posibilities:
                    direction_posibilities.append(direction_posibility)
                    
        cell_posibilities = self.cells[pos[0]][pos[1]].posibilities
        before_entropy = self.cells[pos[0]][pos[1]].entropy

        # Get the posibilities that match from the direction posibilities and the actual cell the posibilities
        match_posibilities = []
        for i in cell_posibilities:
            if i in direction_posibilities:
                match_posibilities.append(i)

        self.cells[pos[0]][pos[1]].posibilities = match_posibilities
        # Collapse if it has only one posibility
        if len(match_posibilities) == 1:
            self.cells[pos[0]][pos[1]].collapse

        self.cells[pos[0]][pos[1]].entropy = len(match_posibilities)
        if before_entropy != self.cells[pos[0]][pos[1]].entropy:
            self.update_neighbors(pos)


# *entropy = number of posibilities of a system
# *collapse = reduce the posibilities of a system to one
# Let's see, in each iteration we're gonna get the cell with the lowest entropy
# Then we're gonna collapse it to a random posibility
# Then we're gonna asign the posibilities to the neighbors accordingly (recurivily if the neighbors entropy changes)
# Then change the grid acordingly

    def update(self):
        
        # Get the cell with the lowest entropy
        lowest_entropy = self.get_lowest_entropy()
        # Collapse it into a random posibility
        self.cells[lowest_entropy[0]][lowest_entropy[1]].collapse()
        # Asign the posibilities to the neighbors
        self.update_neighbors(lowest_entropy)
        # Change the grid acordingly to the changes
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.cells[row][col].collapsed:
                    self.grid[row][col] = self.cells[row][col].posibilities[0]