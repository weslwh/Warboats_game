import Constants
import pygame
import time



def check_on_board(x, y):
    '''
    check_on_board() returns a number 1,2, or 0 based on whether the
    values of x and y are in a specific range

    Args:
        x: A int from 100 to 900

        y: A int from 100 to 400
        
        Returns:
            int 1, 2, or 0
        
        Raises:
            void
    '''
    if y >= 100 and y <= 400:
        # 1 represents player's grid
        if x >= 100 and x <= 400:
            return 1
        # 2 represents opponents's grid
        elif x >= 600 and x <= 900:
            return 2
        # other positions: invalid
        else:
            return 0


def check_player_coor(x, y):
    '''
    This function returns the indices if a click is on the player's grid.
    :param x:
    :param y:
    :return:
    '''
    x_index = (x - 100) // Constants.LENGTH
    y_index = (y - 100)// Constants.LENGTH
    return (Constants.LETTER_INDICES[x_index], Constants.NUMBER_INDICES[y_index])


def check_oppo_coor(x, y):
    '''
    This function returns the indices if a click is the on opponent's grid.
    :param x:
    :param y:
    :return:
    '''
    x_index = (x - 600) // Constants.LENGTH
    y_index = (y - 100) // Constants.LENGTH
    return (Constants.LETTER_INDICES[x_index], Constants.NUMBER_INDICES[y_index])


def get_click_info(x, y):
    '''
    This function simply prints a message for each click. Further modifications
    are expected.
    :param x:
    :param y:
    :return:
    '''
    mesg = check_on_board(x, y)
    if mesg == 0:
        print("Invalid position")
    elif mesg == 1:  # 1 represents player's grid
        print("Click on player's grid. Coordinate: ", check_player_coor(x, y))
    elif mesg == 2:  # 2 represents opponents's grid
        print("Click on opponents's grid. Coordinate: ", check_oppo_coor(x, y))


def fill_square(x, y):
    import View

    ''' This function takes pixel coordinates and first: determine which board 
        should fill on and second: fill the square on that board
    '''
    # Click on the player's grid
    if check_on_board(x, y) == 1:
        sq_idt = check_player_coor(x, y)
        for obj in View.player_grid.square_lst:
            if obj.idt == sq_idt:
                # fill the square to 'hit'
                obj.fill_square_as_ship()
    elif check_on_board(x, y) == 2:
        sq_idt = check_oppo_coor(x, y)
        for obj in View.oppo_grid.square_lst:
            if obj.idt == sq_idt:
                # fill the square to 'hit'
                obj.fill_square_as_ship()



def get_rand_square(lst):
    import random
    '''
    This function takes a list and return a random object in that list.
    Once an object is selected, it will not be selected again. That is,
    all objects selected from this function are distinct.
    '''
    num_lst = list(range(0, 100))
    rand_num = random.choice(num_lst)
    # remove the number so that the computer won't select same objects
    num_lst.remove(rand_num)
    return lst[rand_num]
