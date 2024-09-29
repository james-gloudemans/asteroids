import random

import pygame

from powerup import Powerup
from constants import *

class PowerupField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        
    def spawn(self, position: pygame.Vector2, velocity: pygame.Vector2, kind: int):
        powerup = Powerup(position.x, position.y, kind)
        powerup.velocity = velocity
        
    def update(self, dt: int) -> None:
        self.spawn_timer += dt
        if self.spawn_timer > POWERUP_SPAWN_RATE:
            self.spawn_timer = 0
            # spawn a new powerup at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity: pygame.Vector2 = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position: pygame.Vector2 = edge[1](random.uniform(0, 1))
            kind = random.choice(POWERUP_KINDS)
            self.spawn(position, velocity, kind)