from src.config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(join('data/player.png')).convert_alpha()
        self.rect = self.image.get_rect(center=pos)


        self.direção = pygame.Vector2(0, 0)
        self.velocidade = 300

    def input(self):

        keys = pygame.key.get_pressed()
        self.direção.x = keys[pygame.K_d] - keys[pygame.K_a]
        self.direção.y = keys[pygame.K_s] - keys[pygame.K_w]

        if self.direção.length() > 0:
            self.direção = self.direção.normalize()

    def move(self, dt):
        # Calcule o novo centro do jogador
        novo_centro_x = self.rect.centerx + self.direção.x * self.velocidade * dt
        novo_centro_y = self.rect.centery + self.direção.y * self.velocidade * dt

        # Verifique as colisões com as bordas da tela
        if novo_centro_x < self.rect.width // 2:  # Verifica a colisão com a parede esquerda
            novo_centro_x = self.rect.width // 2
        elif novo_centro_x > largura - self.rect.width // 2:  # Verifica a colisão com a parede direita
            novo_centro_x = largura - self.rect.width // 2

        if novo_centro_y < self.rect.height // 2:  # Verifica a colisão com a parte superior
            novo_centro_y = self.rect.height // 2
        elif novo_centro_y > altura - self.rect.height // 2:  # Verifica a colisão com a parte inferior
            novo_centro_y = altura - self.rect.height // 2

        # Atualiza a posição do jogador
        self.rect.center = (novo_centro_x, novo_centro_y)

    def update(self, dt):
        self.input()
        self.move(dt)
