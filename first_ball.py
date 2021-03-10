import pygame
import random

class Ball:
    def __init__(self, pos):
        self.pos = pos
        self.color = (random.randint(0, 255), random.randint(1, 255), random.randint(1, 255))
        pygame.draw.circle(screen, self.color, self.pos, 50)
        self.stop = False
        self.running = True
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
        if self.speed_x == 0 and self.speed_y == 0:
            self.speed_x, self.speed_y = random.randint(1, 5), random.randint(1, 5)

    def hmove(self):
        if self.pos[0] >= long - radius or self.pos[0] <= radius:
            self.speed_x = -self.speed_x
        self.pos = (self.pos[0] + self.speed_x, self.pos[1])

    def vmove(self):
        if self.pos[1] >= short - radius or self.pos[1] <= radius:
            self.speed_y = -self.speed_y
        self.pos = (self.pos[0], self.pos[1] + self.speed_y)

    def renew(self):
        pygame.draw.circle(screen, self.color, self.pos, radius)


pygame.init()

balls = []
radius = 50
FPS = 200
long = 900
short = 600
screen = pygame.display.set_mode((long, short))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = event.pos
                if pos[0] <= radius:
                    pos = (radius + 1, pos[1])
                elif pos[0] >= long - radius:
                    pos = (long - radius - 1, pos[1])
                if pos[1] <= radius:
                    pos = (pos[0], radius + 1)
                elif pos[1] >= short - radius:
                    pos = (pos[0], short - radius - 1)
                ball = Ball(pos)
                balls.append(ball)
            elif event.button == 3:
                if balls:
                    del balls[0]
    for ball in balls:
        ball.hmove()
        ball.vmove()
        ball.renew()
    pygame.display.flip()
    screen.fill((255, 0, 0))
    clock.tick(FPS)
pygame.quit()