import Constants


def check_on_board(x, y):
    if y >= 100 and y <= 400:
        if x >= 100 and x <= 400:
            return 1
        elif x >= 600 and x <= 900:
            return 2
        else:
            return 0    


def check_player_coor(x, y):
    x_index = (x - 100) // Constants.LENGTH
    y_index = (y - 100) // Constants.LENGTH
    return (Constants.LETTER_INDICES[x_index], 
            Constants.NUMBER_INDICES[y_index])

def check_oppo_coor(x, y):
    x_index = (x - 600) // Constants.LENGTH
    y_index = (y - 100) // Constants.LENGTH
    return (Constants.LETTER_INDICES[x_index], 
            Constants.NUMBER_INDICES[y_index])

def get_click_info(x, y):
    mesg = check_on_board(x, y)
    if mesg == 0:
        print("invalid position")
    elif mesg == 1:
        print("Click on the player's grid. Coordinate ",
              check_player_coor(x, y))
    elif mesg == 2:
        print("Click on the opponent's grid. Coordinate ",
              check_oppo_coor(x, y))   

def fill_square(x, y):
    import View
    
    # Click on the player's grid
    if check_on_board(x, y) == 1:
        sq_idt = check_player_coor(x, y)
        for obj in View.player_grid.square_lst:
            if sq_idt == obj.idt:
                # fill the square
                obj.fill_square()
                
    # Click on the opponent's grid
    if check_on_board(x, y) == 2:
        sq_idt = check_oppo_coor(x, y)
        for obj in View.oppo_grid.square_lst:
            if sq_idt == obj.idt:
                # fill the square
                obj.fill_square()        

