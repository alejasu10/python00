import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("juego prueba")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Frame rate
clock = pygame.time.Clock()
FPS =60

#background 

class Background:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self, surface):
        surface.blit(self.image , (0, 0))
    
background_image = "POO/bottom.png"
bak= Background(background_image)

# creando los obstaculos
class Obstacle:
    def __init__(self, name, image_path, x, y=90):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(20, 20))  # rectangulo de colision
    
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.rect.topleft= (self.x, self.y)  # Update rect position
        
    def move(self, dx):
        self.x -= dx

# creando el persoonaje

class Personaje:
    def __init__(self, name, image_path, x, y):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.x = x
        self.y = y
        self.jump=False
        self.jumpcount=12# altura del salto
        self.rect = self.image.get_rect(topleft=(x, y)) 


    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)

Pj_image= "POO/assets/1.png"
Pj=Personaje("personaje",Pj_image,300,100)

obstacle_image = "POO/assets/roca.png"
obstacle = Obstacle("obstacle", obstacle_image, 700)


def check_collision(pj, obstacle):
    return pj.rect.colliderect(obstacle.rect)


# Main game loop
def main():
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle keys for car movement
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE] and not Pj.jump:# salto
            Pj.jump = True
        
        if Pj.jump:# salto
                Pj.y -= Pj.jumpcount 
                Pj.jumpcount -= 1
                if Pj.jumpcount < -12:#gravedad
                    Pj.jump = False
                    Pj.jumpcount = 12
        obstacle.move(3)
        if obstacle.x <0:
            obstacle.x = 800
        # Check for collision
        if check_collision(Pj, obstacle):
            print("has chocado con la roca!")
        
        # Borrar el screen
        screen.fill(WHITE)
        bak.draw(screen)
        

        # Dibujar los objetos
        Pj.draw(screen)
        obstacle.draw(screen)

        # Actualizar todo que has sido dibujado
        pygame.display.flip()

        # Mantener el FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()