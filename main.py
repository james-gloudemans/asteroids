from sys import exit
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    game_font = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()
    dt: int = 0
    score: int = 0
    score_text = game_font.render(f'Score: {score}', False, (255,255,255))
    lives = 3
    lives_text = game_font.render(f'Extra Lives: {lives}', False, (255,255,255))
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for obj in updatables:
            obj.update(dt)
        for obj in drawables:
            obj.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                lives -= 1
                if lives <= 0:
                    print("Game over!")
                    exit()
                else:
                    lives_text = game_font.render(f'Extra Lives: {lives}', False, (255,255,255))
                    for obj in drawables:
                        obj.kill()
                    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                    field = AsteroidField()
            for shot in shots:
                if asteroid.collides_with(shot):
                    score += 10
                    score_text = game_font.render(f'Score: {score}', False, (255,255,255))
                    asteroid.split()
                    shot.kill()

        screen.blit(score_text, (TEXT_PADDING,0))
        screen.blit(lives_text, (SCREEN_WIDTH - (lives_text.get_width() + TEXT_PADDING), 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()