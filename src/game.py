# Importando os módulos de configuração e classes específicas que são utilizados no projeto:

from src.config import *
from src.player import Player # Importa o personagem
from src.responses import Resposta # Importa o sistema de respostas
import pygame # Importa o usada para gerar os elementos gráficos

# Fundo do jogo:
fundo = pygame.image.load('data/command_center.png') # Carrega a imagem de fundo utilizada no projeto

# Classe para o menu, que gerencia a tela inicial do projeto:
class Menu:
    def __init__(self, display_surface): #Inicializa o menu
        self.display_surface = display_surface  # Recebe a superfície de exibição
        self.imagem_menu = pygame.image.load('data/menu.png')  # Exibe a imagem do menu inicial
        self.rodando = True # Indica que o menu está em execução
        self.jogar_rect = pygame.Rect(largura // 2 - 300, altura // 2 + 110, 280, 100)  # Define a área do botão JOGAR
        self.sair_rect = pygame.Rect(largura // 2 + 20, altura // 2 + 110, 285, 100)  # Define a área do botão SAIR

    def run(self): # Exibe o menu em loop enquanto aguarda a interação do usuário.

        while self.rodando: # Esse loop continua executando o projeto enquanto self.rodando for True, mantendo o menu ativo até a interação do usuário para começar ou encerrar.
            for event in pygame.event.get(): # Pega todos os eventos possíveis ocorridos (como cliques por exemplo) em uma lista e os processa).
                if event.type == pygame.QUIT: # Verifica se o evento atual é de "fechar"
                    self.rodando = False # Define como false interrompendo o loop e encerrando o menu caso o usuário feche a janela
                if event.type == pygame.MOUSEBUTTONDOWN: # Verifica se houve clique no mouse
                    pos = pygame.mouse.get_pos() # Armazena a posição do mouse durante o clique do usuário
                    if self.jogar_rect.collidepoint(pos): # Verifica se a posição do clique está dentro da área definida para JOGAR
                        return True  # Se o usuário clicou no botão JOGAR o método run retorna True e indica que o projeto deve iniciar
                    elif self.sair_rect.collidepoint(pos):# Verifica se o clique ocorreu dentro da área do botão SAIR
                        return False  # O método retorna False, indicando que o menu deve ser encerrado e o jogo não será iniciado.

            # Desenhando os elementos visuais do menu na tela:
            self.display_surface.blit(self.imagem_menu, (0, 0)) # A superfície principal onde tudo é desenhado com o método blit e a definição da imagem utilizada indicada na variável
            pygame.draw.rect(self.display_surface, (255, 0, 0), self.jogar_rect, -1)  # Superfície onde o botão para jogar é desenhado, entre parênteses está definido o código das cores usadas
            pygame.draw.rect(self.display_surface, (255, 0, 0), self.sair_rect, -1)    # Superfície onde o botão para sair é desenhado, entre parênteses está definido o código das cores usadas
# o -1 indica que a cor preenche o retângulo completamente.
            pygame.display.update() # Atualiza a tela, exibindo as mudanças que foram feitas (imagem de fundo e retângulos dos botões).




# A principal classe que contém toda a lógica do jogo:

class Game:
    def __init__(self): # Esse método define a construção da classe Game, com tudo o que será configurado e inicializado
        pygame.init() # Inicializa todos os módulos do Pygame e configura a biblioteca a ser usada
        self.display_surface = pygame.display.set_mode((largura, altura)) # Cria as janelas do projeto com suas dimensões e as armazena
        pygame.display.set_caption('Nebula') # Define o título da janela
        self.clock = pygame.time.Clock() # Cria um objeto Clock que controla a taxa de atualização do jogo e mantëm a mesma consistente
        self.rodando = True # Define uma variável rodando, que controla se o jogo está em execução e mantëm o loop principal ativo

        # Carrega o jogador
        posicao_inicial = (largura // 6, altura // 1)  # Define a posição inicial do jogador
        self.player = Player(posicao_inicial) # Cria uma instância do Player na posição definida

        # Grupo de sprites
        self.sprites = pygame.sprite.Group(self.player) # Cria o grupo de sprites e adiciona o Player ao grupo

        # Criando o retângulo que representa a área na tela onde o jogador pode interagir. Esse retângulo tem coordenadas e dimensões específicas que definem sua posição e tamanho.
        self.zona_interacao = pygame.Rect(largura // 20 - 15, altura // 2 - 30, 508, 196)

        # resposta
        self.resposta = Resposta() #  Gera respostas às perguntas do jogador.
        self.exibindo_resposta = False # Define que inicialmente não há uma resposta sendo exibida.
        self.resposta_texto = ""  # Inicializa como uma string vazia, onde será armazenado o texto da resposta selecionada.

        # Opções de diálogo
        self.opcoes = [] # Inicializa uma lista vazia para armazenar as opções de perguntas que serão exibidas
        self.fonte = pygame.font.Font(None, 36)  # Deine a fonte e o tamanho do texto que será utilizado

    def verificar_interacao(self):
        return self.player.rect.colliderect(self.zona_interacao) # Verifica se o jogador está na zona de interação


# Armazenando as perguntas nas opções:

    def exibir_opcoes(self):
        perguntas = [
            "Para que serve o Python?",
            "Onde o Python é mais utilizado?",
            "Quais as ferramentas necessárias para operações matemáticas?",
            "Podemos criar um jogo com o Python?",
            "Encerrar a conversa"
        ]
        self.opcoes = perguntas

    def desenhar_opcoes(self):
        y_offset = altura // 2 - 50   # Posição vertical inicial das opções
        for opcao in self.opcoes: # Itera sobre as opções de diálogo
            texto = self.fonte.render(opcao, True, (255, 255, 255)) # Renderiza o texto
            self.display_surface.blit(texto, (largura // 10 - 150, y_offset)) # Exibe o texto na tela
            y_offset += 40  # Move para a próxima opção vertical

    def desenhar_resposta(self): # Dividir a resposta em linhas

        max_largura = 500  # Largura máxima da resposta
        palavras = self.resposta_texto.split(' ') # Divide a resposta em palavras
        linhas = [] # Lista que armazena cada linha da resposta
        linha_atual = "" # Inicializa a variável linha_atual como uma string vazia

        for palavra in palavras: # Verificar se adicionar a palavra atual excede a largura máxima
            largura_linha, _ = self.fonte.size(linha_atual + palavra + ' ') #  Calcula a largura da linha atual
            if largura_linha <= max_largura:
                linha_atual += palavra + ' ' # Adiciona a palavra a linha
            else:
                linhas.append(linha_atual)  # Adicionar a linha atual à lista de linhas
                linha_atual = palavra + ' '  # Começar uma nova linha com a palavra atual

        # Adicionar a última linha se houver
        if linha_atual:
            linhas.append(linha_atual)

        # Desenhar cada linha na tela
        y_offset = altura // 2 + 100  # Posição inicial para desenhar a resposta
        for linha in linhas:
            texto_resposta = self.fonte.render(linha, True, (255, 255, 0))
            self.display_surface.blit(texto_resposta, (largura // 2 - 250, y_offset))  # Ajuste a posição conforme necessário
            y_offset += self.fonte.get_height()  # Mover para baixo para a próxima linha



# Definindo o método run da classe Game:


    def run(self):
        menu = Menu(self.display_surface)  # Cria uma instância da classe Menu e passa self.display_surface (a superfície de exibição) como parâmetro para que o menu possa desenhar seus elementos na tela.
        start_game = menu.run() # Executa o método run do menu, exibindo o menu e espera uma interação do jogador
        if not start_game:  # Se o jogador escolher sair encerra o jogo o fechando
            pygame.quit() # Retorna False caso o jogador opte por sair
            return




# Loop principal:

        while self.rodando: # O loop principal do jogo, que continua enquanto self.rodando for True.
            dt = self.clock.tick(60) / 1000  # Define a taxa de atualização do jogo para 60 frames por segundo e calcula o "delta time" (dt).

            # Loop de eventos
            for event in pygame.event.get(): # Processa todos os eventos (cliques, teclas, etc.) que ocorreram desde o último quadro.
                if event.type == pygame.QUIT: # Se o evento é de fechamento de janela, define self.rodando como False, encerrando o loop e o jogo.
                    self.rodando = False
                if event.type == pygame.KEYDOWN: # Verifica se uma tecla foi pressionada.
                    if event.key == pygame.K_e and self.verificar_interacao(): # Se a tecla "E" foi pressionada e o jogador está na zona de interação, chama self.exibir_opcoes() para exibir opções de diálogo.
                        self.exibir_opcoes()
                        self.exibindo_resposta = True

                if event.type == pygame.MOUSEBUTTONDOWN and self.exibindo_resposta: # Verifica se houve um clique do mouse e se as opções de diálogo estão sendo exibidas.
                    pos = pygame.mouse.get_pos() # Armazena a posição do clique do mouse
                    y_offset = altura // 2 - 50  # Define o deslocamento vertical inicial para verificar a posição das opções de diálogo.
                    for i in range(len(self.opcoes)): # Verifica se o clique está em uma das opções de diálogo.
                        # Verifique se o mouse está sobre a opção
                        if y_offset < pos[1] < y_offset + 40:
                            self.resposta_texto = self.resposta.resposta(str(i + 1))
                            print(self.resposta_texto)  # Exibir no console se necessário
                            if i + 1 == 5:  # Se a opção 5 for selecionada
                                self.rodando = False # Encerra o jogo
                            self.exibindo_resposta = False # Para de exibir opções
                            break
                        y_offset += 40



            # Atualizando os elementos gráficos:

            self.sprites.update(dt)     # Atualiza todos os sprites com base no tempo decorrido (dt)
            self.display_surface.blit(fundo, (0, 0)) # Desenha o fundo da sala de comando partindo do canto superior esquerdo (0 e 0)
            self.sprites.draw(self.display_surface) # Desenha todos os sprites na superfície de exibição

            pygame.draw.rect(self.display_surface, (0, 0, 0), self.zona_interacao, -1) # Desenha a zona de interação como um retângulo preto preenchido

            if self.exibindo_resposta: # Se as opções de diálogo estão sendo exibidas, chama self.desenhar_opcoes(), do contrario chama self.desenhar_respostas()
                self.desenhar_opcoes()
            else:
                self.desenhar_resposta()  # Desenha a resposta quando não estiver exibindo as opções

            pygame.display.update() #Comando que atualiza a tela para que as mudanças feitas nesse ciclo sejam exibidas

        pygame.quit() # Encerra o Pygame e fecha o projeto.


if __name__ == '__main__': # Se o script for executado diretamente (não importado), ele cria uma instância de Game e chama o método run para iniciar o jogo.
    game = Game()
    game.run()
