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

#itens                                      ####sala de teleporte = aquario

mapa_da_DP=5
caneta_do_Raul=0
pendrive_da_punicao=2
livro_da_salvacao=5

#inventario

inventario=[]
game_over=False


###função itens

def itens_no_cenario(nome_do_cenario): #chamada tem que ser uma chave de um dicionario cenario_atual['titulo']
    objetos={'Saguão':{'Mapa da DP':'Tira 5 pontos de vida a cada rodada','Chave da sala do Raul':'Permite entrar na sala do Raul'},
           'Sala do Raul':{'Caneta do Raul':'Zera qualquer dano de vida passivo','Pendrive da Punição':'Tira 2 pontos de vida a cada rodada','Mapa para o livro da salvação':'Mapa'},
           'Biblioteca':{'Livro da salvação': 'Recebe 5 pontos de vida a cada rodada','Fone do Pelicano':'Te deixa imortal'},
           'Fab Lab':{'Estilete':'+2 de dano','Escudo de Papelão':'Toma -2 de dano'}}
    
    for k,v, in objetos.items():
        if nome_do_cenario==k:
            return v
        else:
            return 'Nenhum objeto'
        
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
        ecolha=input('Quer entrar nessa aventura?')
        if escolha=='sim':                                  #########lembrar de colocar else
                inicio=carregar_cenarios('saguao')
                while inicio=='cenario1':
                    print('Nessa sala temos esses itens:')
                    print(itens_no_cenario('Saguão do Perigo'))
                    numero_dado=dado()
                    print('O número sorteado no dado foi',numero_dado)
                    if numero_dado<=7:
                        inventario.append('Mapa da DP')
                        print('Você encontrou o Mapa da DP')        ###### condições de dado
                        print('-5 de vida a cada rodada')
                    elif numero_dado>=12:
                        inventario.append('Chave da sala do Raul')
                        print('Você encontrou a chave da sala do Raul')
                        print('Use a com sabedoria')
                        
                    inicio=''
                print('''Você tem essas opções de lugares para ir: 1- Sujinhuus
                                                                 2- Fab Lab''')
                opcoes=input('Qual desses lugares você quer ir?')
                if opcoes=='sujinhuus':
                    jogador.combate()
                    if jogador.vida==0:
                        game_over=True
                    else:
                        inicio=carregar_cenarios('sujinhuus')
                        if inicio == 'Cenario5':
                            alcool = 0
                            print('Bem vindo ao Sujinhuus! Vamos te apresentar as nossas opções de bebida:')
                            print('litrão nosso de todo dia')
                            print('corote do amor')
                            print('caipirinha do role')
                            escolha = input('Vai querer tomar alguma coisa ou ir embora? Se quiser algo, digite o nome da bebida. ')
                            while escolha != 'ir embora':
                                if escolha == 'litrão nosso de todo dia':
                                    alcool += 1
                                    escolha = input('Vai querer tomar mais alguma coisa ou ir embora? Se quiser algo, digite o nome da bebida. ')
                                elif escolha == 'corote do amor':
                                    alcool += 1
                                    escolha = input('Vai querer tomar mais alguma coisa ou ir embora? Se quiser algo, digite o nome da bebida. ')
                                elif escolha == 'caipirinha do role':
                                    alcool +=1
                                    escolha = input('Vai querer tomar mais alguma coisa ou ir embora? Se quiser algo, digite o nome da bebida. ')
                                else:
                                    print('Não temos isso, perdeu a chance de pedir! Vai ter que ir embora.')
                                    escolha == 'ir embora'
                            if alcool > 0:
                               print('Você não pode voltar ao Insper tendo bebido!')
                               game_over = True
                            
                            ##### opcoes='nao'
                    
                elif opcoes=='fab lab':
                    jogador.combate()
                    if jogador.vida==0:
                        game_over=True
                    else:
                        inicio=carregar_cenarios('fab lab')
                        
                        while inicio=='cenario4':
                            print('Nessa sala temos esses itens:')
                            print(itens_no_cenario('Fab Lab'))
                            numero_dado=dado()
                            print('O número sorteado no dado foi',numero_dado)
                            if numero_dado>=7:
                                inventario.append('Estilete')
                                inventario.append('Papelão')
                                print('Você ganhou o estilete')
                                print('Dano recebe +2 pontos')
                                print('Você ganhou um escudo de papelão')
                                print('Recebe -2 pontos de dano')
                            inicio=''
                                
                
                        print('''Você tem essas opções de lugares para ir: 1- Sala do Raul
                                                                       2- Biblioteca''')
                        opcoes=input('Qual desses lugares você quer ir?') 
                        if opcoes=='sala do raul':
                            inicio=carregar_cenarios('sala do raul')
                            if 'Chave da sala do Raul' not in inventario:
                                print('Você não consegue entrar na sala do Raul')
                                inicio=carregar_cenarios('fab lab')
                            else:
                                print('Nessa sala temos esses itens:')
                                print(itens_no_cenario('Sala do Raul'))
                                numero_dado=dado()
                                print('O número sorteado no dado foi',numero_dado)
                                if numero_dado>=15:
                                    hit_marker=caneta_do_Raul  #### hitmarker permannete 
                                    inventario.append('Caneta do Raul')
                                    inventario.append('Mapa para o Livro da Salvação')      ########## condições de dado
                                    print('Você foi abençoado com a caneta do Raul e encontrou o Mapa secreto para o Livro da Salvação')
                                    print('Hit Marker foi ZERADO')
                                elif numero_dado<=10:
                                    hit_marker+=-pendrive_da_punicao  ###hitmarker permannete 
                                    inventario.append('Pendrive da Punição')
                                    print('Você irritou o MESTRE DO PYTHON')
                                    print('Por isso foi amaldiçoado com -2 pontos de vida a cada rodada')
                            
                     
                      
                        
                        
                        
                        ####codigo deseja sair dessa sala//////transporte
                        
                        
                        
                        
                        
                        
                        
            elif cenario_atual=='andar professor': #acontecimentos andar do professor
                if 'Chave da sala do Raul' not in inventario:
                    print('Você não consegue entrar na sala do Raul')
                else:
                    print('Nessa sala temos esses itens:')
                    print(itens_no_cenario('Sala do Raul'))
                    print('O número sorteado no dado foi',dado)
                    if dado()>=15:
                        hit_marker=caneta_do_Raul  #### hitmarker permannete 
                        inventario.append('Caneta do Raul')
                        inventario.append('Mapa para o Livro da Salvação')      ########## condições de dado
                        print('Você foi abençoado com a caneta do Raul e encontrou o Mapa secreto para o Livro da Salvação')
                        print('Hit Marker foi ZERADO')
                    elif dado()<=10:
                        hit_marker+=-pendrive_da_punicao  ###hitmarker permannete 
                        inventario.append('Pendrive da Punição')
                        print('Você irritou o MESTRE DO PYTHON')
                        print('Por isso foi amaldiçoado com -2 pontos de vida a cada rodada')
            elif cenario_atual=='biblioteca': #acontecimentos biblioteca
                print('Nessa sala temos esses itens:')
                print(itens_no_cenario('Biblioteca'))
                print('O número sorteado no dado foi',dado)
                if 'Mapa para o livro da Salvação' in inventario:
                    hit_marker+=livro_da_salvacao    ##hitmarker fica permanente
                    inventario.append('Livro da Salvação')
                    print('Buscando um milagre.... e com o mapa em mãos Você encontrou o Livro da Salvação')
                    print('Com todo o conhecimento vindo do livro, você será premiado com +5 pontos de vida a cada rodada')
                elif dado()>=7:
                    print('Você encontrou um colega também desesperado')
                    print('Ele demonstra interesse em te ajudar')
                    resposta=input('Aceita a ajuda do colega?')         ######## condições de dados 
                    if resposta=='sim':
                        inventario.append('Arquivo secreto do Python')
                    else:
                        print('Deveria ter aceitado...')
                elif dado()>=16:
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
           
                
                        
                        
                        
            visualizar=input('Você quer visualizar seu inventário?')
            if visualizar=='sim':
                print(inventario)
                
                
                
                
                
if __name__ == "__main__":
    main()            