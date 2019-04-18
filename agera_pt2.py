#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:20:05 2019

@author: joaopedrochacon
"""

                elif inicio=='cenario4':
                    print('Fab Lab')
                    tamanho=len('Fab Lab')
                    print('-'*tamanho)
                    print('Você está no Fab Lab do Insper')
                    print('Nessa sala temos esses itens:')
                    print(itens_no_cenario('fab lab'))
                    numero_dado=dado()
                    print('O número sorteado no dado foi',numero_dado)
                    if numero_dado>=7:
                        inventario.append('Estilete')
                        inventario.append('Papelão')
                        print('Você ganhou o estilete')
                        print('Dano recebe +2 pontos')
                        print('Você ganhou um escudo de papelão')
                        print('Recebe -2 pontos de dano')
                    print('''Você tem essas opções de lugares para ir: 1- Biblioteca 2- Sala do Raul''')
                    opcoes=input('Qual desses lugares você quer ir? ')
                    if opcoes=='biblioteca':
                        inicio=carregar_cenarios('biblioteca')
                    elif opcoes=='sala do raul':
                        inicio=carregar_cenarios('sala do raul')
                    else:
                        game_over=True
                        print('Digitou errado! WASTED!')
                elif inicio=='cenario5':
                    alcool = 0
                    print('Bem vindo ao Sujinhuus! Vamos te apresentar as nossas opções de bebida:')
                    print('-litrão nosso de todo dia')
                    print('-corote do amor')
                    print('-caipirinha do role')
                    escolha = input('Vai querer tomar alguma coisa ou ir embora? Se quiser algo, digite o nome da bebida. ')
                    while escolha != 'ir embora':
                        if escolha == 'litrao nosso de todo dia':
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
                    else:
                        inicio=carregar_cenarios('saguao')
                elif inicio=='cenario6':
                    print('Aquário')
                    tamanho=len('Aquário')
                    print('-'*tamanho)
                    print('Por algum motivo desconhecido, você deu sorte de encontrar um aquário vazio na biblioteca')
                    print('Sem querer, você acabou caindo no sono e acordou em um lugar aleatório')
                    cenarios=['saguao','sala do raul','biblioteca','fab lab','sujinhuus']
                    n=random.randint(0,4)
                    inicio=carregar_cenarios(cenarios[n])
                    
         if  game_over==False:
            visualizar=input('Você quer visualizar seu inventário? ')
            if visualizar=='sim':
                print(inventario)
             
    if ganhou==True:
        print('PARABÉNS!Você derrotou o Raul e se salvou da DP!')
    else:
        print('Você perdeu :(')
        print('Nos vemos na DP!')
        
        
# Programa principal.
if __name__ == "__main__":
    main()            
            
                    
                    