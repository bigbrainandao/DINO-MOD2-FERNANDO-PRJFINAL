import pygame
import random
from dino_runner.utils.constants import DEATH_SOUND, DESTROY
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird()
        ]
        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0, 1)])
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)    
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    DEATH_SOUND.play()
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    game.update_score_rank()
                    break
                else:
                    DESTROY.play()
                    self.obstacles.remove(obstacle)

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
