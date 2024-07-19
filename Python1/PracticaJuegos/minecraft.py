# import pygame
# import sys


# ANCHO = 800
# ALTO = 600
# TAMANIOBLOQUE = 40


# VERDE = (34, 177, 76)
# MARRON = (139, 69, 19)
# AZUL = (0, 162, 232)


# pygame.init()
# pantalla = pygame.display.set_mode((ANCHO, ALTO))
# pygame.display.set_caption("Juego Estilo Minecraft")


# mapa = [[0 for _ in range(ANCHO // TAMANIOBLOQUE)] for _ in range(ALTO // TAMANIOBLOQUE)]

# def dibujarmapa():
#     for y in range(len(mapa)):
#         for x in range(len(mapa[y])):
#             if mapa[y][x] == 1:
#                 pygame.draw.rect(pantalla, MARRON, (x * TAMANIOBLOQUE, y * TAMANIOBLOQUE, TAMANIOBLOQUE, TAMANIOBLOQUE))
#             elif mapa[y][x] == 2:
#                 pygame.draw.rect(pantalla, VERDE, (x * TAMANIOBLOQUE, y * TAMANIOBLOQUE, TAMANIOBLOQUE, TAMANIOBLOQUE))
# dibujarmapa()
# def main():
#     reloj = pygame.time.Clock()
#     seleccionado = 1  # 1 para marrón, 2 para verde
#     while True:
#         pantalla.fill(AZUL)
#         dibujarmapa()
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif evento.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()
#                 x //= TAMANIOBLOQUE
#                 y //= TAMANIOBLOQUE
#                 if evento.button == 1:  # Click izquierdo para colocar
#                     mapa[y][x] = seleccionado
#                 elif evento.button == 3:  # Click derecho para eliminar
#                     mapa[y][x] = 0
#             elif evento.type == pygame.KEYDOWN:
#                 if evento.key == pygame.K_1:
#                     seleccionado = 1
#                 elif evento.key == pygame.K_2:
#                     seleccionado = 2

#         pygame.display.flip()
#         reloj.tick(60)

# if __name__ == "__main__":
#     main()

# ////////////////////////////////////////////////////


import pygame   
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]


aristas = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]
arista = aristas[0]
vertice1 = vertices[arista[0]]
vertice2 = vertices[arista[1]]
print(f"La arista {arista} conecta los vértices {vertice1} y {vertice2}.")

caras = [
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
]
cara = caras[0]
vertices_de_cara = [vertices[indice] for indice in cara]
print(f"La cara {cara} está formada por los vértices {vertices_de_cara}.")

colores = [
    (2, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1)
]

def Cubo():
    glBegin(GL_QUADS)
    for i, cara in enumerate(caras):
        glColor3fv(colores[i])
        for vertice in cara:
            glVertex3fv(vertices[vertice])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    for arista in aristas:
        for vertice in arista:
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Controles para rotar el cubo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            glRotatef(1, 0, 1, 0)
        if keys[pygame.K_RIGHT]:
            glRotatef(-1, 0, 1, 0)
        if keys[pygame.K_UP]:
            glRotatef(1, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotatef(-1, 1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cubo()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()