import pygame
import main as m
class Background:# imagen de fondo
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (m.SCREEN_WIDTH,m.SCREEN_HEIGHT))
    def draw(self, surface):# dibujo de la imagen
        surface.blit(self.image , (0, 0))