pygame.init()
enemy_font = pygame.font.SysFont('Comic Sans MS', 30)
enemy_text = enemy_font.render('Enemy', False,Constants.BLACK)
player_font = pygame.font.SysFont('Comic Sans MS', 30)
player_text = player_font.render('Friendly', False, Constants.BLACK)
def start():
    import View
    import Grid
    import pygame
    pygame.init()
    View.screen.blit(player_text, (200, 20))
    View.screen.blit(enemy_text, (670,20))
    pygame.display.update()
    while not Constants.USER_QUIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Constants.USER_QUIT = True

            # start the deployment process
            if Constants.SHIP_DEPLOYED == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()

                    # OPTIONAL: print the info of the click
                    # get_click_info(x, y)

                    # check whether the user clicks on its own grid
                    if check_on_board(x, y) == 1:
                        # append the selected squares in this.ship_lst
                        if check_player_coor(x, y) not in View.player_grid.ship_lst:
                            View.player_grid.ship_lst.append(check_player_coor(x, y))
                        # Fill the square
                        fill_square(x, y)

                    # print the coors that is selected as ships
                    View.player_grid.print_ship_lst()

                if event.type == pygame.KEYDOWN:
                    # ship deployment process finished
                    Constants.SHIP_DEPLOYED = True

                    # mark the player's selected squares as ships
                    View.player_grid.mark_ships()

                    # randomly initialize opponent's ship positions
                    View.oppo_grid.rand_initialize_ship_lst()

                    # mark the opponent's selected squares as ships
                    View.oppo_grid.mark_ships()

                    # show opponent's ships for test uses
                    # later deletion needed

                    View.oppo_grid.fill_ship_squares()


            else: # SHIP_DEPLOYED = True, guessing starts
                if event.type == pygame.MOUSEBUTTONDOWN:

                    x, y = pygame.mouse.get_pos() # hit positions

                    if check_on_board(x, y) == 2: # user clicks on the opponent's grid
                        idt = check_oppo_coor(x, y) # get the idt of the square of this click
                        if idt not in View.oppo_grid.hit_lst: # if the position hasn't been hit before
                            for sq in View.oppo_grid.square_lst:
                                if sq.idt == idt:  # determine the square object as sq
                                    sq.is_hit = True  # mark the position as hit
                                    View.oppo_grid.hit_lst.append(sq)  # append the position to hit_lst
                                    # mark its color
                                    if sq.is_ship == True:
                                        sq.fill_square_as_hit()
                                        # if a ship is hit, remove it from the ship_lst
                                        if sq.idt in View.oppo_grid.ship_lst:
                                            View.oppo_grid.ship_lst.remove(sq.idt)
                                    else:
                                        sq.fill_square_as_miss();
                    # Delay gord here
                    time.sleep(2)
                    
                    # get a random square object from player's grid
                    obj = get_rand_square(View.player_grid.square_lst)
                    if obj.is_ship == True:
                        obj.fill_square_as_hit()
                    else:
                        obj.fill_square_as_miss()


                    # Check winners
                    if View.oppo_grid.ship_lst == []:
                        import pygame
                        pygame.init()
                        font = pygame.font.SysFont("arial", 72)
                        text_surface = font.render("Congratulations!! You Win!!", True,(255,0,0))
                        View.screen.fill(Constants.WHITE)
                        View.screen.blit(text_surface,((Constants.SCREEN_SIZE[0])/6,(Constants.SCREEN_SIZE[1])//2))
                        pygame.display.update()
                        # pops a window up then exit the pygame

                    if View.player_grid.ship_lst == []:
                        import pygame
                        pygame.init()
                        font = pygame.font.SysFont("arial", 72)
                        text_surface = font.render("Game Over!! Computer Wins!!", True,(255,0,0))
                        View.screen.fill(Constants.WHITE)
                        View.screen.blit(text_surface,((Constants.SCREEN_SIZE[0])/6,(Constants.SCREEN_SIZE[1])//2))
                        pygame.display.update()
                        # pops a window up then exit the pygame
                        
                    else:
                        # for later message instructions
                         mesg = "Invalid position. Please click on the opponent's grid"

                '''
                elif event.type == pygame.KEYDOWN: # press any key to shift to computer's turn
                    # get a random square object from player's grid
                    obj = get_rand_square(View.player_grid.square_lst)
                    if obj.is_ship == True:
                        obj.fill_square_as_hit()
                    else:
                        obj.fill_square_as_miss()

                    if View.player_grid.ship_lst == []:
                        import pygame
                        pygame.init()
                        font = pygame.font.SysFont("arial", 72)
                        text_surface = font.render("Gameover Computer Win!!", True,(255,0,0))
                        View.screen.fill(Constants.WHITE)
                        View.screen.blit(text_surface,((Constants.SCREEN_SIZE[0])/6,(Constants.SCREEN_SIZE[1])//2))
                        # pops a window up then exit the pygame


                '''
