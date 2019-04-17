#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:44:27 2019

@author: joaopedrochacon
"""

#descricao do sujinhuus

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
    else:
        inicio = carregar_cenarios('Saguão')
    opcoes = 'não'
            