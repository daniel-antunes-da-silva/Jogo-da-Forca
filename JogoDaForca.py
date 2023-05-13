from random import randint, choice


def desenho(qtd_erros):
    boneco = [' O', '\\O', '\\O \n | ',
              '\\O/ \n | ',
              '\\O/ \n |\n/',
              '\\O/ \n |\n/ \\',
              ' _O_ \n/ | \ \n / \\']
    while True:
        print()
        print('*' * 20)
        colorir('amarelo_negrito')
        print(f'{boneco[qtd_erros]}')
        colorir('limpa')
        print('*' * 20)
        print()
        qtd_erros += 1
        break


def mensagem_com_linhas(msg):
    print('-' * 40)
    print(msg)
    print('-' * 40)


def colorir(cor):
    cores = {'limpa': '\033[m',
             'verde_negrito': '\033[1;32m',
             'vermelho_negrito': '\033[1;31m',
             'branco_negrito': '\033[1;97m',
             'azul_negrito': '\033[1;34m',
             'amarelo_negrito': '\033[1;33m'}
    print(cores[cor])


palavras = {'frutas': ['banana', 'uva', 'abacaxi', 'morango', 'abacate', 'amora',
                       'framboesa', 'pêra', 'maçã', 'laranja', 'jaca', 'goiaba', 'acerola',
                       'limão', 'tangerina', 'maracujá', 'ameixa', 'mamão', 'coco', 'figo']}

#No dicionário palavras, estou pegando os values de 'frutas', e randomizando um valor dessa lista (value).
#escolhida = palavras['frutas'][randint(0, len(palavras['frutas']) - 1)]
escolhida = choice(palavras['frutas'])
print()
print(f'A fruta escolhida tem {len(escolhida)} letras: ', end='')
print('_' * len(escolhida))

# Fazendo a lista com underlines, de acordo com a palavra escolhida.
escondida = []
for c in range(0, len(escolhida)):
    escondida.append('_')
# print(escondida)

# Variável para controle de quantas vezes o usuário vai errar.
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
        if letra != '_':
            print(f'\033[0;34m{letra}\33[m', end='')
        else:
            print(letra, end='')
    print()
    if erros < 7:
        if '_' not in escondida:
            mensagem_com_linhas('Jogo finalizado!')
            colorir('verde_negrito')
            print('Você venceu! ')
            break
    else:
        mensagem_com_linhas('Jogo finalizado!')
        colorir('vermelho_negrito')
        print(f'Você perdeu! A palavra era {escolhida}')
        break
