#Generates an editable 4x4 grid of 0's.

import os

def clear():
    os.system('clear')

grid = [ ]

def print_grid(grid):
    for i in range(len(grid)):
        print(" ".join([str(x) for x in grid[i]]))

for i in range(4):
    grid.append(["0"] * 4)

print_grid(grid)

while True:
    try:
        col = int(input("X: "))
        row = int(input("Y: "))
        if grid[row][col] == "0":
            grid[row][col] = " "
        else:
            grid[row][col] = "0"
    except IndexError:
        print("One or more values is out of range.")
        continue
    except ValueError:
        print("Please input a whole number.")
        continue
    except:
        print("There was an error.")
        continue
