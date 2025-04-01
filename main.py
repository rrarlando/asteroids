import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
  pygame.init()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)

  AsteroidField.containers = (updatable)

  Player.containers = (updatable, drawable)

  Shot.containers = (shots, updatable, drawable)

  AsteroidField()

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

  game_over = False

  while not game_over:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return

     screen.fill("black")

     for item in drawable:
        item.draw(screen)

     updatable.update(dt)

     for asteroid in asteroids:
        if asteroid.check_collision(player):
           print("Game over!")
           game_over = True

     pygame.display.flip()

     dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()

