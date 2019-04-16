# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:43:10 2019

@author: André Luis Silva Lop
"""
import random


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
        if nome_do_cenario==k:
            return v
        else:
            return 'Nenhum objeto'
    
        
        

#####jogo


while not game_over:
    cenario_atual=cenario[nome_cenario_atual]
    if cenario_atual['titulo']=='Saguão do perigo':#acontecimentos do saguao do perigo
        print('Nessa sala temos esses itens:')
        print(itens_no_cenario('Saguão do Perigo'))
        print('O número sorteado no dado foi',dado)
        if dado<=7:
            hit_marker+=-mapa_da_DP    #### hitmarker permanenente 
            inventario.append('Mapa da DP')
            print('Você encontrou o Mapa da DP')        ###### condições de dado
            print('-5 de vida a cada rodada')
        elif dado>=12:
            inventario.append('Chave da sala do Raul')
            print('Você encontrou a chave da sala do Raul')
            print('Use a com sabedoria')
    elif cenario_atual['titulo']=='Andar do Professor': #acontecimentos andar do professor
        if 'Chave da sala do Raul' not in inventario:
            print('Você não consegue entrar na sala do Raul')
        else:
            print('Nessa sala temos esses itens:')
            print(itens_no_cenario('Andar do Professor'))
            print('O número sorteado no dado foi',dado)
            if dado>=15:
                hit_marker=caneta_do_Raul  #### hitmarker permannete 
                inventario.append('Caneta do Raul')
                inventario.append('Mapa para o Livro da Salvação')      ########## condições de dado
                bonus_de_batalha+=12
                print('Você foi abençoado com a caneta do Raul e encontrou o Mapa secreto para o Livro da Salvação')
                print('Hit Marker foi ZERADO')
            elif dado<=10:
                hit_marker+=-pendrive_da_punicao  ###hitmarker permannete 
                inventario.append('Pendrive da Punição')
                print('Você irritou o MESTRE DO PYTHON')
                print('Por isso foi amaldiçoado com -2 pontos de vida a cada rodada')
    elif cenario_atual['titulo']=='Biblioteca': #acontecimentos biblioteca
        print('Nessa sala temos esses itens:')
        print(itens_no_cenario('Biblioteca'))
        print('O número sorteado no dado foi',dado)
        if 'Mapa para o livro da Salvação' in inventario:
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
                bonus_de_batalha+=5
            else:
                print('Deveria ter aceitado...')
        elif dado>=16:
            print('Não é possível...')
            print('Você encontrou o Fone do Pelicano')
            print('Agora você está mais forte do que o GOKU!')
            print('Você está IRMOTAL')
            inventario.append('Fone do Pelicano')
    elif cenario_atual['titulo']=='Sala de teleporte': #acontecimentos sala de teletransporte
        print('Nessa sala temos esses itens:')
        print(itens_no_cenario('Sala de Teletransporte'))
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
    elif cenario_atual['título']=='Fab Lab':
        print('Nessa sala temos esses itens:')
        print(itens_no_cenario('Fab Lab'))
        print('O número sorteado no dado foi',dado)
        if dado>=7:
            inventario.append('Estilete')
            inventario.append('Papelão')
            bonus_de_batalha+=2
            print('Você ganhou o estilete')
            print('Dano recebe +2 pontos')
            print('Você ganhou um escudo de papelão')
            print('Recebe -2 pontos de dano')
        
        
                
                
                
    dado=random.randint(1,20)
    visualizar=input('Você quer visualizar seu inventário?')
    if visualizar=='sim':
        print(inventario)
    
    
    
    
   
        
      
            
        
        
    
