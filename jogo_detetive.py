import random
import textwrap
from rich.console import Console
import time 

def centralizar_texto(console, texto, largura=155, estilo="white", justify="center"):
    """Centraliza o texto na tela, usando o módulo Rich para formatação."""
    console.print(textwrap.fill(texto, width=largura), justify=justify, style=estilo)

def mostrar_mapa(console):
    """Exibe o mapa do zoológico no console."""
    mapa = (
        "MAPA \n"
        "+" + "-" * 65 + "+\n"
        "|       Entrada        | Praça de Alimentação   | Jaula do Cervo  |\n"
        "|----------------------|------------------------|-----------------|\n"
        "| Jaula do Macaco      |                        | Jaula do Leão   |\n"
        "|----------------------|     Cabana Central     |-----------------|\n"
        "| Jaula do Elefante    |                        | Jaula do Tigre  |\n"
        "|----------------------|----------------------- |-----------------|\n"
        "| Jaula do Rinoceronte |  Jaula do Hipopótamo   | Banheiros       |\n"
        "+" + "-" * 65 + "+\n"
    )
    console.print(mapa, style="bold", justify="center")

def mostrar_titulo(console):
    console = Console()  # Inicializa o console Rich
    console.print("\n\n+---------------------------------------------+", style="bold green", justify="center")  # Exibe o título do jogo
    console.print("|     FERA OCULTA: O MISTERIO NO ZOOLOGICO    |", style="bold green", justify="center")  # Exibe o título do jogo
    console.print("+---------------------------------------------+\n", style="bold green", justify="center")  # Exibe o título do jogo


def aleatorizar_cenario():
    """Retorna um número aleatório entre 1 e 3, representando diferentes cenários do jogo."""
    return random.randint(1, 3)

def definir_animais():
    """Define os animais do zoológico e seleciona um animal morto e um possível assassino."""
    animais = ["leão", "elefante", "hipopótamo", "tigre", "rinoceronte", "macaco", "cervo"]
    random.shuffle(animais)  # Embaralha a lista de animais

    # Define o animal morto e o assassino
    animal_morto = animais[0]
    assassino = animais[1]
    animal_1 = animais[2]
    animal_2 = animais[3]
    animal_3 = animais[4]
    animal_4 = animais[5]
    animal_5 = animais[6]

    # Retorna o animal morto, o assassino e os outros animais
    return animal_morto, assassino, animal_1, animal_2, animal_3, animal_4, animal_5

def mostrar_texto_cenario(console, cenario, animal_morto, assassino):
    """Exibe a descrição do cenário de acordo com o animal morto e o assassino."""
    if cenario == 1:
        texto = (
            f"Em uma manhã ensolarada no Zoológico da Cidade, a alegria dos visitantes se transformou em pânico quando"
            f" o {animal_morto} foi encontrado flutuando no Lago dos Hipopótamos. Os cuidadores isolaram a área, "
            f"levantando questões sobre como o {assassino} havia chegado até ali. Qual animal matou o {animal_morto}?\n"
        )
    elif cenario == 2:
        texto = (
            f"Em uma noite de tempestade no Zoológico da Cidade, o {animal_morto} foi encontrado na área da Praça de "
            f"alimentação com algumas marcas de mordida. Os cuidadores ficaram intrigados, pois não era claro se o "
            f"{assassino} agiu sozinho ou em parceria. Quem matou o {animal_morto}?\n"
        )
    else:
        texto = (
            f"Em uma noite chuvosa no Zoológico da Cidade, o silêncio da madrugada foi interrompido por gritos de pavor"
            f" dos vigilantes. Ao investigar, o {animal_morto} foi encontrado próximo ao banheiro, com sinais de ter"
            f" sido envenenado. Os cuidadores, perplexos, bloquearam o local para descobrir como o {assassino}"
            f" conseguiu colocar o veneno. Qual animal envenenou o {animal_morto}?\n"
        )

    centralizar_texto(console, texto)  # Centraliza e exibe o texto do cenário

