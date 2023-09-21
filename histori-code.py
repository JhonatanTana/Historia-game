import time

pause = 1.5

print('G- Oh! Finalmente, você despertou está machucado e essas vestimentas, Ough! fedem, e muito!')
time.sleep(pause)
nome = input('G- Diga-me qual és teu nome?\n')
time.sleep(pause)
print('G- E, o que tu és?')

opcoes_validas = ['Paladino', 'Feiticeiro', 'Arqueiro']

while True:
    classes = input('Escolha uma classe (Paladino, Feiticeiro, Arqueiro): \n')

    classes = classes.capitalize()

    if classes in opcoes_validas:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Paladino, Feiticeiro ou Arqueiro.')
        continue

print('G- Ah, mas é claro, com essas vestimentas era óbvio!')
time.sleep(pause)
print(f'G- o que fazes aqui {nome} ?')
time.sleep(pause)
print('N- eu... eu não me lembro.')
time.sleep(pause)
print('G- o senhor não se lembra de nada?')
time.sleep(pause)
print('N- não...')
time.sleep(pause)
print('G- Bom, por enquanto, vamos lavar essas roupas e limpar seus ferimentos, você esta na pior.')
time.sleep(pause)
print('N- Quem é você, e por quê esta me ajudando?')
time.sleep(pause)
print('G- sou apenas uma garota do campo, o ajudei pois senti que era a coisa certa a se fazer.')
time.sleep(pause)
print('N- O-Obrigado.')

opcoes_armas = ['Cajado', 'Espada', 'Arco']

while True:
    classes = input('Escolha uma arma (Cajado, Espada, Arco): \n')

    armas = classes.capitalize()

    if armas in opcoes_armas:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Cajado, Espada ou Arco.')
        continue

opcoes_acessorios = ['Amuleto', 'Armadura', 'Aljava']

while True:
    classes = input('Escolha um acessório (Amuleto, Armadura, Aljava): \n')

    acessorios = classes.capitalize()

    if acessorios in opcoes_acessorios:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Paladino, Feiticeiro ou Arqueiro.')
        continue
time.sleep(pause)
print(f'Narrador- A mulher estrangeira lava suas vestimentas enquanto você se limpava, quando saiu de seu banho achou suas vestimentas limpas, porem no estado que estavam, eram apenas trapos, e somente por pouco lembrava sua forma antiga.Mas voce não se lembra do que aconteceu, com apenas seu/a {armas} e {acessorios} voce decide agradecer a mulher estrangeira e partir para tentar descobrir o que aconteceu, mas antes voce à pede para lhe mostrar onde o achou.')
time.sleep(pause)
print('G- Bom, só posso lhe trazer até aqui, boa sorte guerreiro, que a luz de !THALMOR! brilhe sobre ti.')
time.sleep(pause)
print(f'Narrador- E assim comça sua jornada, com apenas seu/sua {opcoes_armas} em mãos e trapos em seu corpo você decide investigar.')

print('Narrador- você esta na entrada de uma floresta cercada por arvores frutiferas, suas frutas sao de cores variadas, e exalam o melhor perfume que seu nariz ja sentiu.')
time.sleep(pause)
opcao_fome = input("Narrador: você esta com fome, deseja comer?").upper()
while True:
    if opcao_fome == "NAO":
        time.sleep(pause)
        print("Narrador: Você decide seguir em frente.")
        break
    elif opcao_fome == "SIM":
        time.sleep(pause)
        print("Narrador- você pega uma fruta estranha, aparencia de maçã porem coloração de madeira, você a morde, seu suco e sabor o revigoram.")

        opcao_xp = input("Subir de Nível ?").upper()

        if opcao_xp == "NAO":
            time.sleep(pause)
            print("Narrador: Você armazenou o XP.")
            break
        elif opcao_xp == "SIM":
            time.sleep(pause)
            print("Narrador: Voce subiu de nível")
            break
        else:
            time.sleep(pause)
            print("Narrador: Opção inválida. Por favor, escolha entre 'S' para sim ou 'N' para não.")
            continue
    else:
        time.sleep(pause)
        print("Narrador: Opção inválida. Por favor, escolha entre 'S' para sim ou 'N' para não.")
        continue
time.sleep(pause)
print('Narrador- você olha mais um pouco ao seu redor e vê marcas de batalha nas árvores o que parecem ser garras, dileceraram pela madeira em volta, você investiga.')
time.sleep(pause)
print(f'Narrador- enquanto você olha as árvores, ouve pegadas se aproximando, é algo grande! Você saca sua/seu {opcoes_armas} e logo em seguida ouve um grunido que faz seu peito resonar com medo. e um enorme urso ensanguentado pula de fora da floresta, em sua pelagem densa à marcas de espadas apenas olhar para tal criatura o enche de medo.')
