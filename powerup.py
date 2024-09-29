import pygame

from circleshape import CircleShape
from constants import *

class Powerup(CircleShape):
    
    color_map = {POWERUP_KINDS[0]: (255,100,100), POWERUP_KINDS[1]: (100,255,100)}
    
    def __init__(self, x: float, y: float, kind) -> "Powerup":
        super().__init__(x, y, POWERUP_RADIUS)
        self.kind = kind
        self.color = self.color_map[kind]
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)
        
    def update(self, dt: int) -> None:
        self.position += self.velocity * dt