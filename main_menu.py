from src.grupos.sem_flores.briofitas import BriofitaAmazonia
from src.grupos.sem_flores.pteridofitas import PteridofitaAmazonia
from src.grupos.com_flores.angiospermas.angiospermas_base import AngiospermaAmazonia
from src.grupos.com_flores.gimnospermas import GimnospermaAmazonia
from src.grupos.com_flores.angiospermas.dicotiledoneas import Dicotiledonea
from src.grupos.com_flores.angiospermas.monoticoledonia import Monocotiledonia

identificadas = []


def menu():
    while True:
        print('=== MENU ===')
        print('1. Identificar plantas')
        print('2. Ver plantas identificadas')
        print('3. Ver hierarquia das plantas identificadas')
        print('0. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            identificar_plantas(plantas, identificadas)
        elif opcao == '2':
            ver_plantas_identificadas(identificadas)
        elif opcao == '3':
            ver_hierarquia_das_plantas(identificadas)
        elif opcao == '0':
            print('\nSaindo...\n')
            break
        else:
            print('\nOpção inválida. Tente novamente.\n')

def registrar_planta(p, identificadas):
    p.identificar()
    if p not in identificadas:
        identificadas.append(p)


def identificar_plantas(plantas, identificadas):
    resposta2 = None
    resposta3 = None
    resposta4 = None

    resposta1 = input('A planta em questão possui flores ?(s/n)\n').lower() == 's'
    if resposta1:
        resposta2 = input('A planta possui frutos ?(s/n)\n').lower() == 's'
        # Se tem frutos, perguntamos das folhas
        if resposta2:
            resposta3 = input(
                'A planta possui:\n'
                '1. Folhas finas e compridas\n'
                '2. Folhas largas e espalhadas\n'
                'Escolha uma opção: '
            ).strip()

    else:
        resposta4 = input('A planta possui caule ?').lower() == 's'

    for p in plantas:
        if p.flores == resposta1:

            if resposta1:
                if hasattr(p, 'frutos') and p.frutos == resposta2:

                    if resposta2:
                        if hasattr(p, 'folhas'):
                            if resposta3 == '1' and 'finas' in p.folhas.lower():
                                registrar_planta(p, identificadas)
                            elif resposta3 == '2' and 'largas' in p.folhas.lower():
                                registrar_planta(p, identificadas)

                    else:
                        registrar_planta(p, identificadas)

            else:
                tem_caule = getattr(p, 'caule', False)
                if tem_caule == resposta4:
                    registrar_planta(p, identificadas)


def ver_plantas_identificadas(identificadas):
    if not identificadas:
        print('\nNenhuma planta identificada ainda.\n')
        return
    else:
        print('\nPlantas identificadas:')
        for i, p in enumerate(identificadas, start=1):
            print(f'{i}. {p.nome}')
        print()

def ver_hierarquia_das_plantas(identificadas):
    if not identificadas:
        print("\nNenhuma planta identificada ainda.\n")
        return
    else:
        print('Plantas identificadas:\n')
        for i, p in enumerate(identificadas, start=1):
            print(f'{i}. {p.nome}')
        print()
        x = int(input('Escolha uma das plantas identificadas:\n'))
        escolhida = identificadas[x-1]
        print( f'{escolhida.nome} < {escolhida.especie} < Reino {escolhida.reino} ')



p1 = BriofitaAmazonia('musgo amazônico de floresta úmida', 'Musgo')
p2 = PteridofitaAmazonia('samambaia amazônica', 'Samambaia', 'medio')
p3 = GimnospermaAmazonia('pinheiro-do-paraná-amazônico ', 'Podocarpus', 'grande')
p4 = Dicotiledonea('castanheira-do-pará', 'Bertholletia', 'grande')
p5 = Monocotiledonia ('bananeira amazônica', 'Musa', 'grande')

plantas = [p1, p2, p3, p4, p5]

menu()