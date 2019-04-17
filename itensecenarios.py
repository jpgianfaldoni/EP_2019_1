# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:43:10 2019

@author: André Luis Silva Lop
"""
import random


#criando algumas "salas"/cenarios


#criando dado
def dado():
    dado=random.randint(1,20)
    return dado


hit_marker=0
bonus_de_batalha=0

#itens

mapa_da_DP=5
caneta_do_Raul=0
pendrive_da_punicao=2
livro_da_salvacao=5

#inventario

inventario=[]
game_over=False


###função itens

def itens_no_cenario(nome_do_cenario): #chamada tem que ser uma chave de um dicionario cenario_atual['titulo']
    objetos={'Saguão do Perigo':{'Mapa da DP':'Tira 5 pontos de vida a cada rodada','Chave da sala do Raul':'Permite entrar na sala do Raul'},
           'Andar do Professor':{'Caneta do Raul':'Zera qualquer dano de vida passivo','Pendrive da Punição':'Tira 2 pontos de vida a cada rodada','Mapa para o livro da salvação':'Mapa'},
           'Biblioteca':{'Livro da salvação': 'Recebe 5 pontos de vida a cada rodada','Fone do Pelicano':'Te deixa imortal'},
           'Fab Lab':{'Estilete':'+2 de dano','Escudo de Papelão':'Toma -2 de dano'}}
    for k,v, in objetos.items():
        if nome_do_cenario == k:
            print(v)
    if nome_do_cenario not in objetos.keys():
        print("Nenhum Objeto")
        
#### função carregar cenarios
            
        
def carregar_cenarios(nome):
    cenarios = {'saguao':'cenario1','sala do raul':'cenario2',
                'biblioteca':'cenario3', 'fab lab':'cenario4',
                'sujinhuus':'cenario5','aquario':'cenario61'}
    for k,v in cenarios.items():
        if nome==k:
            carrega=v
            return carrega

def main():
    dados = 0
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
        
    
    game_over = False
    while not game_over:
        inicio=carregar_cenarios('saguao')
        print('Saguão')
        tamanho=len('Saguao')
        print('-'*tamanho)
        print('Você está no saguão do insper')
        escolha=input('Quer entrar nessa aventura?')
        if escolha=='sim':                                  #########lembrar de colocar else
            inicio=carregar_cenarios('saguao')
            if inicio=='cenario1':
                print('Nessa sala temos esses itens:')
                print(itens_no_cenario('Saguão do Perigo'))
                rng = dado()
                print('O número sorteado no dado foi',dados)
                if dados<=7:
                    inventario.append('Mapa da DP')
                    print('Você encontrou o Mapa da DP')        ###### condições de dado
                    print('-5 de vida a cada rodada')
                elif dados>=12:
                    inventario.append('Chave da sala do Raul')
                    print('Você encontrou a chave da sala do Raul')
                    print('Use a com sabedoria')
        opcoes=input()        
                        
                        
                        
                        ####codigo deseja sair dessa sala//////transporte
                        
                        
                        
                        
                        
                        
                        
        if cenario_atual=='andar professor': #acontecimentos andar do professor
            if 'Chave da sala do Raul' not in inventario:
                print('Você não consegue entrar na sala do Raul')
            else:
                print('Nessa sala temos esses itens:')
                print(itens_no_cenario('Andar do Professor'))
                dados = dado()
                print('O número sorteado no dado foi',dados)
            if dados>=15:
                hit_marker=caneta_do_Raul  #### hitmarker permannete 
                inventario.append('Caneta do Raul')
                inventario.append('Mapa para o Livro da Salvação')      ########## condições de dado
                print('Você foi abençoado com a caneta do Raul e encontrou o Mapa secreto para o Livro da Salvação')
                print('Hit Marker foi ZERADO')
            elif dados<=10:
                hit_marker+=-pendrive_da_punicao  ###hitmarker permannete 
                inventario.append('Pendrive da Punição')
                print('Você irritou o MESTRE DO PYTHON')
                print('Por isso foi amaldiçoado com -2 pontos de vida a cada rodada')
            elif cenario_atual=='biblioteca': #acontecimentos biblioteca
                print('Nessa sala temos esses itens:')
                print(itens_no_cenario('Biblioteca'))
                dados = dado()
                print('O número sorteado no dado foi',dados)
                if 'Mapa para o livro da Salvação' in inventario:
                    hit_marker+=livro_da_salvacao    ##hitmarker fica permanente
                    inventario.append('Livro da Salvação')
                    print('Buscando um milagre.... e com o mapa em mãos Você encontrou o Livro da Salvação')
                    print('Com todo o conhecimento vindo do livro, você será premiado com +5 pontos de vida a cada rodada')
                elif dados>=7:
                    print('Você encontrou um colega também desesperado')
                    print('Ele demonstra interesse em te ajudar')
                    resposta=input('Aceita a ajuda do colega?')         ######## condições de dados 
                    if resposta=='sim':
                        inventario.append('Arquivo secreto do Python')
                    else:
                        print('Deveria ter aceitado...')
                elif dados>=16:
                    print('Não é possível...')
                    print('Você encontrou o Fone do Pelicano')
                    print('Agora você está mais forte do que o GOKU!')
                    print('Você está IRMOTAL')
                    inventario.append('Fone do Pelicano')
            elif cenario_atual=='sala de teleporte': #acontecimentos sala de teletransporte
                print('Nessa sala temos esses itens:')
                print(itens_no_cenario('Sala de Teletransporte'))
                print('Você cehgou na sala de teleporte e pode se teletransportar para qualquer uma das salas. Desde que lembre de cor o nome dela.')
                deseja=input('Deseja se teletransportar?')
                if deseja=='sim':
                    nome=input('Qual sala deseja ir?')
                    if nome=='Saguão do perigo':
                        cenario_atual="inicio"    ###### condições de teletransporte 
                    elif nome=='Andar do professor':
                        cenario_atual="andar professor"
                    elif nome=='Biblioteca':
                        cenario_atual="biblioteca"
                    else:
                        print('Digitou o nome errado... Perdeu sua chance')
            elif cenario_atual=='Fab Lab':
                print('Nessa sala temos esses itens:')
                print(itens_no_cenario('Fab Lab'))
                dados = dado()
                print('O número sorteado no dado foi',dados)
                if dados>=7:
                    inventario.append('Estilete')
                    inventario.append('Papelão')
                    print('Você ganhou o estilete')
                    print('Dano recebe +2 pontos')
                    print('Você ganhou um escudo de papelão')
                    print('Recebe -2 pontos de dano')
                
                
                        
                        
                        
            visualizar=input('Você quer visualizar seu inventário?')
            if visualizar=='sim':
                print(inventario)
                
                
                
                
                
if __name__ == "__main__":
    main()                                    