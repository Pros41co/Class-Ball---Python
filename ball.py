import pygame
import random
from sys import exit



class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.orientation_x = 1
        self.orientation_y = 1
        self.move_x = 9
        self.move_y = 8
        self.image = pygame.Surface((10,10), pygame.SRCALPHA)
        self.rect = self.image.get_rect(midbottom=(250, 250))

        self.draw_ball()

    def draw_ball(self):
        pygame.draw.circle(self.image, (230, 249, 0), (5, 5), 5)

    def move_ball(self):
        self.rect.x += self.move_x * self.orientation_x
        self.rect.y += self.move_y * self.orientation_y

        if self.rect.right >= 500 or self.rect.left <= 0:
            self.orientation_x *= -1
            self.move_x += random.uniform(-0.5, 0.5)


        if self.rect.top <= 0 or self.rect.bottom >= 490:
            self.orientation_y *= -1
            self.move_y += random.uniform(-0.5, 0.5)

        self.move_x = max(2, min(self.move_x, 9))
        self.move_y = max(2, min(self.move_y, 9))




    def update(self):
        self.move_ball()


def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    state_game = True

    ball_group = pygame.sprite.GroupSingle(Ball())

    while state_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        screen.fill((250, 250, 250))
        ball_group.update()
        ball_group.draw(screen)

        pygame.display.update()
        clock.tick(60)




if __name__ == "__main__":
    main()
