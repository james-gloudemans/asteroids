import pygame

from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
    
    def rotate(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt: int) -> None:
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt
        
        
        
    def update(self, dt: int) -> None:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        