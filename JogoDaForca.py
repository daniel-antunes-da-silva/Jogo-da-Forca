from random import randint


def desenho(qtd_erros):
    boneco = [' O', '\\O', '\\O \n | ',
              '\\O/ \n | ',
              '\\O/ \n |\n/',
              '\\O/ \n |\n/ \\',
              ' _O_ \n/ | \ \n / \\']

    while True:
        print()
        print('*'*20)
        print(cores['amarelo_negrito'], end='')
        print(f'{boneco[qtd_erros]}')
        print(cores['limpa'], end='')
        print('*'*20)
        print()
        qtd_erros += 1
        break


def mensagem_com_linhas(msg):
    print('-'*40)
    print(msg)
    print('-'*40)


cores = {'limpa': '\033[m',
             'verde_negrito': '\033[1;32m',
             'vermelho_negrito': '\033[1;31m',
             'branco_negrito': '\033[1;97m',
             'azul_negrito': '\033[1;34m',
             'amarelo_negrito': '\033[1;33m'}


palavras = ['banana', 'uva', 'abacaxi', 'morango', 'abacate', 'amora',
            'framboesa', 'pêra', 'maçã', 'laranja', 'jaca', 'goiaba', 'acerola',
            'limão', 'tangerina', 'maracujá', 'ameixa', 'mamão', 'coco', 'figo']
escolhida = palavras[randint(0, len(palavras) - 1)]
print()
print(f'A fruta escolhida tem {len(escolhida)} letras: ', end='')
print('_'*len(escolhida))

#Fazendo a lista com underlines, de acordo com a palavra escolhida.
escondida = []
for c in range(0, len(escolhida)):
    escondida.append('_')
#print(escondida)

#Variável para controle de quantas vezes o usuário vai errar.
erros = 0
while True:
    print()
    tentativa = str(input('Adivinhe uma letra: '))
    for pos, letra in enumerate(escolhida):
        if tentativa == escolhida[pos]:
            escondida[pos] = letra
    if tentativa not in escolhida:
        desenho(erros)
        erros += 1
    for letra in escondida:
        print(letra, end='')
    print()
    if erros < 7:
        if '_' not in escondida:
            mensagem_com_linhas('Jogo finalizado!')
            print('\nVocê venceu! ')
            break
    else:
        mensagem_com_linhas('Jogo finalizado!')
        print(f'\nVocê perdeu! A palavra era {escolhida}')
        break

