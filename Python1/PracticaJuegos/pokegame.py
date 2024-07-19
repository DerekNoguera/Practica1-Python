import pygame
import sys

# Inicialización de pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego estilo Pokémon")

# Colores
CHARACTER_COLOR = (0, 0, 255)  # Color azul para el personaje
HEAD_COLOR = (255, 255, 0)  # Color amarillo para la cabeza

# Cargar y redimensionar la imagen de fondo
background_image = pygame.image.load("character.png").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Dimensiones y posición del personaje
character_x = SCREEN_WIDTH // 2
character_y = SCREEN_HEIGHT // 2
head_radius = 10
body_length = 20

# Velocidad de movimiento
character_speed = 1

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover el personaje usando W, A, S, D
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Izquierda
        character_x -= character_speed
    if keys[pygame.K_d]:  # Derecha
        character_x += character_speed
    if keys[pygame.K_w]:  # Arriba
        character_y -= character_speed
    if keys[pygame.K_s]:  # Abajo
        character_y += character_speed

    # Limitar el movimiento a la pantalla
    character_x = max(head_radius, min(SCREEN_WIDTH - head_radius, character_x))
    character_y = max(head_radius + body_length, min(SCREEN_HEIGHT, character_y))

    # Dibujar la pantalla
    screen.blit(background_image, (0, 0))  # Dibujar el fondo

    # Dibujar la cabeza
    pygame.draw.circle(screen, HEAD_COLOR, (character_x, character_y - body_length), head_radius)

    # Dibujar el cuerpo (línea vertical)
    pygame.draw.line(screen, CHARACTER_COLOR, (character_x, character_y - body_length), (character_x, character_y), 2)

    # Dibujar los brazos (línea horizontal)
    pygame.draw.line(screen, CHARACTER_COLOR, (character_x - 10, character_y - 10), (character_x + 10, character_y - 10), 2)

    # Dibujar las piernas (líneas diagonales)
    pygame.draw.line(screen, CHARACTER_COLOR, (character_x, character_y), (character_x - 10, character_y + 10), 2)
    pygame.draw.line(screen, CHARACTER_COLOR, (character_x, character_y), (character_x + 10, character_y + 10), 2)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
