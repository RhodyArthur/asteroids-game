import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, duration=0.5, max_radius=40):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.duration = duration
        self.elapsed = 0
        self.max_radius = max_radius

    def update(self, dt):
        self.elapsed += dt
        if self.elapsed > self.duration:
            self.kill()

    def draw(self, screen):
        progress = min(self.elapsed / self.duration, 1)
        radius = int(self.max_radius * progress)
        if radius > 0:
            pygame.draw.circle(screen, (255, 200, 50), self.position, radius, 2)
            pygame.draw.circle(screen, (255, 100, 0), self.position, radius // 2, 1)