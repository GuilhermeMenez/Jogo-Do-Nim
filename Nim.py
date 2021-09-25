def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    opcao = int(input())
    if opcao == 1:
        partida()
    elif opcao == 2:
        campeonato()
    elif opcao == 0:
        pass
    else:
        print("Opcão invalida")
        partida()


def computador_escolhe_jogada(n, m):
    print("Vez do computador!")
    if n <= m:
        return n
    else:
        quantidade_retirada = n % (m + 1)
        if quantidade_retirada > 0:
            return quantidade_retirada
        else:
            return m


# 3 casos, digitar o numero errado, digitar o numero certo e nao ganhar, digitar o numero certo e nao ganhar
def usuario_escolhe_jogada(n, m):
    print("Sua vez\n")
    jogada_usuario = int(input("Quantas peças irá tirar\n"))
    if 0 < jogada_usuario <= m and jogada_usuario <= n:
        return jogada_usuario
    else:
        print("Jogada invalida")
        return usuario_escolhe_jogada(n, m)


def partida():
    global jogada
    n = int(input("Digite o numero de peças no jogo"))
    m = int(input("Digite o numero maximo de peças que podem ser retiradas"))
    turno_do_computador = True

    if (n % (m + 1)) == 0:
        turno_do_computador = False
    while n > 0:
        if turno_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            turno_do_computador = False
            print("Computador retirou ", jogada, " peças.")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            turno_do_computador = True
            print("Você retirou", jogada, "peças.")
        n = n - jogada
        print("Restam apenas", n, "peças em jogo.\n")

    if turno_do_computador:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0


def campeonato():
    usuario = 0
    computador = 0

    for i in range(3):
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario + 1
        else:
            # Computador venceu:
            computador = computador + 1

    print("Placar final: Você", usuario, "x", computador, "Computador")


inicio()
