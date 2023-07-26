import pygame
import pygame.sprite

class Piece(pygame.sprite.Sprite):
    def __init__(self, cell_size=100, pos=(0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.circle_radius = (cell_size/2) - 5
        self.speed = 10

        #basic colours
        BLACK = (0, 0, 0)  # RGB for black
        WHITE = (255, 255, 255)  # RGB for white

        self.image = pygame.Surface([cell_size, cell_size])
        self.image.fill(BLACK)

        pygame.draw.rect(self.image, BLACK, (0, 0, cell_size, cell_size), 2)

        self.rect = self.image.get_rect(center=pos)

    def draw_player_colour(self, player):
        #player colours
        RED = (255, 0, 0)  # RGB for red
        YELLOW = (255, 255, 0)  # RGB for yellow

        if player == 1:
            colour = RED
        else:
            colour = YELLOW

        pygame.draw.circle(self.image, colour, (self.circle_radius, self.circle_radius), self.circle_radius, 3)

    def add_to_group(self, group, moving_group):
        moving_group.add(self)
        self.moving_group = moving_group
        self.static_group = group
        
    def piece_movement(self, screen_height):
        self.rect.y += self.speed
        hits = pygame.sprite.spritecollide(self, self.static_group, False)
        if hits or self.rect.bottom >= screen_height:
            self.rect.y -= self.speed
            self.speed = 0
            self.static_group.add(self)
            self.moving_group.remove(self)

"""
For parts outside this one

all_sprites = pygame.sprite.Group()

"""