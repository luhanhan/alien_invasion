import pygame


class SuperMario:

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load(r'D:\\Downloads\\Documents\\python_work\\alien_invasion\\images\\SuperMario.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)