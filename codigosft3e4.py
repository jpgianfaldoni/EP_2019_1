# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:43:10 2019

@author: André Luis Silva Lop
"""
import random


jogadores=[]
print('Bem vindo')
jog=input('Insira o nome do jogador')
jogadores.append(jog)
while jog!='sair':
    jog=input('Insira o nome do outro jogador')
    jogadores.append(jog)
i=0
while i<len(jogadores):
    ###### sistema para armazenar nome de jogadores 
    






#criando algumas "salas"/cenarios


cenario={'sala do terror':'Você acaba de entrar na sala do terror', 
         'caverna assombrada':'Morra na escuridão da caverna', 
         'campo de batalha': 'Prepare-se para o combate'}
#criando dado

dado=random.randint(1,20)


hit_marker=0
bonus_de_batalha=0

#itens

mapa_da_DP=5
caneta_do_Raul=0
pendrive_da_punicao=8
livro_da_salvacao=5

#inventario

inventario=[]
game_over=False
while not game_over:
    cenario_atual=cenario[nome_cenario_atual]
    if cenario_atual['titulo']=='Saguão do perigo': #acontecimentos do saguao do perigo
        if dado<=7:
            hit_marker+=-mapa_da_DP    #### hitmarker permanenente 
            inventario.append('Mapa da DP')
            print('Você encontrou o Mapa da DP')        ###### condições de dado
            print('-5 de vida a cada rodada')
        elif dado>=12:
            inventario.append('Chave da sala do Raul')
            print('Você encontrou a chave da sala do Raul')
            print('Use a com sabedoria')
    elif cenario_atual['titulo']=='Andar do professor': #acontecimentos andar do professor
        if 'Chave da sala do Raul' not in inventario:
            print('Você não consegue entrar na sala do Raul')
        else:
            if dado>=15:
                hit_marker=caneta_do_Raul  #### hitmarker permannete 
                inventario.append('Caneta do Raul')
                inventario.append('Mapa para o Livro da Salvação')      ########## condições de dado
                bonus_de_batalha=12
                print('Você foi abençoado com a caneta do Raul e encontrou o Mapa secreto para o Livro da Salvação')
                print('Hit Marker foi ZERADO')
            elif dado<=10:
                hit_marker+=-pendrive_da_punicao  ###hitmarker permannete 
                inventario.append('Pendrive da Punição')
                print('Você irritou o MESTRE DO PYTHON')
                print('Por isso foi amaldiçoado com -8 pontos de vida a cada rodada')
    elif cenario_atual['titulo']=='Biblioteca': #acontecimentos biblioteca
        if 'Livro da Salvação' in inventario:
            hit_marker+=livro_da_salvacao    ##hitmarker fica permanente
            inventario.append('Livro da Salvação')
            print('Buscando um milagre.... e com o mapa em mãos Você encontrou o Livro da Salvação')
            print('Com todo o conhecimento vindo do livro, você será premiado com +5 pontos de vida a cada rodada')
        elif dado>=7:
            print('Você encontrou um colega também desesperado')
            print('Ele demonstra interesse em te ajudar')
            resposta=input('Aceita a ajuda do colega?')         ######## condições de dados 
            if resposta=='sim':
                inventario.append('Arquivo secreto do Python')
                bonus_de_batalha=5
            else:
                print('Deveria ter aceitado...')
    elif cenario_atual['titulo']=='Sala de teleporte': #acontecimentos sala de teletransporte
        print('Você cehgou na sala de teleporte e pode se teletransportar para qualquer uma das salas. Desde que lembre de cor o nome dela.')
        deseja=input('Deseja se teletransportar?')
        if deseja=='sim':
            nome=input('Qual sala deseja ir?')
            if nome=='Saguão do perigo':
                cenario_atual=cenario['Saguão do perigo']    ###### condições de teletransporte 
            elif nome=='Andar do professor':
                cenario_atual=cenario['Andar do professor']
            elif nome=='Biblioteca':
                cenario_atual=cenario['Biblioteca']
            else:
                print('Digitou o nome errado... Perdeu sua chance')
                
                
                
    dado=random.randint(1,20)
    visualizar=input('Você quer visualizar seu inventário?')
    if visualizar=='sim':
        print(inventario)
    
    transporte=input('Como quer ir para o próximo local?')
    print( ''' 1-Andando
               2-Baita infra car
               3-Patinete elétrico
               4-Ferrari 
                              ''')
    if transporte=='Andando':
        print('Você parou para tomar um café')
        hit_marker+=2  #hit marker instantaneo 
        print('Com a bebida revitalizante, você ganhou +2 pontos de vida')
        
    elif transporte=='Baita infra car':
        print('Você voltou no tempo para o vestibular do Insper')
        print('Decisão errada')
        jogo=game_over
        
    
            
        
        
    
print('Você perdeu o jogo, jogador {0}!'.format(jog))   
    