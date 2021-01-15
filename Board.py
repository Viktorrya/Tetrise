import pygame
from Shape import Shape


class Board:
    # создание поля
    def __init__(self):
        self.width = 500
        self.height = 800
        self.board = [[0] * self.width for _ in range(self.height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 50

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, self.shape.color,
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
                                      self.cell_size, self.cell_size))

    def start(self, mouse_pos):
        if mouse_pos[0] > self.left + self.cell_size * self.width \
                or mouse_pos[1] > self.top + self.cell_size * self.height \
                or mouse_pos[0] < self.left or mouse_pos[1] < self.top:
            return False
        self.shape = Shape()
        return True

    def change_field(self):
        self.board = [[0] * self.width for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.shape.cells:
                    self.board[i][j] = 1


