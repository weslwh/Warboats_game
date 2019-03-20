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