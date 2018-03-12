tabuleiro = ['', '', '', '', '', '', '', '', '']
tabAuxiliar = ['', '', '', '', '', '', '', '', '']
_Result = ['', '', '', '', '', '', '', '', '']
tabEstFinal = [['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', '']]
simboloP = ''
simboloC = ''

def menu():
    global simboloP
    global simboloC

    while True:
        simboloP = input("Qual símbolo você deseja? ")
        if simboloP == 'x' or simboloP == 'o':
            break
        else:
            print("Símbolo inválido!")

    if simboloP == 'x':
        simboloC == 'o'
    else:
        simboloC == 'x'

def movPlayer():
    global simboloP
    global tabuleiro
    global tabuleiro

    while True:
        pos = int(input("Digite a posição que você deseja: "))
        if pos < 0 or pos > 8:
            print('Posição inválida!')
        elif tabuleiro[pos] != '':
            print('Posição já marcada!')
            pos = -1
        else:
            break
    tabuleiro[pos] = simboloP

def movCPU(aSimbolo, aMiniMax, aNivel, aNivelPai):
    _FlagMarcado  = False
    _MiniMax       = 0
    _Continue      = False
    _FlagFinaliza = False

    global tabAuxiliar
    global tabuleiro
    global tabEstFinal
    global simboloP
    global simboloC
    global _Result

    for i in range(0, 8):
        if tabAuxiliar[i] != '':
            continue

        for j in range(0, 8):
            if tabEstFinal[j][0] == aNivelPai:
                if tabEstFinal[j][1] == i:
                    _Continue = True
                    break

        if _Continue:
            _Continue = False
            continue

        if not _FlagMarcado:
            tabAuxiliar[i] = aSimbolo
            _FlagMarcado   = True

            for j in range(0, 8):
                if tabEstFinal[j][1] == 0:
                    tabEstFinal[j][0] = aNivelPai
                    tabEstFinal[j][1] = i
                    break

        if estadoFinalVencedor(tabAuxiliar, aSimbolo):
            if aSimbolo == simboloP:
                if aMiniMax != -1:
                    aMiniMax = 1
                else:
                    aMiniMax = -1

            return aMiniMax
            break

        if estadoFinal(tabAuxiliar):
            if aMiniMax != -1:
                aMiniMax = 0
            return aMiniMax
            break

        if aSimbolo == simboloC:
            _MiniMax = movCPU(simboloP, _MiniMax, aNivel + 1, aNivelPai + 1)
        else:
            _MiniMax = movCPU(simboloC, _MiniMax, aNivel + 1, aNivelPai + 1)

        if aNivel == 1:
            _Result[i] = _MiniMax

    tabAuxiliar[i] = ''

    for i in range(0, 8):
        if tabEstFinal[i][1] == aNivel:
            tabEstFinal[i][1] = 0
            tabEstFinal[i][2] = 0

    if aNivel == 1:
        for i in range(0, 8):
            if _Result[i] == -1:
                tabuleiro[i] = simboloC
                _FlagFinaliza = True

        if not _FlagFinaliza:
            for i in range(0, 8):
                if _Result[i] == 0:
                    tabuleiro[i] = simboloC
                    _FlagFinaliza = True

            if _FlagFinaliza:
                for i in range(0, 8):
                    if _Result[i] == 1:
                        tabuleiro[i] = simboloC

def estadoFinal(aTabuleiro):
    flagEstadoFinal = True;

    for i in range(0, 8):
        if aTabuleiro[i] == '':
            flagEstadoFinal = False
            break

    return flagEstadoFinal

def estadoFinalVencedor(aTabuleiro, aSimbolo):
    flagEstadoFinal = False

    if aTabuleiro[0] == aSimbolo and aTabuleiro[1] == aSimbolo and aTabuleiro[2] == aSimbolo:
        flagEstadoFinal = True

    if aTabuleiro[0] == aSimbolo and aTabuleiro[4] == aSimbolo and aTabuleiro[8] == aSimbolo:
        flagEstadoFinal = True

    if aTabuleiro[0] == aSimbolo and aTabuleiro[3] == aSimbolo and aTabuleiro[6] == aSimbolo:
        flagEstadoFinal = True

    if aTabuleiro[1] == aSimbolo and aTabuleiro[4] == aSimbolo and aTabuleiro[6] == aSimbolo:
        flagEstadoFinal = True

    if aTabuleiro[2] == aSimbolo and aTabuleiro[5] == aSimbolo and aTabuleiro[8] == aSimbolo:
        flagEstadoFinal = True

    if aTabuleiro[2] == aSimbolo and aTabuleiro[4] == aSimbolo and aTabuleiro[6] == aSimbolo:
        flagEstadoFinal = True

    if aTabuleiro[3] == aSimbolo and aTabuleiro[4] == aSimbolo and aTabuleiro[5] == aSimbolo:
        flagEstadoFinal = True

    if aTabuleiro[6] == aSimbolo and aTabuleiro[7] == aSimbolo and aTabuleiro[8] == aSimbolo:
        flagEstadoFinal = True

    return flagEstadoFinal

def desenhaTabuleiro():
    global tabuleiro

    for i in range(0, 8):
        if tabuleiro[i] == '':
            print('_', end="")
        else:
            print(tabuleiro[i], end="")

    print('');

def jogar():
    _MinMaxAux = 0

    global simboloC
    global simboloP
    global tabuleiro

    while True:
        movPlayer()
        if estadoFinalVencedor(tabuleiro, simboloP):
            desenhaTabuleiro()
            print('Você ganhou!')
            break

        for i in range(0, 8):
            tabAuxiliar[i] = tabuleiro[i]

        _MinMaxAux = movCPU(simboloC, _MinMaxAux, 1, 0)
        desenhaTabuleiro()
        if estadoFinalVencedor(tabuleiro, simboloC):
            desenhaTabuleiro()
            print('Você perdeu!')
            break

menu()
jogar()