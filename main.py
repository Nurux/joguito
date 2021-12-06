import time
import os
import random

class color():
    cyan = '\033[1;36m'
    yellow = '\033[1;33m'
    red = '\033[91m'
    green = '\033[92m'
    white = '\033[1;97m'

def escolha_menu(resp):
    if resp == 1:
        game()
    
    if resp == 2:
        tutorial()

    if resp == 3:
        creditos()
    
    if resp == 4:
        limpa_tela()
        print(color.yellow +'Obrigado por me usar ( ͡° ͜ʖ ͡°)')
        print(color.red + 'Finalizando programa...')
    
def volta_menu():
    back_resp = input(color.yellow + 'Deseja voltar ao menu (s/n)? ')
    limpa_tela()

    if back_resp.lower() == 's' or back_resp.lower() == 'sim':
        main()
    else:
        print(color.white + 'Neste caso o programa será finalizando °3°')
        time.sleep(2)
        print(color.red + 'Finalizando programa ...')

def tutorial():
    limpa_tela()
    print(color.cyan + 'O game consiste em tentar advinhar um numero de 1 a 100 gerado pelo robô')
    print('Toda vez que o jogador errar o robô enviará uma dica')
    print('O game acaba quando o jogador acertar o número escolhido pelo robo\n')

    volta_menu()

def creditos():
    limpa_tela()
    print(color.white + 'Joguito bem simples para ser jogado no terminal mesmo.\n\nGerando conhecimento de utilização de cores no terminal e usuabilidade de classes.\n\nFeito por: Nuruzinho')

    volta_menu()

def limpa_tela():
    os.system('cls')

def game_gerar_numero():
    limpa_tela()
    print(color.yellow + 'Gerando numero aleatório de 1 a 100.....')
    time.sleep(1)
    numero = random.randrange(101)
    return numero

def game_continuar():
    resp = input('Deseja continuar(s/n)?')
    
    if resp.upper() == 'S' or resp.upper() == 'SIM':
        return 1
    elif resp.upper() == 'N' or resp.upper() == 'NAO':
        return 0

def game_verificar_resposta(numero, numero_digitado, tentativas):

    if numero > numero_digitado:
        print(color.red + f'Você errou!\nTente um numero maior que {numero_digitado}')
        time.sleep(2)
        limpa_tela()

    if numero < numero_digitado:
        print(color.red + f'Você errou!\nTente um numero menor que {numero_digitado}')
        time.sleep(3)
        limpa_tela()
    
    if numero == numero_digitado:
        limpa_tela()
        print(color.cyan + '------------------------')
        print(color.green + '--------' + color.red + 'Parabéns'+ color.green +'--------')
        print(color.cyan + '------------------------')
        print(color.yellow + f'Você acertou com {tentativas} tentativas\n')
        time.sleep(2)
        resp = game_continuar()
        if resp == 0:
            return True
        else:
            return False       

def game():
    numero = game_gerar_numero()
    tentativas = 0
    print(color.green + 'Qual numero o nosso robo escolheu?')
    
    while True:
        try:
            tentativas += 1
            numero_digitado = int(input(color.cyan + 'Digite o numero que você acha ser o escolhido pelo robo: '))
            fim = game_verificar_resposta(numero, numero_digitado, tentativas)

            if fim == True:
                limpa_tela()
                print(color.white + 'Obrigado por jogar :)')
                print(color.red + 'Finalizando o programa...')
                break
            elif fim == False:
                continue
        except ValueError:  
            print(color.red + 'Por favor digite um número inteiro')
            continue 

def main():
    print(color.white + '-------------------------------')
    print(color.white + '-------DESCUBRA O NÚMERO-------')
    print(color.white + '-------------------------------')

    print(color.cyan + '1) Jogar')
    print(color.yellow + '2) Tutorial')
    print(color.green + '3) Créditos')
    print(color.red + '4) Sair')

    resp = int(input(color.white))

    escolha_menu(resp)

if __name__ == '__main__':
    main()