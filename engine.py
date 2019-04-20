
"""
Created on Wed Apr 17 19:18:56 2019

@author: joaopedrochacon
"""

import random
import time
import json
from PIL import Image



inventario = []


## Funcao Random Number Generation
def rng():
    rng = random.randint(0, 10)
    return rng


class Stats:    
    vida = 100
    
    def combate_raul(self): 
        vidaraul = 50 
        if rng() > 0:
            print("Voce encontrou seu ultimo desafio: Raul, o Mestre do Python")
            time.sleep(0.5)
            print("Não há escapatória, DP não é mais uma opção, lutem até a MORTE!")
            while vidaraul > 0 and self.vida > 0:
                dano_no_monstro = rng() # dano causado pelo jogador
                if dano_no_monstro == 10: ## Acerto critico
                    print("Acerto critico! Pena que o mestre do python é imune a dano extra..")
                    vidaraul = vidaraul - dano_no_monstro
                else:
                    if "Estilete" in inventario:
                        dano_no_monstro += 2
                    vidaraul = vidaraul - dano_no_monstro
                    dano_no_jogador = rng() # dano causado pelo monstro
                    if "Fone do Pelicano" in inventario:
                        dano_no_jogador = 0
                    elif "Papelao" in inventario and dano_no_jogador >= 2:
                        dano_no_jogador = dano_no_jogador - 2
                    self.vida = self.vida - dano_no_jogador
                    if self.vida < 0:
                        self.vida = 0
                    print("Você levou",dano_no_jogador, "de dano e está com", self.vida, "de vida")
                    time.sleep(0.5)
                    if vidaraul <= 0: ## nao deixa vida do monstro ser menor que 0
                        vidaraul = 0
                        print("Você venceu!") 
                        ganhou = True
                    else:
                        print("Você causou" ,dano_no_monstro, "de dano no Raul, e ele esta com", 
                          vidaraul, "de vida")
                    time.sleep(0.5)
            

    
    ## Funcao do combate
    def combate(self): 
        vidamonstro = 20 ## Como sao diferentes monstros a vida reseta cada vez q roda a funcao
        if rng() > 3:
            print("Você encontrou um monstro!")
            decisao = input("Você quer lutar ou correr?:")
        
        
        ## Sistema de fuga
            while decisao == "correr" and self.vida > 0:
                if rng() < 1: ## % de chance de conseguir fugir
                    print("Can't escape!")
                    time.sleep(0.5)
                    dano_no_jogador = rng() ## dano do mostro se nao conseguir fugir
                    if "Fone do Pelicano" in inventario:
                        dano_no_jogador = 0
                    elif "Papelao" in inventario:
                        dano_no_jogador = dano_no_jogador - 2
                    self.vida = self.vida - dano_no_jogador
                    if self.vida < 0:
                        self.vida = 0
                    print("Você levou",dano_no_jogador, "de dano e está com", self.vida, "de vida")
                    time.sleep(0.5)
                    decisao = input("Você quer lutar ou correr?:")
                    time.sleep(0.5)
                else:
                    print("Você fugiu")
                    decisao = "fim"
                
                
        ## Sistema de luta    
            if decisao == "lutar":
                while vidamonstro > 0 and self.vida > 0:
                    dano_no_monstro = rng() # dano causado pelo jogador
                    if dano_no_monstro == 10: ## Acerto critico
                        print("Acerto critico! você causou" ,dano_no_monstro * 2, 
                              "de dano no monstro!")
                        vidamonstro = 0
                    else:
                        if "Estilete" in inventario:
                            dano_no_monstro += 2
                        vidamonstro = vidamonstro - dano_no_monstro
                        dano_no_jogador = rng() # dano causado pelo monstro
                        if "Fone do Pelicano" in inventario:
                            dano_no_jogador = 0
                        elif "Papelao" in inventario and dano_no_jogador >= 2:
                            dano_no_jogador = dano_no_jogador - 2
                        self.vida = self.vida - dano_no_jogador
                        if self.vida < 0:
                            self.vida = 0
                        print("Você levou",dano_no_jogador, "de dano e está com", self.vida, "de vida")
                        time.sleep(0.5)
                        if vidamonstro <= 0: ## nao deixa vida do monstro ser menor que 0
                            vidamonstro = 0
                            print("Você matou o monstro!") 
                        print("Você causou" ,dano_no_monstro, "de dano no monstro, e ele esta com", 
                              vidamonstro, "de vida")
                        time.sleep(0.5)
            

