def minesweeper(bomb):
    
    # Define array dimension 
    ROWS = len(bomb)
    COLS = len(bomb[0])

    # Convert all "-" into int(0)
    for row in range(ROWS):
        for col in range(COLS):
            if bomb[row][col] == "-":
                bomb[row][col] = 0
    
    for row in range(ROWS):

        for col in range(COLS):
            
            # Increment all adjacent value
            # if value is not a mine
            if bomb[row][col] == "#":
                
                # Top boundary, row cannot be less or equal to 0
                if row > 0:
                    if bomb[row-1][col] != "#":
                        bomb[row-1][col] +=1
                
                # Bottom boundary, row cannot be greater or equal to last ROW-1
                if row < ROWS-1:
                    if bomb[row+1][col] !="#":
                        bomb[row+1][col] +=1

                # Left boundary, col cannot be less or equal to 0
                if col > 0:
                    if bomb[row][col-1] != "#":
                        bomb[row][col-1] +=1
                
                # Right boundary, col cannot be greater or equal to last COL-1
                if col < COLS-1:
                    if bomb[row][col+1] != "#":
                        bomb[row][col+1] +=1

                # Top left corner boundary, row and col cannot be less or equal to 0
                if row > 0 and col > 0:
                    if bomb[row-1][col-1] != "#":
                        bomb[row-1][col-1] +=1

                # Top right corner boundary, row cannot be less or equal to 0 and col cannot be greater or equal to last COL-1
                if row > 0 and col < COLS-1:
                    if bomb[row-1][col+1] != "#":
                        bomb[row-1][col+1] +=1
                
                # Bottom left corner boundary, row cannot be greater or equal to last ROW-1 and col cannot be less or equal to 0
                if row < ROWS-1 and col > 0:
                    if bomb[row+1][col-1] != "#":
                        bomb[row+1][col-1] +=1
                
                # Bottom right corner boundary, row and col cannot be greater or equal to last ROW-1 and COL-1
                if row < ROWS-1 and col < COLS-1:
                    if bomb[row+1][col+1] != "#":
                        bomb[row+1][col+1] +=1
    
    # Convert each item in bomb as a string
    bomb = [list(map(str, item)) for item in bomb]
    
    return bomb

bomb = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

print(minesweeper(bomb))