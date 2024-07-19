import pygame
import sys
import random

# Dimensiones de la pantalla
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
MORADO = (144, 12, 247)

# Inicialización de pygame y creación de la ventana
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("WAZAAA")

# Configuración de fuentes para los mensajes de texto
font = pygame.font.SysFont("Arial", 50)

# Clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 10
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Tecla 'a' para mover a la izquierda
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  # Tecla 'd' para mover a la derecha
            self.rect.x += self.speed

        # Limitar el movimiento dentro de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Clase para los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(MORADO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)

# Clase para los proyectiles del jugador
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # Eliminar el proyectil si se sale de la pantalla
        if self.rect.bottom < 0:
            self.kill()

def show_message(text):
    """Función para mostrar un mensaje en la pantalla."""
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Pausa para mostrar el mensaje

def main():
    global all_sprites, enemies, bullets

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Crear el jugador
    player = Player()
    all_sprites.add(player)

    # Crear enemigos
    for i in range(8):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Reloj para controlar la velocidad de actualización de la pantalla
    clock = pygame.time.Clock()

    # Loop principal del juego
    running = True
    game_over = False
    while running:
        # Mantener el bucle a la velocidad de 60 frames por segundo
        clock.tick(60)

        # Procesar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Salir del juego si se presiona "Esc"
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    player.shoot()
                if game_over and event.key == pygame.K_RETURN:
                    main()  # Reiniciar el juego al presionar "Enter"
                    return

        if not game_over:
            # Actualizar
            all_sprites.update()

            # Colisiones: verificar si los proyectiles del jugador golpean a los enemigos
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                # Añadir nuevos enemigos tras ser destruidos
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)

            # Colisiones: verificar si los enemigos golpean al jugador
            hits = pygame.sprite.spritecollide(player, enemies, False)
            if hits:
                game_over = True
                show_message("¡Haz perdido!")

        # Dibujar / renderizar
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Mostrar mensaje de "Presiona Enter para volver a jugar" si el juego termina
        if game_over:
            show_message("Presiona 'Enter' para volver a jugar")

        # Actualizar la pantalla
        pygame.display.flip()

    # Salir de pygame
    pygame.quit()
    sys.exit()

main()
