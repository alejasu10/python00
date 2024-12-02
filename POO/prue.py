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

# Vehicle class
class Vehicle:
    def __init__(self, name, image_path, x, y):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))  # Resize the image
        self.x = x
        self.y = y

    def drive(self, dx, dy):
        """Mover el coche """
        self.x += dx
        self.y += dy

    def draw(self, surface):
        """Dibujar el coche """
        surface.blit(self.image, (self.x, self.y))


CAR_IMAGE_PATH = "POO/car.png"  

# Create a vehicle object
car = Vehicle("Coche 1", CAR_IMAGE_PATH, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# obstaculos
class Obstacle:
    def __init__(self, name, image_path, x, y):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100)) 
        self.x = x
        self.y = y
    def draw(self, surface):# dibiujar el obstaculo
        surface.blit(self.image, (self.x, self.y))
        #dibujar rectangulo
    def rect(self):
        self.rect = pygame.rect(self.x, self.y, self.image.get_width(), self.image.get_height())
class enemigo(Obstacle):
    def __init__(self, name, image_path, x, y):
        super().__init__(name, image_path, x, y)
        self.image = pygame.transform.scale(self.image, (50, 50))
        
    def draw(self, surface):# dibiujar el enemigo
        
        surface.blit(self.image, (self.x, self.y))
            
        
        
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

# colision de objetos

def check_collision(car, obstacle):
    car_rect = pygame.Rect(car.x, car.y, car.image.get_width(), car.image.get_height())
    obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.image.get_width(), obstacle.image.get_height())
    return car_rect.colliderect(obstacle_rect)
def check_collision_enemy(car,enemigo):
    car_rect = pygame.Rect(car.x, car.y, car.image.get_width(), car.image.get_height())
    enemy_rect = pygame.Rect(enemigo.x, enemigo.y, enemigo.image.get_width(), enemigo.image.get_height())
    return car_rect.colliderect(enemy_rect)


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
        if check_collision(car, roca,):
            print("has chocado con la roca!")
        elif check_collision_enemy(car, enemy):
            print("has chocado con el enemigo!")
        
        # Borrar el screen
        screen.fill(WHITE)

        # Dibujar el coche
        car.draw(screen)
        roca.draw(screen)
        roca2.draw(screen)
        roca3.draw(screen)
        enemy.draw(screen)

        # Actualizar todo que has sido dibujado
        pygame.display.flip()

        # Mantener el FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()