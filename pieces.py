import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * 80 + 80 // 2
        self.y = self.row * 80 + 80 // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = 80//2 - self.PADDING
        pygame.draw.circle(win, (128,128,128), (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, (255,255,255) if self.color == 'white' else (0,255,255), (self.x, self.y), radius)
        if self.king:
            font = pygame.font.SysFont('arial', 24)
            crown = font.render('S', True, (255, 215, 0))
            win.blit(crown, (self.x - crown.get_width()//2, self.y - crown.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return f'{self.color[0].upper()}K' if self.king else f'{self.color[0].upper()}'
