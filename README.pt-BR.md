# Nebula

Minigame educacional desenvolvido com Python e Pygame como projeto acadêmico em equipe durante o curso Técnico em Desenvolvimento de Sistemas do SENAI.

<p align="center">
  <img src="docs/nebula-preview.png" alt="Menu do jogo Nebula" width="100%">
</p>

## Visão Geral

Nebula é um minigame educacional 2D desenvolvido para combinar mecânicas básicas de jogo com conceitos introdutórios de Python.

O jogador pode se movimentar pelo ambiente, entrar em uma área de interação e acessar um diálogo contendo perguntas sobre Python. Cada pergunta selecionada apresenta uma resposta educacional correspondente.

O projeto foi desenvolvido em equipe durante o curso Técnico em Desenvolvimento de Sistemas do SENAI, proporcionando experiência prática com Python, Pygame, tratamento de eventos, sprites e desenvolvimento de aplicações interativas.

## Funcionalidades

- Menu inicial interativo
- Movimentação 2D do jogador
- Sistema de interação por teclado
- Diálogo de perguntas e respostas
- Seleção de opções com o mouse
- Conteúdo educacional sobre Python
- Renderização de sprites e imagens com Pygame
- Game loop com controle de taxa de quadros

## Gameplay

Após iniciar o jogo pelo menu principal, o jogador pode navegar pelo ambiente e se aproximar da área de interação.

Quando o jogador alcança a zona de interação, pressionar `E` abre uma lista de perguntas sobre Python. As perguntas podem ser selecionadas com o mouse e a resposta correspondente é exibida no jogo.

O diálogo aborda tópicos como aplicações do Python, casos de uso comuns, operações matemáticas e desenvolvimento de jogos.

## Tecnologias

- **Python** — lógica do jogo e estrutura da aplicação
- **Pygame** — gráficos, sprites, tratamento de entradas e game loop

## Estrutura do Projeto

```text
nebula/
├── data/
│   ├── command_center.png
│   ├── command_room.png
│   ├── menu.png
│   └── player.png
├── docs/
│   └── nebula-preview.png
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── game.py
│   ├── player.py
│   └── responses.py
├── .gitignore
├── README.md
├── README.pt-BR.md
└── requirements.txt
```

## Como Executar

### Requisitos

- Python
- pip

### Clone o repositório

```bash
git clone https://github.com/arthurcfranklin/nebula.git
cd nebula
```

### Crie um ambiente virtual

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### Execute o jogo

```bash
python -m src.game
```

## Controles

| Entrada | Ação |
| --- | --- |
| `W` `A` `S` `D` | Movimentar o jogador |
| `E` | Interagir dentro da área de interação |
| Mouse | Selecionar opções do diálogo |

## Contexto Acadêmico

Nebula foi desenvolvido como projeto acadêmico em equipe durante o curso Técnico em Desenvolvimento de Sistemas do SENAI.

O projeto proporcionou experiência prática com Python e Pygame, explorando conceitos fundamentais como programação orientada a objetos, tratamento de eventos, movimentação do jogador, sprites, interação baseada em proximidade e interfaces interativas.

## Equipe

Nebula foi desenvolvido colaborativamente como projeto estudantil.

- Arthur Franklin
- Diana Drischel
- Euclides Rodrigues
- Leandro Valle

---

Desenvolvido como projeto acadêmico · [Read in English](README.md)
