import pygame
pygame.init()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 30
        self.board = [[0] * (self.width // self.cell_size) for i in range(self.height // self.cell_size)]

    def render(self):
        x, y = 0, 0
        for i in range(self.height // self.cell_size):
            for j in range(self.width // self.cell_size):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size))
                x += self.cell_size
            y += self.cell_size
            x = 0

    def on_click(self, x, y):
        i = x // self.cell_size
        j = y // self.cell_size
        self.board[i][j] = 1

    def off_click(self, x, y):
        i, j = x // self.cell_size, y // self.cell_size
        self.board[i][j] = 0


x, y = 170, 230
screen = pygame.display.set_mode((x, y))
main_board = Board(x, y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                main_board.on_click(event.pos[1], event.pos[0])
            elif event.button == 3:
                main_board.off_click(event.pos[1], event.pos[0])
    screen.fill((0, 0, 0))
    main_board.render()
    pygame.display.flip()