import Constants

import pygame
pygame.init()

class Square:

    def __init__(self, x_pos, y_pos, idt):
        # initialize the start_pos and coor of a Square
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.start_pos = (x_pos, y_pos)
        self.idt = idt # e.g. idt = (A, 3) or (H, 5)
        self.is_ship = False
        self.is_hit = False

    def draw_square(self):
        import View

        pygame.draw.rect(View.screen, Constants.BLACK, (self.x_pos, self.y_pos,
                        Constants.LENGTH, Constants.LENGTH), Constants.LINE_WIDTH)
                        # LINE_THICKNESS


    def fill_square_as_ship(self):
        '''
        This function takes a Square object and fill it
        :return:
        '''
        import View

        pygame.draw.rect(View.screen, Constants.SILVER, (self.x_pos + 2, self.y_pos + 2,
                         Constants.LENGTH - 4, Constants.LENGTH - 4), 0)
        pygame.display.update()

    def fill_square_as_hit(self):
        import View
        # square will turn green if you hit a ship
        pygame.draw.rect(View.screen, Constants.LIGHT_GREEN, (self.x_pos + 2, self.y_pos + 2,
                         Constants.LENGTH - 4, Constants.LENGTH - 4), 0)
        pygame.display.update()


    def fill_square_as_miss(self):
        import View
        # square will turn red if you hit a ship
        pygame.draw.rect(View.screen, Constants.TOMATO, (self.x_pos + 2, self.y_pos + 2,
                         Constants.LENGTH - 4, Constants.LENGTH - 4), 0)
        pygame.display.update()



    def mark_ship(self):
        self.is_ship = True
        # test that ships are successfully marked
        # print("a ship is marked ture")