def definir_dicas(cenario, animal_morto, assassino, animal_1, animal_2, animal_3, animal_4, animal_5):
    """Define as dicas disponíveis para cada cenário."""
    if cenario == 1:
        dica_principal = f"O {animal_morto} morreu afogado sem lesões corporais."
        dicas = [
            f"Se {animal_morto} morreu afogado, então o {animal_morto} tomou água do bebedouro do {assassino} ou o {animal_5} é o assassino.",
            f"Se o {animal_morto} foi morto com um golpe na cabeça, então o {animal_1} é o assassino e {animal_2} se encontrou com o {animal_morto} antes de dormir.",
            f"Se o {animal_4} estava na cabana central antes de o corpo ser descoberto e estava com ferimentos recentes, então o {animal_5} não é o assassino.",
            f"O {animal_4} estava na cabana central e estava com ferimentos recentes se e somente se o {animal_morto} tomou água do bebedouro do {assassino}.",
            f"O {animal_5} é o assassino se e somente se o {animal_morto} foi morto com graves lesões corporais.",
            f"O {animal_2} matou o {animal_morto} empurrando-o de um lugar alto.",
            f"Se {animal_5} tem comportamento agressivo e já machucou o {animal_3}, o {animal_3} estava dormindo no consultório veterinário.",
            f"Se o {animal_3} estava ausente na manhã da descoberta, então ele é o responsável pela morte do {animal_morto}.",
            f"Se o {animal_4} estava com ferimentos recentes, então ele brigou por comida com o {animal_1} ou o {animal_morto} não tomou água do bebedouro e o {animal_2} estava nos banheiros.",
            f"Se o {animal_4} brigou por comida com o {animal_1}, então o {assassino} matou o {animal_morto}."
        ]
    elif cenario == 2:
        dica_principal = f"O {animal_morto} morreu após uma disputa, apresentando marcas de mordida."
        dicas = [
            f"Se o {animal_morto} tem marcas de mordidas, então ele foi atacado pelo {assassino} ou o {animal_1} estava na praça de alimentação durante a noite e atacou o {animal_morto}.",
            f"Se o {animal_morto} morreu por mordidas profundas, então o {animal_4} estava no perímetro externo e o {animal_1} estava isolado no viveiro.",
            f"Se o {animal_5} foi encontrado com ferimentos na pata traseira, então ele não é o assassino e estava em recuperação.",
            f"O {animal_4} estava no perímetro externo se e somente se o {animal_morto} foi atacado pelo {assassino}.",
            f"O {animal_1} é o assassino se e somente se o {animal_morto} foi atacado no Banheiro.",
            f"O {animal_3} atacou o {animal_morto} após uma briga territorial.",
            f"Se o {animal_5} já teve comportamentos agressivos e feriu o {animal_3} anteriormente, então o {animal_3} estava descansando próximo ao riacho.",
            f"Se o {animal_2} estava ausente durante a madrugada, então ele é o responsável pela morte do {animal_morto}.",
            f"Se o {animal_4} tinha lama nas patas, então ele brigou por território com o {animal_5} ou o {animal_morto} não foi atacado pelo {assassino} e o {animal_1} estava no bebedouro.",
            f"Se o {animal_4} brigou por território com o {animal_5}, então o {assassino} matou o {animal_morto}.",
            f"O {animal_1} estava no bebedouro."
        ]
    else:
        dica_principal = f"O {animal_morto} morreu por envenenamento sem sinais de luta corporal."
        dicas = [
            f"Se o {animal_morto} morreu envenenado, então {animal_1} odiava o {animal_morto} ou o {animal_morto} comeu a comida do {assassino}.",
            f"Se o {animal_morto} foi ferido antes de morrer, então o {animal_3} esteve na área de alimentação antes da vítima.",
            f"Se o {animal_3} estava próximo à cabana central com ferimentos recentes, então ele pode ter feito algo errado na noite anterior.",
            f"O {animal_3} estava próximo à cabana central com ferimentos recentes se e somente se o {animal_morto} comeu a comida do {assassino}.",
            f"O {animal_2} é o assassino se e somente se o {animal_morto} foi atacado na área de alimentação.",
            f"O {animal_4} pode ter envenenado o {animal_morto} durante a madrugada.",
            f"Se o {animal_5} já tinha se comportado de forma estranha, então o {animal_5} pode ser o culpado.",
            f"Se o {animal_2} não estava na área da praça de alimentação, então ele não é o assassino.",
            f"Se o {animal_1} estava ausente durante a manhã, então ele é o responsável pela morte do {animal_morto}.",
            f"Se o {animal_2} estava próximo ao banheiro, então o {animal_4} não pode ser o assassino."
        ]

    return dica_principal, dicas

