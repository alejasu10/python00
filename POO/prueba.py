import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame prueba")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Frame rate
clock = pygame.time.Clock()
FPS =60



# creando los obstaculos
class Obstacle:
    def __init__(self, name, image_path, x, y):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))  # Add this line
    
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)  # Update rect position

# creando el carro
class Vehicle:
    def __init__(self, name, image_path, x, y):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y)) 

    def drive(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)  # Update rect position

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        

CAR_IMAGE_PATH = "POO/car.png"  

# Create a vehicle object
car = Vehicle("Coche 1", CAR_IMAGE_PATH, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


# creando el enemigo
class enemigo(Obstacle):
    def __init__(self, name, image_path, x, y):
        super().__init__(name, image_path, x, y)
        self.image = pygame.transform.scale(self.image, (50, 50))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)
    
    #dandole movimiento al enemigo
    def move(self, dx, dy):
        self.x = dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)

# Update collision detection functions
def check_collision(car, obstacle):
    return car.rect.colliderect(obstacle.rect)

def check_collision_enemy(car, enemy):
    return car.rect.colliderect(enemy.rect)

roca_path = "POO/roca.jpg"
random_x = random.randint(0, SCREEN_WIDTH - 100)
random_y = random.randint(0, SCREEN_HEIGHT - 100)

roca = Obstacle("Roca", roca_path, random_x, random_y)


random_x = random.randint(0, SCREEN_WIDTH - 100)
random_y = random.randint(0, SCREEN_HEIGHT - 100)

roca2 = Obstacle("Roca", roca_path, random_x, random_y)

random_x = random.randint(0, SCREEN_WIDTH - 100)
random_y = random.randint(0, SCREEN_HEIGHT - 100)

roca3 = Obstacle("Roca", roca_path, random_x, random_y)


enemy_path = "POO/moto.png"
random_x = random.randint(0, SCREEN_WIDTH - 100)
random_y = random.randint(0, SCREEN_HEIGHT - 100)
enemy= enemigo("enemigo", enemy_path, random_x, random_y)



# Main game loop
def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle keys for car movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            car.drive(0, -5)  # Move up
        if keys[pygame.K_DOWN]:
            car.drive(0, 5)  # Move down
        if keys[pygame.K_LEFT]:
            car.drive(-5, 0)  # Move left
        if keys[pygame.K_RIGHT]:
            car.drive(5, 0)  # Move right

        # Check for collision
        if check_collision(car, roca):
            print("has chocado con la roca!")
        elif check_collision_enemy(car, enemy):
            print("has chocado con el enemigo!")
        elif check_collision(car, roca2):
            print("has chocado con la roca!")
        elif check_collision(car, roca3):
            print("has chocado con la roca!")
        
        # Borrar el screen
        screen.fill(WHITE)

        # Dibujar el coche
        car.draw(screen)
        roca.draw(screen)
        roca2.draw(screen)
        roca3.draw(screen)
        enemy.draw(screen)
        
        enemy.move(0, 5)
        if enemy.y > 800:
            enemy.y = 5
    
        # Actualizar todo que has sido dibujado
        pygame.display.flip()

        # Mantener el FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()