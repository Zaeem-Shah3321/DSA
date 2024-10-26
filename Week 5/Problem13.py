def add_row(grid, row):
    grid.append(row)

def add_column(grid, column):
    for i in range(len(grid)):
        if i < len(column):
            grid[i].append(column[i])
        else:
            grid[i].append(0)

def display_grid(grid):
    for row in grid:
        print(row)

def sum_of_elements(grid):
    total_sum = 0
    for row in grid:
        total_sum += sum(row)
    return total_sum

def main():
    grid = []

    add_row(grid, [1, 2, 3])
    add_row(grid, [4, 5, 6])
    add_row(grid, [7, 8, 9])
    
    print("Grid after adding rows:")
    display_grid(grid)

    add_column(grid, [10, 11, 12])
    print("Grid after adding a column:")
    display_grid(grid)

    total_sum = sum_of_elements(grid)
    print("Sum of all elements in the grid:", total_sum)

if __name__ == "__main__":
    main()
