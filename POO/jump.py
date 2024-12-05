import pygame
import sys
import random

# codigo obligatorio para iniciar pygame
pygame.init()

# dimensiones de ka ventana
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("juego prueba")# nombre ne la ventana

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Frame rate
clock = pygame.time.Clock()
FPS =60

# Texto en la ventana
font = pygame.font.Font(None, 36)

#background 

class Background:# imagen de fondo
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    def draw(self, surface):# dibujo de la imagen
        surface.blit(self.image , (0, 0))
    
background_image = "POO/bottom.png"
bak= Background(background_image)

# creando los obstaculos
class Obstacle:
    def __init__(self, name, image_path, x, y=90):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))# rectangulo de colision
        self.rect.height = 20
        self.rect.width = 20# tamañop del rectangulo de colision
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.rect.center= (self.x, self.y)  # update rectangulo de colision
        
    def move(self, dx):
        self.x -= dx

# creando el personaje

class Personaje:
    def __init__(self, name, image_path, x, y):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.x = x
        self.y = y
        self.velocity = 5
        self.jump=False
        self.jumpcount=12# altura del salto
        self.rect = self.image.get_rect(center=(self.x, self.y))
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.rect.center = (self.x, self.y)

Pj_image= "POO/assets/1.png"
Pj=Personaje("personaje",Pj_image,180,100)

obstacle_image = "POO/assets/roca.png"
obstacle = Obstacle("obstacle", obstacle_image, 500)

def check_collision(pj, obstacle):
    return pj.rect.colliderect(obstacle.rect)


# Main game loop
def main():
    running = True
    count=0
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
        obstacle.move(6)
        if obstacle.x <0:
            obstacle.x = 800
        # Check for collision
        if check_collision(Pj, obstacle):
            print("has chocado con la roca!")
            running = False
        if obstacle.x == Pj.x+20:
            count +=1
            print(count)
        # Borrar el screen
        screen.fill(WHITE)
        bak.draw(screen)
        
        # Dibujar los objetos
        Pj.draw(screen)
        obstacle.draw(screen)
        
        # Dibujar el score
        score_text = font.render(f'Score: {count}', True, BLACK)
        screen.blit(score_text, (40, 20))
        
        
        # Actualizar todo que has sido dibujado
        pygame.display.flip()
        # Mantener el FPS
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()