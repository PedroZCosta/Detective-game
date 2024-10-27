import random


def mostrar_mapa():  # Mapa do Zoológico
    print("+" + "-" * 65 + "+")
    print("|       Entrada        | Praça de Alimentação   | Jaula do Cervo  |")
    print("|----------------------|------------------------|-----------------|")
    print("| Jaula do Macaco      |                        | Jaula do Leão   |")
    print("|----------------------|     Cabana Central     |-----------------|")
    print("| Jaula do Elefante    |                        | Jaula do Tigre  |")
    print("|----------------------|----------------------- |-----------------|")
    print("| Jaula do Rinoceronte |  Jaula do Hipopótamo   | Banheiros       |")
    print("+" + "-" * 65 + "+")


def aleatorizar_cenario():
    return random.randint(1, 3)  # Gera um número aleatório entre 1 e 3


def definir_animais():
    animais = ["leão", "elefante", "hipopótamo", "tigre", "rinoceronte", "macaco", "cervo"]
    random.shuffle(animais)

    # Definição de animais no contexto do cenário
    animal_morto = animais[0]
    assassino = animais[1]
    animal_1 = animais[2]
    animal_2 = animais[3]
    animal_3 = animais[4]
    animal_4 = animais[5]
    animal_5 = animais[6]

    return animal_morto, assassino, animal_1, animal_2, animal_3, animal_4, animal_5


# Função para exibir o texto do cenário
def mostrar_texto_cenario(cenario, animal_morto, assassino):
    if cenario == 1:
        print(
            f"Em uma manhã ensolarada no Zoológico da Cidade, a alegria dos visitantes se transformou em pânico quando"
            f" o {animal_morto} foi encontrado flutuando no Lago dos Hipopótamos. Os cuidadores isolaram a área, "
            f"levantando questões sobre como o {assassino} havia chegado até ali. Qual animal matou o {animal_morto}?")
    elif cenario == 2:
        print(f"Em uma noite de tempestade no Zoológico da Cidade, o {animal_morto} foi encontrado na área da Praça de "
              f"alimentação com algumas marcas de mordida. Os cuidadores ficaram intrigados, pois não era claro se o "
              f"{assassino} agiu sozinho ou em parceria. Quem matou o {animal_morto}?")
    else:
        print(
            f"Em uma noite chuvosa no Zoológico da Cidade, o silêncio da madrugada foi interrompido por gritos de pavor"
            f" dos vigilantes. Ao investigar, o {animal_morto} foi encontrado próximo ao banheiro, com sinais de ter"
            f" sido envenenado. Os cuidadores, perplexos, bloquearam o local para descobrir como o {assassino}"
            f" conseguiu colocar o veneno. Qual animal envenenou o {animal_morto}?")


def definir_dicas(cenario, animal_morto, assassino, animal_1, animal_2, animal_3, animal_4, animal_5):
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
        dica_principal = f"O {animal_morto} morreu após uma disputa, apresentando marcas de mordidas."
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
            f"O {animal_2} é o assassino se e somente se o {animal_morto} não foi visto durante a madrugada.",
            f"Se o {animal_4} foi visto durante a noite e estava ausente durante o dia, então ele é o responsável pela morte do {animal_morto}.",
            f"Se o {animal_5} já teve comportamentos estranhos e feriu o {animal_1} anteriormente, então o {animal_1} estava isolado em seu viveiro.",
            f"Se o {animal_1} estava ausente na manhã da descoberta, então ele é o responsável pela morte do {animal_morto}.",
            f"Se o {animal_2} estava doente e não compareceu ao bebedouro, então ele pode ter sido o responsável pela morte do {animal_morto}.",
            f"Se o {animal_3} já foi tratado no consultório veterinário, então ele não é o assassino."
        ]

    return dica_principal, dicas


def main():
    mostrar_mapa()
    cenario = aleatorizar_cenario()
    animal_morto, assassino, animal_1, animal_2, animal_3, animal_4, animal_5 = definir_animais()
    mostrar_texto_cenario(cenario, animal_morto, assassino)
    dica_principal, dicas = definir_dicas(cenario, animal_morto, assassino, animal_1, animal_2, animal_3, animal_4,
                                          animal_5)

    print(dica_principal)
    random.shuffle(dicas)  # Embaralha as dicas
    for i, dica in enumerate(dicas, 1):
        print(f"Dica {i}: {dica}")


if __name__ == "__main__":
    main()
