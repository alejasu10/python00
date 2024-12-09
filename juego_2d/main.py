import pygame
import sys
import random
import pantalla as pant

# codigo obligatorio para iniciar pygame
pygame.init()

# dimensiones de ka ventana
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
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
background_image_1 = pygame.image.load("/juego_2d/assets/Background1.png")
background_image_2 = pygame.image.load("/juego_2d/assets/Background2.png")
background_image_3 = pygame.image.load("/juego_2d/assets/Background3.png")
background_image_4 = pygame.image.load("/juego_2d/assets/Background4.png")
bak_1= pant.Background(background_image_1)
bak_2= pant.Background(background_image_2)
bak_3= pant.Background(background_image_3)
bak_4= pant.Background(background_image_4)
# Main game loop
def main():
    running = True
    count=0
    while running:
        
        
        # Check for collision
        # Borrar el screen
        screen.fill(WHITE)
        bak_1.draw(screen)
        bak_2.draw(screen,(500,0))
        bak_3.draw(screen,(1000,0))
        bak_4.draw(screen,(1500,0))
        
        # Dibujar los objetos
        
        
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