def main():
    k = 1000  # Valor constante que define a pontuação máxima possível
    
    while True:  # Loop para permitir jogar novamente
        console = Console()  # Inicializa o console Rich
        cenario = aleatorizar_cenario()  # Gera um cenário aleatório
        animal_morto, assassino, animal_1, animal_2, animal_3, animal_4, animal_5 = definir_animais()  # Define os animais do jogo
        animais = {  # Dicionário de animais com seus nomes
            "leão": {"nome": "Leão"},
            "elefante": {"nome": "Elefante"},
            "hipopótamo": {"nome": "Hipopótamo"},
            "tigre": {"nome": "Tigre"},
            "rinoceronte": {"nome": "Rinoceronte"},
            "macaco": {"nome": "Macaco"},
            "cervo": {"nome": "Cervo"},
        }
        pistas_encontradas = []  # Inicializa uma lista para armazenar pistas encontradas
        monster_found = False  # Inicializa a variável para controle do monstro
        jogo_vencido = False  # Variável para verificar se o jogador venceu

        dica_principal, dicas = definir_dicas(cenario, animal_morto, assassino, animal_1, animal_2, animal_3, animal_4, animal_5)  # Define as dicas
        mostrar_titulo(console)  # Exibe o título
        time.sleep(0.5)
        mostrar_mapa(console)  # Exibe o mapa do zoológico
        time.sleep(0.5)
        mostrar_texto_cenario(console, cenario, animal_morto, assassino)  # Exibe o cenário do jogo
        time.sleep(0.5)
        
        dia_atual = 1  # Inicializa o dia atual
        chance_de_sucesso = 0.9  # Chance inicial de sucesso para investigar
        pistas_encontradas.append(dica_principal)  # Adiciona a dica principal às pistas encontradas

        while not monster_found:  # Enquanto o monstro não for encontrado
            console.print(f"\nDia {dia_atual}", style="bold")  # Exibe o dia atual
            print(chance_de_sucesso)
            for pista in pistas_encontradas:
                time.sleep(0.5)
                print(f"- {pista}")
                
            if dia_atual == 10:
                acao = input("Hoje é o dia 10! Você só pode escolher a opção:\n1. Confrontar o monstro\n").strip()
            else:
                console.print("Escolha uma ação:", style="bold")
                time.sleep(0.5)
                acao = input("1. Investigar\n2. Confrontar o monstro\n3. Passar o dia\n").strip()

            if acao == '1' and dia_atual != 10:
                time.sleep(0.5)
                print("Investigando mais pistas...")
                
                if random.random() < chance_de_sucesso:
                    dicas_disponiveis = [dica for dica in dicas if dica not in pistas_encontradas]
                    if dicas_disponiveis:
                        nova_dica = random.choice(dicas_disponiveis)
                        pistas_encontradas.append(nova_dica)
                        console.print(f"Você encontrou uma nova pista: {nova_dica}", style="bold green")
                    else:
                        console.print("Não há mais dicas para serem encontradas.", style="bold red")
                else:
                    monster_found = True
                    console.print("Sua investigação falhou! O monstro te encontrou.", style="bold red")
                
                # Não aumenta o dia ao investigar, apenas diminui a chance de sucesso
                chance_de_sucesso -= 0.17  

            elif acao == '2' or (acao == '1' and dia_atual == 10):
                time.sleep(0.5)
                resposta = input(
                    "Quem você acha que é o monstro? (leão, elefante, hipopótamo, tigre, rinoceronte, macaco, cervo): ").strip().lower()
                if resposta in animais:
                    time.sleep(0.5)
                    print(f"Você confrontou o {animais[resposta]['nome']}!")
                    if resposta == assassino:
                        console.print("Você encontrou o monstro! Parabéns, você resolveu o mistério!", style="bold green")
                        jogo_vencido = True  # Marca o jogo como vencido
                        monster_found = True
                        
                        # Calcula a pontuação com base nos dias usados
                        pontuacao = k * (1 / dia_atual)
                        console.print(f"Sua pontuação final é: {pontuacao:.2f}", style="bold yellow")
                    else:
                        console.print("Você estava errado! O monstro escapuliu.", style="bold red")
                        break
                else:
                    console.print("Essa não é uma opção válida.", style="bold red")

            elif acao == '3' and dia_atual != 10:
                dia_atual += 1
                chance_de_sucesso -= 0.05  # Reduz a chance de sucesso no início de um novo dia
                print("Você passou o dia...")
                dicas_disponiveis = [dica for dica in dicas if dica not in pistas_encontradas]
                if dicas_disponiveis:
                    nova_dica = random.choice(dicas_disponiveis)
                    pistas_encontradas.append(nova_dica)
                    console.print(f"Você recebeu uma nova dica: {nova_dica}", style="bold green")
                else:
                    console.print("Não há mais dicas para serem dadas.", style="bold red")
            else:
                console.print("Ação inválida. Tente novamente.", style="bold red")

        # Verifica o motivo do final do jogo
        if not jogo_vencido: 
            console.print("Você foi encontrado pelo monstro! Fim de jogo.", style="bold red")  # Mensagem de fim de jogo por derrota

        # Pergunta se o jogador deseja jogar novamente
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            break

if __name__ == "__main__":
    main()
