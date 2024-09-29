from collections import Counter

import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x: float, y: float) -> "Player":
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.powerups = Counter(POWERUP_KINDS)
        
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, (0,255,0), self.triangle(), 2)
    
    def rotate(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt: int) -> None:
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt
        
    def shoot(self) -> None:
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED_BASE * (1+self.powerups["shot_speed"]/5)
        self.timer = PLAYER_SHOOT_COOLDOWN_BASE / self.powerups["shot_rate"]
        
    def update(self, dt: int) -> None:
        self.timer -= dt
        
        keys = pygame.key.get_pressed()        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
        if keys[pygame.K_ESCAPE]:
            exit()
        