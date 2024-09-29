import pygame

from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    
    def __init__(self, x: float, y: float) -> "Shot":
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255,0,0), self.position, self.radius, 2)
        
    def update(self, dt: int) -> None:
        self.position += self.velocity * dt