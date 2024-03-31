
  
"""
Nomes dos integrantes do grupo:
- Leonardo de Goes da Silva
- Nicolas Aparecido Ferreira
- Vithor Augusto Andrade
- Felipe Fernandes Bortolino
- João Victor Repula Cordeiro
"""
import random
import time

tempoFinal = 0
tempoFinal1 = 0
tempoFinal2 = 0
tempoTotal = 0

pontof = 0
pontoP1 = 0
pontoP2 = 0

tasksom = 0
tasksub = 0
taskmult = 0
taskdiv = 0

som = 0
sub = 0
mult = 0
div = 0

pontoSom = 0
pontoSub = 0
pontoMult = 0
pontoDiv = 0

#start
print('JOGO DE MATEMÁTICA')
print('[1] Singleplayer')
print('[2] Multiplayer')

##Valores randômicos
randomNegativo = 0
randomPositivo = 0

modoDeJogo = int(input("Escolha o modo de jogo:"))

#singleplayer
if(modoDeJogo == 1 or modoDeJogo == 2):
    print('[1] Fácil (-10 a 10)')
    print('[2] Médio (-100 a 100)')
    print('[3] Díficil (-1000 a 1000)')

    start = int(input('Escolha sua dificuldade:'))
    if start == 1:
        randomNegativo = -10
        randomPositivo = 10
    elif start == 2:
        randomNegativo = -100
        randomPositivo = 100
    elif start == 3:
        randomNegativo = -1000
        randomPositivo = 1000
    else:
        print("valor invalido")

    tempoInicialSoma= time.time()

    # SOMA
    n1 = random.randint(randomNegativo, randomPositivo)
    n2 = random.randint(randomNegativo, randomPositivo)
    som = n1 + n2
    tasksom = int(input(f'{n1} + {n2} ='))
    tempoFinalSoma = time.time()

    tempoTotalSoma= tempoInicialSoma - tempoFinalSoma

    # SUBTRAÇÃO
    tempoInicialSubtracao = time.time()
    n1 = random.randint(randomNegativo, randomPositivo)
    n2 = random.randint(randomNegativo, randomPositivo)
    sub = n1 - n2
    tasksub = int(input(f'{n1} - {n2} ='))
    tempoFinalSubtracao= time.time()

    tempoTotalSubtracao= tempoInicialSubtracao - tempoFinalSubtracao

    # MULTIPLICAÇÃO
    tempoInicialMultiplicacao = time.time()
    n1 = random.randint(randomNegativo, randomPositivo)
    n2 = random.randint(randomNegativo, randomPositivo)
    mult = n1 * n2
    taskmult = int(input(f'{n1} x {n2} ='))
    tempoFinalMultiplicacao = time.time()

    tempoTotalMultiplicacao = tempoInicialMultiplicacao - tempoFinalMultiplicacao


    # DIVISÃO
    tempoDivisaoInicio = time.time()
    n1 = random.randint(randomNegativo, randomPositivo)
    n2 = random.randint(randomNegativo, randomPositivo)
    div = n1 // n2
    taskdiv = int(input(f'{n1} / {n2} ='))

    tempoDivisaoFinal = time.time()
    tempoTotalDivisao = tempoDivisaoInicio - tempoDivisaoFinal
    tempoTotalPlayer1 = tempoTotalMultiplicacao - tempoTotalDivisao - tempoTotalSoma - tempoTotalSubtracao

    # PONTUAÇÃO---------------------------------------------------------
    if(modoDeJogo == 1):
        if (start <= 3):
        # SOMA
            if (tasksom == som):
                if (tempoTotalSoma > 5):
                    ponto = abs(((tempoTotalSoma - 5) * 0.2) - 10)
                    pontoSom = ponto
                else:
                    pontoSom = 10
            else:
                pontoSom = 0
        # SUBTRAÇÃO
            if (tasksub == sub):
                if (tempoTotalSubtracao > 5):
                    ponto = abs(((tempoTotalSubtracao - 5) * 0.2) - 10)
                    pontoSub = ponto
                else:
                    pontoSub = 10
            else:
                pontoSub = 0
        # MULTIPLICAÇÃO
            if (taskmult == mult):
                if (tempoTotalMultiplicacao > 5):
                    ponto = abs(((tempoTotalMultiplicacao - 5) * 0.2) - 10)
                    pontoMult = ponto
                else:
                    pontoMult = 10
            else:
                pontoMult = 0
        # DIVISÃO
            if (taskdiv == div):
                if (tempoTotalDivisao > 5):
                    ponto = abs(((tempoTotalDivisao - 5) * 0.2) - 10)
                    pontoDiv = ponto
                else:
                    pontoDiv = 10
            else:
                pontoDiv = 0
                pontof = int(pontoSom + pontoSub + pontoMult + pontoDiv)
        # RESULTADO
            if (pontof > 0):
                print(f'Pontuação: {pontof} pontos')
                print(f'Tempo de jogo: {tempoTotalPlayer1:.2f}s')
                print('FIM DE JOGO')
            elif (pontof == 0):
                print('Errou tudo')
    elif(modoDeJogo == 2):
        #PLAYER 2------------------------------------------
            input('(PLAYER 2) Aperte enter para começar')
            tempoInicialSoma= time.time() # início do tempo

            # SOMA
            n1 = random.randint(randomNegativo, randomPositivo)
            n2 = random.randint(randomNegativo, randomPositivo)
            som = n1 + n2
            tasksom = int(input(f'{n1} + {n2} ='))
            tempoFinalSoma = time.time()

            tempoTotalSoma= tempoInicialSoma - tempoFinalSoma

            # SUBTRAÇÃO
            tempoInicialSubtracao = time.time()
            n1 = random.randint(randomNegativo, randomPositivo)
            n2 = random.randint(randomNegativo, randomPositivo)
            sub = n1 - n2
            tasksub = int(input(f'{n1} - {n2} ='))
            tempoFinalSubtracao= time.time()

            tempoTotalSubtracao= tempoInicialSubtracao - tempoFinalSubtracao

            # MULTIPLICAÇÃO
            tempoInicialMultiplicacao = time.time()
            n1 = random.randint(randomNegativo, randomPositivo)
            n2 = random.randint(randomNegativo, randomPositivo)
            mult = n1 * n2
            taskmult = int(input(f'{n1} x {n2} ='))
            tempoFinalMultiplicacao = time.time()

            tempoTotalMultiplicacao = tempoInicialMultiplicacao - tempoFinalMultiplicacao
            # DIVISÃO
            tempoDivisaoInicio = time.time()
            n1 = random.randint(randomNegativo, randomPositivo)
            n2 = random.randint(randomNegativo, randomPositivo)
            div = n1 // n2
            taskdiv = int(input(f'{n1} / {n2} ='))

            tempoTotalPlayer2 = tempoTotalMultiplicacao - tempoTotalDivisao - tempoTotalSoma - tempoTotalSubtracao

            if (start <= 3):
                # SOMA
                if (tasksom == som):
                    if (tempoTotalSoma > 5):
                        ponto = abs(((tempoTotalSoma - 5) * 0.2) - 10)
                        pontoSom = ponto
                    else:
                        pontoSom = 10
                else:
                        pontoSom = 0
            # SUBTRAÇÃO
            if (tasksub == sub):
                if (tempoTotalSubtracao > 5):
                    ponto = abs(((tempoTotalSubtracao - 5) * 0.2) - 10)
                    pontoSub = ponto
                else:
                    pontoSub = 10
            else:
                pontoSub = 0
            # MULTIPLICAÇÃO
            if (taskmult == mult):
                if (tempoTotalMultiplicacao > 5):
                    ponto = abs(((tempoTotalMultiplicacao - 5) * 0.2) - 10)
                    pontoMult = ponto
                else:
                    pontoMult = 10
            else:
                pontoMult = 0
            # DIVISÃO
            if (taskdiv == div):
                if (tempoTotalDivisao > 5):
                    ponto = abs(((tempoTotalDivisao - 5) * 0.2) - 10)
                    pontoDiv = ponto
                else:
                    pontoDiv = 10
            else:
                pontoDiv = 0
            pontoP1 = int(pontoSom + pontoSub + pontoMult + pontoDiv)

        # pontos player 2
            if (start <= 3):
            # SOMA
                if (tasksom == som):
                    if (tempoTotalSoma > 5):
                        ponto = abs(((tempoTotalSoma - 5) * 0.2) - 10)
                        pontoSom = ponto
                else:
                    pontoSom = 10
            else:
                pontoSom = 0
            # SUBTRAÇÃO
            if (tasksub == sub):
                if (tempoTotalSubtracao > 5):
                    ponto = abs(((tempoTotalSubtracao - 5) * 0.2) - 10)
                    pontoSub = ponto
                else:
                    pontoSub = 10
            else:
                pontoSub = 0
            # MULTIPLICAÇÃO
            if (taskmult == mult):
                if (tempoTotalMultiplicacao > 5):
                    ponto = abs(((tempoTotalMultiplicacao - 5) * 0.2) - 10)
                    pontoMult = ponto
                else:
                    pontoMult = 10
            else:
                pontoMult = 0
            # DIVISÃO
            if (taskdiv == div):
                if (tempoTotalDivisao > 5):
                    ponto = abs(((tempoTotalDivisao - 5) * 0.2) - 10)
                    pontoDiv = ponto
                else:
                    pontoDiv = 10
            else:
                pontoDiv = 0
            pontoP2 = int(pontoSom + pontoSub + pontoMult + pontoDiv)

        #RESULTADO
            if (pontoP1 > pontoP2):
                print(f'Primeiro lugar: Player1 = {pontoP1} pontos.Tempo de jogo: {tempoTotalPlayer1:.2f}s')
                print(f'Segundo lugar: Player2 = {pontoP2} pontos.Tempo de jogo: {tempoTotalPlayer2:.2f}s')
                print('FIM DE JOGO')
            elif (pontoP1 < pontoP2):
                print(f'Primeiro lugar: Player2 = {pontoP2} pontos.Tempo de jogo: {tempoTotalPlayer2:.2f}s')
                print(f'Segundo lugar: Player1 = {pontoP1} pontos.Tempo de jogo: {tempoTotalPlayer1:.2f}s')
                print('FIM DE JOGO')
            elif (start <= 3 and pontoP1 == pontoP2):
                print('EMPATE')
                print('FIM DE JOGO')
            else:
                print('INVÁLIDO')



    
