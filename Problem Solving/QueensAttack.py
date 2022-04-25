

def available_tiles(size, queen_row, queen_column, obstacles):
    rows_up = size-queen_row
    columns_right = size-queen_column
    columns_left = queen_column-1
    rows_down = queen_row-1
    diagonal_up_right= min(rows_up, columns_right)
    diagonal_down_right = min(rows_down, columns_right)
    diagonal_down_left = min(rows_down, columns_left)
    diagonal_up_left = min(rows_up, columns_left)

    for o in obstacles:
        o_row = o[0]
        o_col = o[1]
        if o_row == queen_row:
            if o_col < queen_column:
                columns_left = min(columns_left, columns_left-o_col)
            else:
                columns_right = min(columns_right, o_col - queen_column -1)
        elif o_col == queen_column:
            if o_row < queen_row:
                rows_down = min(rows_down, rows_down-o_row)
            else:
                rows_up = min(rows_up, o_row-queen_row-1)
        elif abs(o_row - queen_row) == abs(o_col - queen_column):
            if o_col < queen_column:
                if o_row < queen_row:
                    diagonal_down_left = min(diagonal_down_left, queen_column-o_col-1)
                else:
                    diagonal_up_left = min(diagonal_up_left, queen_column-o_col-1)
            else:
                if o_row < queen_row:
                    diagonal_down_right = min(diagonal_down_right, o_col-queen_column-1)
                else:
                    diagonal_up_right = min(diagonal_up_right, o_col-queen_column-1)

    # Naive solution:
    # 
    # for i in range(rows_up):
    #     tile = [queen_row+i+1, queen_column]
    #     if tile not in obstacles:
    #         available_tiles+=1
    #     else:
    #         break
    # for i in range(min(rows_up, columns_right)):
    #     tile = [queen_row+i+1, queen_column+i+1]
    #     if tile not in obstacles:
    #         available_tiles+=1
    #     else:
    #         break
    # for i in range(columns_right):
    #     tile = [queen_row, queen_column+i+1]
    #     if tile not in obstacles:
    #         available_tiles+=1
    #     else:
    #         break
    # for i in range(min(columns_right, rows_down)):
    #     tile = [queen_row-i-1, queen_column+i+1]
    #     if tile not in obstacles:
    #         available_tiles+=1
    #     else:
    #         break

    # for i in range(rows_down):
    #     tile = [queen_row-i-1, queen_column]
    #     if tile not in obstacles:
    #         available_tiles+=1
    #     else:
    #         break
    # for i in range(min(rows_down, columns_left)):
    #     tile = [queen_row-i-1, queen_column-i-1]
    #     if tile not in obstacles:
    #         available_tiles+=1
    #     else:
    #         break
    # for i in range(columns_left):
    #     tile = [queen_row, queen_column-i-1]
    #     if tile not in obstacles:
    #         available_tiles+=1
    #     else:
    #         break
    # for i in range(min(columns_left, rows_up)):
    #     tile = [queen_row+i+1, queen_column-i-1]
    #     if tile not in obstacles:
    #         available_tiles+=1
    #     else:
    #         break
    return rows_down + rows_up + columns_left + columns_right + diagonal_up_right +diagonal_up_left + diagonal_down_right + diagonal_down_left



if __name__ == "__main__":
    size, tests = list(map(int, input().split()))
    queen_row, queen_column = list(map(int, input().split()))
    obstacles = []
    for i in range(tests):
        obstacle = list(map(int, input().split()))
        obstacles.append(obstacle)
    result = available_tiles(size, queen_row, queen_column, obstacles)
    print(result)