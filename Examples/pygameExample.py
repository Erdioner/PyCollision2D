from Module.rect import Rect
from Module.vector import Vector
import pygame

pygame.init()

display = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

movingRect = Rect(Vector(50, 50), Vector(50, 50))
projectedMovementRect = Rect(Vector(100, 50), Vector(50, 50))
unalteredProjectedMovementRect = Rect(Vector(300, 300), Vector(50, 50))
staticRect = Rect(Vector(200, 200), Vector(100, 100))

speed = 5

while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pressedKeys = pygame.key.get_pressed()
    unalteredProjectedMovementRect.pos.x += (pressedKeys[pygame.K_RIGHT] - pressedKeys[pygame.K_LEFT]) * speed
    unalteredProjectedMovementRect.pos.y += (pressedKeys[pygame.K_DOWN] - pressedKeys[pygame.K_UP]) * speed

    movingRect.pos.x += (pressedKeys[ord('d')] - pressedKeys[ord('a')]) * speed
    movingRect.pos.y += (pressedKeys[ord('s')] - pressedKeys[ord('w')]) * speed

    unalteredVelocity = Vector(
        unalteredProjectedMovementRect.pos.x - movingRect.pos.x,
        unalteredProjectedMovementRect.pos.y - movingRect.pos.y
    )

    velocity, contact_point, contact_normal, t_hit_near, t_hit_far = movingRect.resolve_velocity_dynamic_collision_with_rect(
        staticRect,
        unalteredVelocity
    )

    projectedMovementRect.pos.x = velocity.x + movingRect.pos.x
    projectedMovementRect.pos.y = velocity.y + movingRect.pos.y

    pygame.draw.rect(display, (0, 150, 0), pygame.Rect(movingRect.pos.x, movingRect.pos.y, movingRect.size.x, movingRect.size.y))
    pygame.draw.rect(display, (0, 0, 255), pygame.Rect(unalteredProjectedMovementRect.pos.x, unalteredProjectedMovementRect.pos.y, unalteredProjectedMovementRect.size.x, unalteredProjectedMovementRect.size.y), width=1)
    pygame.draw.rect(display, (0, 255, 0), pygame.Rect(projectedMovementRect.pos.x, projectedMovementRect.pos.y, projectedMovementRect.size.x, projectedMovementRect.size.y), width=1)
    pygame.draw.rect(display, (150, 0, 0), pygame.Rect(staticRect.pos.x, staticRect.pos.y, staticRect.size.x, staticRect.size.y))

    if contact_point:
        pygame.draw.circle(display, (255, 255, 0), (contact_point.x, contact_point.y), 5)
    pygame.draw.line(display, (255, 255, 255), (movingRect.pos.x+movingRect.size.x/2, movingRect.pos.y+movingRect.size.y/2), (projectedMovementRect.pos.x+projectedMovementRect.size.x/2, projectedMovementRect.pos.y+projectedMovementRect.size.y/2))
    pygame.draw.line(display, (255, 255, 255), (movingRect.pos.x+movingRect.size.x/2, movingRect.pos.y+movingRect.size.y/2), (unalteredProjectedMovementRect.pos.x+unalteredProjectedMovementRect.size.y/2, unalteredProjectedMovementRect.pos.y+unalteredProjectedMovementRect.size.y/2))

    pygame.display.update()

    clock.tick(60)
