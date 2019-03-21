import Square
import Constants

class Grid:

    def __init__(self, x_pos, y_pos):
        # use a list to store all components of a grid
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.square_lst = []
        self.ship_lst = []
        self.hit_lst = []

        # create squares
        for row in range(1,11):
            for col in "ABCDEFGHIJ":
                sq = Square.Square(x_pos, y_pos, (col, row)) # create a new Square object
                self.square_lst.append(sq) # append it to the list of squares
                x_pos += Constants.LENGTH; # set the x-coor of the next square
            x_pos = self.square_lst[0].x_pos # prepare for the next row
            y_pos += Constants.LENGTH

    def initialize(self):
        self.draw_grid()
        self.draw_horizontal_indices()
        self.draw_vertical_indices()

    def draw_grid(self):
        for obj in self.square_lst:
            obj.draw_square()

    def draw_horizontal_indices(self):
        import View
        import pygame
        pygame.init()

        # set the font of letters
        font = pygame.font.SysFont("arial", 25)

        # make local variables
        x_pos = self.x_pos + 9  # numbers tested, no modification please
        y_pos = self.y_pos - 35  # numbers tested, no modification please

        # render text
        for letter in Constants.LETTER_INDICES:
            label = font.render(letter, 1, (0, 0, 128))  # text: blue
            View.screen.blit(label, (x_pos, y_pos))
            pygame.display.flip()
            x_pos += Constants.LENGTH

    def draw_vertical_indices(self):
        import View
        import pygame
        pygame.init()

        # set the font of letters
        font = pygame.font.SysFont("arial", 25)

        # make local variables
        x_pos = self.x_pos - 30  # numbers tested, no modification please
        y_pos = self.y_pos + 3  # numbers tested, no modification please
        for num in Constants.NUMBER_INDICES:
            label = font.render(str(num), 1, (0, 0, 128))  # text: blue
            View.screen.blit(label, (x_pos, y_pos))
            pygame.display.flip()
            y_pos += Constants.LENGTH



    def print_ship_lst(self):
        print("ships: ", self.ship_lst)



    def print_hit_lst(self):
        print("hits: ", self.hit_lst)



    def rand_initialize_ship_lst(self):
        import View
        import random

        length = len(View.player_grid.ship_lst)
        index_lst = []
        num_lst = list(range(0, 100))

        '''since there is chance that the random generator gives same numbers,
           we want to append the number if it is not generated before.
           In other words, we want distinct numbers from the range.
        '''

        while len(index_lst) < length:
            rand_num = random.choice(num_lst)
            if rand_num not in index_lst:
                index_lst.append(rand_num)
                # remove the number so that the computer won't select same objects
            num_lst.remove(rand_num)

        # append the coordinate in ship_lst
        for i in index_lst:
            self.ship_lst.append(self.square_lst[i].idt) # append idt, not the object

        # print the list of ships of the opponent (randomized)
        print(self.ship_lst)

    def mark_ships(self):
        # mark the selected squares as ships
        for idt in self.ship_lst:
            for obj in self.square_lst:
                if obj.idt == idt:
                    obj.mark_ship()

    def fill_ship_squares(self):
        '''
        Given a list of idt and fill the squares of the given list
        :return:
        '''

        for idt in self.ship_lst:
            for obj in self.square_lst:
                if obj.idt == idt:
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

