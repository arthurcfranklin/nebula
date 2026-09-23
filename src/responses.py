from src.config import *



class Resposta:
    def __init__(self):
        pass

    def resposta(self, opcao):
        respostas = ""
        if opcao == '1':
            respostas = ("O Python é uma linguagem de programação usada "
                         "para desenvolver uma ampla variedade de aplicações, "
                         "como scripts automatizados, aplicações web, análise de dados, "
                         "inteligência artificial, aprendizado de máquina e muito mais.")
        elif opcao == '2':
            respostas = ("O Python é amplamente utilizado em ciência de dados, desenvolvimento "
                         "web, inteligência artificial, automação de tarefas, desenvolvimento "
                         "de APIs e aplicações de machine learning.")
        elif opcao == '3':
            respostas = ("Para operações matemáticas básicas, basta usar os operadores "
                         "(+, -, *, /) do Python. Para cálculos mais avançados, pode-se usar "
                         "a biblioteca math ou pacotes como numpy e scipy.")
        elif opcao == '4':
            respostas = ("Sim, é possível criar jogos com o Python! A biblioteca pygame, por exemplo, "
                         "é muito usada para desenvolver jogos 2D de forma simples e eficiente.")
        elif opcao == '5':
            respostas = "Até mais!"
            pygame.quit()
        else:
            respostas = "Desculpe, não entendi."

        return respostas
