# ************ Compulsory Task 1 ************

''' This program creates a function that takes a grid of # and -, where 
each hash (#) represents a mine and each dash (-) represents a 
mine-free spot and returns a grid, where each dash is replaced by a 
digit, indicating the number of mines immediately adjacent to the 
mine-free spot i.e. (horizontally, vertically, and diagonally). '''

# Assign the Grid Input.
grid = [ [ "-", "-", "-", "#", "#" ],
        [ "-", "#", "-", "-", "-" ],
        [ "-", "-", "#", "-", "-" ],
        [ "-", "#", "#", "-", "-" ],
        [ "-", "-", "-", "-", "-" ] ]

def count_mines(grid):
    ''' Define indeces of cells adjecent to a mine-free cell in a grid 
    (8 cells adjecent to each mine-free cell: vertical, horizontal, 
    and diagonal).ai is the adjecent indeces. '''
    ai = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Get the number of rows in a grid.
    rows = len(grid)
    # Get the number of columns in the grid.
    cols = len(grid[0])
    
    # Define a function to count mines adjacent to a mine-free spot.
    def adjacent_mines(x, y):
        # Define the mine count and start it at zero.
        mine_count = 0
        # Create a for loop to iterates over each adjecent cell.
        for aix, aiy in ai:
            ''' Define indeces adjecent to the current cell. nai is new 
             adjacent index for both x and y.'''
            naix, naiy = x + aix, y + aiy
            ''' Check if indeces of adjacent cells are within bounds of 
            the grid and if adjacent cells are assigned # indicating 
            that it is a mine.'''
            if 0 <= naix < rows and 0 <= naiy < cols and grid[naix][naiy] == '#':
                # Add the mine count if condition above is satisfied.
                mine_count += 1
        return mine_count
    
    # Define a new grid to store the result.
    result_grid = []

    # Iterate through the grid using enumerate to get row and column indices.
    for i, row in enumerate(grid):
        # Define an empty row list to store new row values.
        result_row = []
        # Iterate over the values of the current row.
        for j, value in enumerate(row):
            # Append # to empty row list so mines are unchanged in final grid.
            if value == '#':
                result_row.append('#')
            else:
                # Find mines adjacent using adjacent_mines function.
                mine_count = adjacent_mines(i, j)
                # Add mine count (as a string) to the result_row list.
                result_row.append(str(mine_count))
        # Build up the final grid row by row.
        result_grid.append(result_row)
    return result_grid

# Get the result
result = count_mines(grid)

print("New grid = [")
# Print the result grid
for row in result:
    print(row)
print("]")
