# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:17:43 2019

@author: André Luis Silva Lop
"""

import random


#criando algumas "salas"/cenarios


#criando dado
def dado():
    dado=random.randint(1,20)
    return dado



#itens                                      ####sala de teleporte = aquario

mapa_da_DP=5
caneta_do_Raul=0
pendrive_da_punicao=2
livro_da_salvacao=5

#inventario

inventario=[]
game_over=False


###função itens

def itens_no_cenario(nome_do_cenario): 
    objetos={'saguao':{'Mapa da DP':'Tira 5 pontos de vida a cada rodada','Chave da sala do Raul':'Permite entrar na sala do Raul'},
           'sala do raul':{'Caneta do Raul':'Zera qualquer dano de vida passivo','Pendrive da Punição':'Tira 2 pontos de vida a cada rodada','Mapa para o livro da salvação':'Mapa'},
           'biblioteca':{'Livro da salvação': 'Recebe 5 pontos de vida a cada rodada','Fone do Pelicano':'Te deixa imortal'},
           'fab lab':{'Estilete':'+2 de dano','Escudo de Papelão':'Toma -2 de dano'}}
    
    for k,v, in objetos.items():
        if nome_do_cenario==k:
            return v
        
        
#### função carregar cenarios
            
        
def carregar_cenarios(nome):
    cenarios = {'saguao':'cenario1','sala do raul':'cenario2',
                'biblioteca':'cenario3', 'fab lab':'cenario4',
                'sujinhuus':'cenario5','aquario':'cenario6'}
    for k,v in cenarios.items():
        if nome==k:
            carrega=v
            return carrega

def main():
    print('MUITO IMPORTANTE!')
    print()
    print('Por favor, meu consagrado...')
    print('Ao longo do jogo, digite TUDO em letra minúscula e sem acento')
    print()
    print('Aproveite a experiência e não se esqueça...')
    print('Se o EP já está difícil, imagina a PF')
    print()
    print()
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
        
    i=0
    game_over = False
    while not game_over:
        if i==0:
            inicio=carregar_cenarios('saguao')
            print('Saguão')
            tamanho=len('Saguao')
            print('-'*tamanho)
            print('Você está no saguão do Insper')
            print('Nessa sala temos esses itens:')
            print(itens_no_cenario('saguão'))
            numero_dado=dado()
            print('O número sorteado no dado foi',numero_dado)
            if numero_dado<=7:
                inventario.append('Mapa da DP')
                print('Você encontrou o Mapa da DP')       
                print('-5 de vida a cada rodada')
            elif numero_dado>=15:
                inventario.append('Chave da sala do Raul')
                print('Você encontrou a chave da sala do Raul')
                print('Use a com sabedoria')
            print('''Você tem essas opções de lugares para ir: 1- Sujinhuus 2- Fab Lab''')
            opcoes=input('Qual desses lugares você quer ir? ')
            if opcoes=='sujinhuus':
                inicio=carregar_cenarios('sujinhuus')
            elif opcoes=='fab lab':
                inicio=carregar_cenarios('fab lab')
            else:
                game_over=True
                print('Digitou errado! WASTED!')
        else:
            jogador.combate()
            if jogador.vida==0:
                game_over=True
            else:
                if inicio=='cenario1':
                    inicio=carregar_cenarios('saguao')
                    print('Saguão')
                    tamanho=len('Saguao')
                    print('-'*tamanho)
                    print('Você está no saguão do Insper')
                    print('Nessa sala temos esses itens:')
                    print(itens_no_cenario('saguão'))
                    numero_dado=dado()
                    print('O número sorteado no dado foi',numero_dado)
                    if numero_dado<=7:
                        inventario.append('Mapa da DP')
                        print('Você encontrou o Mapa da DP')       
                        print('-5 de vida a cada rodada')
                    elif numero_dado>=12:
                        inventario.append('Chave da sala do Raul')
                        print('Você encontrou a chave da sala do Raul')
                        print('Use a com sabedoria')
                    print('''Você tem essas opções de lugares para ir: 1- Sujinhuus 2- Fab Lab''')
                    opcoes=input('Qual desses lugares você quer ir? ')
                    if opcoes=='sujinhuus':
                        inicio=carregar_cenarios('sujinhuus')
                    elif opcoes=='fab lab':
                        inicio=carregar_cenarios('fab lab')
                    else:
                        game_over=True
                        print('Digitou errado! WASTED!')
                elif inicio=='cenario2':
                    print('Sala do Raul')
                    tamanho=len('sala do raul')
                    print('-'*tamanho)
                    print('Você está na porta da Sala do Raul')
                    if 'Chave da sala do Raul' not in inventario:
                        print('Você não consegue entrar na sala do Raul, ainda falta um item para ser encontrado')
                    else:
                        print('Nessa sala temos esses itens:')
                        print(itens_no_cenario('sala do raul'))
                        numero_dado=dado()
                        print('O número sorteado no dado foi',numero_dado)
                        if numero_dado>=15:
                            inventario.append('Caneta do Raul')
                            print('Você foi abençoado com a caneta do Raul')
                            print('Hit Marker foi ZERADO')
                        elif numero_dado<=10:
                            inventario.append('Pendrive da Punição')
                            print('Você irritou o MESTRE DO PYTHON')
                            print('Por isso foi amaldiçoado com -2 pontos de vida a cada rodada')
                    print('''Você tem essas opções de lugares para ir: 1- Fab Lab 2- Biblioteca''')
                    opcoes=input('Qual desses lugares você quer ir? ')
                    if opcoes=='biblioteca':
                        inicio=carregar_cenarios('biblioteca')
                    elif opcoes=='fab lab':
                        inicio=carregar_cenarios('fab lab')
                    else:
                        game_over=True
                        print('Digitou errado! WASTED!')
                elif inicio=='cenario3':
                    print('Biblioteca')
                    tamanho=len('biblioteca')
                    print('-'*tamanho)
                    print('Você está na biblioteca do Insper')
                    print('Nessa sala temos esses itens:')
                    print(itens_no_cenario('biblioteca'))
                    numero_dado=dado()
                    print('O número sorteado no dado foi',numero_dado)
                    if 'Mapa para o livro da Salvação' in inventario:
                        inventario.append('Livro da Salvação')
                        print('Buscando um milagre.... e com o mapa em mãos Você encontrou o Livro da Salvação')
                        print('Com todo o conhecimento vindo do livro, você será premiado com +5 pontos de vida a cada rodada')
                    elif numero_dado>=16:
                        print('Não é possível...')
                        print('Você encontrou o Fone do Pelicano')
                        print('Agora você está mais forte do que o GOKU!')
                        print('Você está IRMOTAL')
                        inventario.append('Fone do Pelicano')
                    print('''Você tem essas opções de lugares para ir: 1- Fab Lab 2- Sala do Raul 3- Aquário''')
                    opcoes=input('Qual desses lugares você quer ir? ')
                    if opcoes=='sala do raul':
                        inicio=carregar_cenarios('sala do raul')
                    elif opcoes=='fab lab':
                        inicio=carregar_cenarios('fab lab')
                    elif opcoes=='aquario':
                        inicio=carregar_cenarios('aquario')
                    else:
                        game_over=True
                        print('Digitou errado! WASTED!')
                        
                
        
            
            
            
            
            
        
        
        
        
        
        
        
        
        