jogador = Stats()





#criando dado
def dado():
    dado=random.randint(1,20)
    return dado



#itens                                     

mapa_da_DP=5
caneta_do_Raul=0
pendrive_da_punicao=2
livro_da_salvacao=5

#inventario

inventario=[]
game_over=False


###função itens

def itens_no_cenario(nome_do_cenario): 
    with open('texto_cenarios.txt','r') as arquivo:
        conteudo = arquivo.read()
        objetos = json.loads(conteudo)
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
    time.sleep(1)
    print("MUITO IMPORTANTE!")
    time.sleep(2)
    print("Por favor, meu consagrado...")
    time.sleep(2)
    print("Ao longo do jogo, digite TUDO com letra minúscula e sem acento")
    time.sleep(2)
    print("Aproveite a experiência e não se esqueça...")
    print("Se o EP já está difícil, imagina a PF...")
    time.sleep(3)
    print()
    print("Na hora do sufoco!")
    print("------------------")
    print()
    time.sleep(1.5)
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    time.sleep(4)
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
        
    i=0
    game_over = False
    ganhou=False
    while not game_over:
        if i == 0:
            inicio=carregar_cenarios('saguao')
            time.sleep(6)
            print()
            print()
            print('Saguão')
            tamanho=len('Saguao')
            print('-'*tamanho)
            print('Você está no saguão do Insper')
            time.sleep(2)
            print('Nessa sala temos esses itens:')
            time.sleep(2)
            print(itens_no_cenario('saguao'))
            time.sleep(2)
            numero_dado=dado()
            print('O número sorteado no dado foi',numero_dado)
            if numero_dado<=15:
                if "Mapa da DP" not in inventario:
                    inventario.append('Mapa da DP')
                    print('Você encontrou o Mapa da DP')       
                    print('-5 de vida a cada rodada')
                    time.sleep(2)
                   
            elif numero_dado > 7:
                print("Que azar! Você não encontrou nenhum item")
            print('''Você tem essas opções de lugares para ir: 
 1- Sujinhuus 
 2- Fab Lab''')
            time.sleep(2)
            opcoes=input('Qual desses lugares você quer ir? ')
            if opcoes=='sujinhuus':
                inicio=carregar_cenarios('sujinhuus')
            elif opcoes=='fab lab':
                inicio=carregar_cenarios('fab lab')
            else:
                game_over=True
                print('Digitou errado! WASTED!')
            i+=1
        else:
            jogador.combate()
            if jogador.vida==0:
                game_over=True
            else:
                if inicio=='cenario1':
                    print()
                    print()
                    print('Saguão')
                    tamanho=len('Saguao')
                    print('-'*tamanho)
                    print('Você está no saguão do Insper')
                    time.sleep(2)
                    print('Nessa sala temos esses itens:')
                    time.sleep(2)
                    print(itens_no_cenario('saguao'))
                    time.sleep(2)
                    numero_dado=dado()
                    print('O número sorteado no dado foi', numero_dado)
                    if numero_dado <= 7:
                        if "Mapa da DP" not in inventario:
                            inventario.append('Mapa da DP')
                            print('Você encontrou o Mapa da DP')       
                            print('-5 de vida a cada rodada')
                            time.sleep(3)
                    elif numero_dado > 7:
                        print("Que azar! Você não encontrou nenhum item")
                        time.sleep(2)
                    print('''Você tem essas opções de lugares para ir: 
1- Sujinhuus 
2- Fab Lab''')
                    time.sleep(2)
                    opcoes=input('Qual desses lugares você quer ir? ')
                    if opcoes=='sujinhuus':
                        inicio=carregar_cenarios('sujinhuus')
                    elif opcoes=='fab lab':
                        inicio=carregar_cenarios('fab lab')
                    else:
                        game_over=True
                        print('Digitou errado! WASTED!')
                elif inicio=='cenario2':
                    print()
                    print()
                    print('Sala do Raul')
                    tamanho=len('Sala do Raul')
                    print('-'*tamanho)
                    print('Você está na porta da Sala do Raul')
                    time.sleep(2)
                    if 'Chave da sala do Raul' not in inventario:
                        print('Você não consegue entrar na Sala do Raul, ainda falta um item para ser encontrado')
                    else:
                        resposta = input('Tem certeza que quer entrar? Pode ser um caminho sem volta (sim/nao):')
                        if resposta == "sim":
                            jogador.combate_raul()
                            if jogador.vida > 0:
                                ganhou = True
                            else: 
                                game_over = True
                            break
                        else:
                            print('''Você tem essas opções de lugares para ir: 
1- Sujinhuus 
2- Fab Lab''')
                            opcoes=input('Qual desses lugares você quer ir? ')
                    print('''Você tem essas opções de lugares para ir: 
1- Fab Lab 
2- Biblioteca''')
                    opcoes=input('Qual desses lugares você quer ir? ')
                    if opcoes=='fab lab':
                        inicio=carregar_cenarios('fab lab')
                    elif opcoes=='biblioteca':
                        inicio=carregar_cenarios('biblioteca')
                    else:
                        game_over=True
                        print('Digitou errado! WASTED!')
                elif inicio=='cenario3':
                    print()
                    print()
                    print('Biblioteca')
                    tamanho=len('Biblioteca')
                    print('-'*tamanho)
                    print('Você está na biblioteca do Insper')
                    time.sleep(2)
                    print('Nessa sala temos esses itens:')
                    time.sleep(2)
                    print(itens_no_cenario('biblioteca'))
                    time.sleep(3.5)
                    numero_dado=dado()
                    print('O número sorteado no dado foi',numero_dado)
                    if 'Mapa para o livro da Salvação' in inventario:
                        if 'Livro da Salvação' not in inventario:
                            inventario.append('Livro da Salvação')
                            print('Buscando um milagre.... e com o mapa em mãos Você encontrou o Livro da Salvação')
                            time.sleep(2.5)
                            print('Com todo o conhecimento vindo do livro, você será premiado com +5 pontos de vida a cada rodada')
                            time.sleep(3)
                    if numero_dado <=18:
                        if 'Chave da sala do Raul' not in inventario:
                            inventario.append('Chave da sala do Raul')
                            print('Você encontrou a chave da sala do Raul')
                            time.sleep(2)
                            print('Use a com sabedoria')
                    if numero_dado>=19:
                        if 'Fone do Pelicano' not in inventario:
                            print('Não é possível...')
                            time.sleep(1)
                            print('Você encontrou o Fone do Pelicano')
                            time.sleep(1.5)
                            print('Agora você está mais forte do que o GOKU!')
                            time.sleep(1.5)
                            print('Você está IMORTAL')
                            time.sleep(1.5)
                            inventario.append('Fone do Pelicano')
                    elif numero_dado < 19 and numero_dado > 18:
                        print("Que azar! Você não encontrou nenhum item")
                    print('''Você tem essas opções de lugares para ir: 
1- Sala do Raul 
2- Fab Lab
3- Aquario''')
                    opcoes=input('Qual desses lugares você quer ir?  ')
                    if opcoes=='sala do raul':
                        inicio=carregar_cenarios('sala do raul')
                    elif opcoes=='fab lab':
                        inicio=carregar_cenarios('fab lab')
                    elif opcoes=='aquario':
                        inicio=carregar_cenarios('aquario')
                    else:
                        game_over=True
                        print('Digitou errado! WASTED!')
                elif inicio=='cenario4':
                    print()
                    print()
                    print('Fab Lab')
                    tamanho=len('Fab Lab')
                    print('-'*tamanho)
                    print('Você está no Fab Lab do Insper')
                    time.sleep(2)
                    print('Nessa sala temos esses itens:')
                    time.sleep(2)
                    print(itens_no_cenario('fab lab'))
                    time.sleep(2)
                    numero_dado=dado()
                    print('O número sorteado no dado foi',numero_dado)
                    if numero_dado>=7:
                        if 'Estilete' not in inventario and 'Papelão' not in inventario:
                            inventario.append('Estilete')
                            inventario.append('Papelão')
                            print('Você ganhou o estilete')
                            print('Dano recebe +2 pontos')
                            time.sleep(2)
                            print('Você ganhou um escudo de papelão')
                            print('Recebe -2 pontos de dano')
                            time.sleep(2)
                    if numero_dado < 7:
                        print("Que azar! Você não encontrou nenhum item")
                    print('''Você tem essas opções de lugares para ir:
1- Biblioteca
2- Sala do Raul''')
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
                    print()
                    print()
                    print('Bem vindo ao Sujinhuus! Vamos te apresentar as nossas opções de bebida:')
                    time.sleep(2)
                    print('-litrão nosso de todo dia')
                    time.sleep(0.5)
                    print('-corote do amor')
                    time.sleep(0.5)
                    print('-caipirinha do role')
                    time.sleep(0.5)
                    escolha = input('Vai querer tomar alguma coisa ou ir embora? Se quiser algo, digite o nome da bebida. Senão, digite ir embora. ')
                    while escolha != 'ir embora':
                        if escolha == 'litrao nosso de todo dia':
                            alcool += 1
                            escolha = input('Vai querer tomar mais alguma coisa ou ir embora? Se quiser algo, digite o nome da bebida. Senão, digite ir embora. ')
                        elif escolha == 'corote do amor':
                            alcool += 1
                            escolha = input('Vai querer tomar mais alguma coisa ou ir embora? Se quiser algo, digite o nome da bebida. Senão, digite ir embora. ')
                        elif escolha == 'caipirinha do role':
                            alcool +=1
                            escolha = input('Vai querer tomar mais alguma coisa ou ir embora? Se quiser algo, digite o nome da bebida. Senão, digite ir embora. ')
                        else:
                            print('Não temos isso, perdeu a chance de pedir! Vai ter que ir embora.')
                            escolha == 'ir embora'
                    if alcool > 0:
                        print('Você não pode voltar ao Insper tendo bebido!')
                        game_over = True
                    else:
                        inicio=carregar_cenarios('saguao')
                elif inicio=='cenario6':
                    print()
                    print()
                    print('Aquário')
                    tamanho=len('Aquário')
                    print('-'*tamanho)
                    print('Por algum motivo desconhecido, você deu sorte de encontrar um aquário vazio na biblioteca')
                    time.sleep(2)
                    print('Você encontrou o mapa de todas as salas!')
                    time.sleep(2)
                    wish=input('Você deseja visualizar o mapa? ')
                    print()
                    print()
                    if wish=='sim':
                        img=Image.open('mapa.png')
                        img.show()
                    print()
                    print()
                    print('Agora você sabe todos os caminhos')
                    time.sleep(1)
                    print('mas...')
                    time.sleep(1)
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
        time.sleep(0.4)
        print('███████████████████████████')
        time.sleep(0.4)
        print('███████▀▀▀░░░░░░░▀▀▀███████')
        time.sleep(0.4)
        print('████▀░░░░░░░░░░░░░░░░░▀████')
        time.sleep(0.4)
        print('███│░░░░░░░░░░░░░░░░░░░│███')
        time.sleep(0.4)
        print('██▌│░░░░░░░░░░░░░░░░░░░│▐██')
        time.sleep(0.4)
        print('██░└┐░░░░░░░░░░░░░░░░░┌┘░██')
        time.sleep(0.4)
        print('██░░└┐░░░░░░░░░░░░░░░┌┘░░██')
        time.sleep(0.4)
        print('██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██')
        time.sleep(0.4)
        print('██▌░│██████▌░░░▐██████│░▐██')
        time.sleep(0.4)
        print('███░│▐███▀▀░░▄░░▀▀███▌│░███')
        time.sleep(0.4)
        print('██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██')
        time.sleep(0.4)
        print('██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██')
        time.sleep(0.4)
        print('████▄─┘██▌░░░░░░░▐██└─▄████')
        time.sleep(0.4)
        print('█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████')
        time.sleep(0.4)
        print('████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████')
        time.sleep(0.4)
        print('█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████')
        time.sleep(0.4)
        print('███████▄░░░░░░░░░░░▄███████')
        time.sleep(0.4)
        print('██████████▄▄▄▄▄▄▄██████████')
        time.sleep(0.4)
        print('███████████████████████████')
        print()
        print('Você perdeu :(')
        print('Nos vemos na DP!')
         
            
            
            
# Programa principal.
if __name__ == "__main__":
    main()            
            
            
            
           



        