import random

import pygame

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
        
    def draw(self, screen: pygame.Surface) -> None:
        if self.position.x > SCREEN_WIDTH + ASTEROID_MAX_RADIUS:
            self.position.x = 0
        if self.position.y > SCREEN_HEIGHT + ASTEROID_MAX_RADIUS:
            self.position.y = 0
        if self.position.x < -ASTEROID_MAX_RADIUS:
            self.position.x = SCREEN_WIDTH
        if self.position.y < -ASTEROID_MAX_RADIUS:
            self.position.y = SCREEN_HEIGHT
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
        
    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
        
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = v1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2.velocity = v2 * 1.2
