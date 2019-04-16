# EP 2019-1: Escape Insper
#
# Alunos: 
# João Pedro Gianfaldoni de Andrade, joaopga1@al.insper.edu.br
# André Luís Silva Lopes, andrelsl1@al.insper.edu.br



import random
import time

inventario = ["Papelao"]

## Funcao Random Number Generation
def rng():
    rng = random.randint(0, 10)
    return rng


## Cria uma classe (em resumo isso faz com que a vida do jogador nao resete pra 100 cada vez que rodar a funcao)
class Stats:    
    vida = 100
    
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





def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        },
        "sala de teleporte": {
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


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

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        jogador.combate()
        if jogador.vida == 0
            game_over = True
        else:
            print(cenario_atual['titulo'])
            tamanho=len(cenario_atual['titulo'])
            print('-'*tamanho)
            print(cenario_atual['descricao'])
    
            opcoes = cenario_atual['opcoes']
            if len(opcoes) == 0:
                print("Acabaram-se suas opções! Mwo mwo mwooooo...")
                game_over = True
            else:
                print("Escolha sua opção")
                for k, v in opcoes.items():
                    print(k,":", v)
                escolha = input("O que você quer fazer?:")
    
                if escolha in opcoes:
                    nome_cenario_atual = escolha
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()