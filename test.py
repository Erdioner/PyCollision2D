import pygame
import PyCollision2D as pycol

pygame.init()
display = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

moving_rect = pycol.Rect(pycol.Vector(10, 10), pycol.Vector(50, 50))
static_rect = pycol.Rect(pycol.Vector(100, 100), pycol.Vector(100, 100))
velocity = pycol.Vector(0, 0)
speed = 1

while True:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pressedKeys = pygame.key.get_pressed()
    velocity = pycol.Vector(
        (pressedKeys[pygame.K_RIGHT] - pressedKeys[pygame.K_LEFT]) * speed,
        (pressedKeys[pygame.K_DOWN] - pressedKeys[pygame.K_UP]) * speed
    )


    velocity = moving_rect.resolve_dynamic_collision_with_rect(static_rect, velocity)
    moving_rect.pos += velocity

    p_moving_rect = moving_rect.create_pygame_rect_from_rect()
    p_static_rect = static_rect.create_pygame_rect_from_rect()

    pygame.draw.rect(display, (200, 0, 0), p_static_rect)
    pygame.draw.rect(display, (0, 200, 0), p_moving_rect)

    clock.tick(60)
    pygame.display.update()
