import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import Powerup
from powerupfield import PowerupField

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
    powerups = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Powerup.containers = (powerups, updatables, drawables)
    PowerupField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    powerup_field = PowerupField()
    
    
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
                    print(f"Game over!  Final score: {score}")
                    exit()
                else:
                    lives_text = game_font.render(f'Extra Lives: {lives}', False, (255,255,255))
                    for powerup in player.powerups.keys():
                        if player.powerups[powerup]:
                            player.powerups[powerup] -= 1
                    player.position = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                    player.rotation = 0
                    for obj in drawables:
                        if not obj is player:
                            obj.kill()
                    asteroid_field = AsteroidField()
                    powerup_field = PowerupField()
            for shot in shots:
                if asteroid.collides_with(shot):
                    score += 10
                    score_text = game_font.render(f'Score: {score}', False, (255,255,255))
                    asteroid.split()
                    shot.kill()
        for powerup in powerups:
            if powerup.collides_with(player):
                powerup.kill()
                if player.powerups[powerup.kind] <= 3:
                    player.powerups[powerup.kind] += 1
                

        screen.blit(score_text, (TEXT_PADDING,0))
        screen.blit(lives_text, (SCREEN_WIDTH - (lives_text.get_width() + TEXT_PADDING), 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()