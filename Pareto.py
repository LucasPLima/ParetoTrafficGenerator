import random
import string
import CreateFile

    ###############INICIALIZAÇÃO##################
def paretoCalculate():
    packetSendTime = 30
    eton =   50 * (10 ** (-3))
    etoff =  40 * (10 ** (-3))
    h = 0.75
    simulationTime = 1000 ## É PRECISO CRIAR UM LIMITE, QUE SEJA DE TAMANHO IGUAL AO SYNTHETIC INTERATIONS
    time = 0

    aux = 5

    valoresON = []
    valoresOFF = []
    ###############INICIALIZAÇÃO##################

    ##################PARETO######################

    alphaON = 3 - 2 * h
    ro = eton / (eton + etoff)
    alphaOFF = ((1 - ro) * alphaON) / (((1 - ro) * alphaON) - (ro * (alphaON - 1)))

    while time < simulationTime:
        u = random.uniform(0,1)
        pON = round(u ** (-1 / alphaON))
        pOFF = round(u ** (-1 / alphaOFF))

        ton = pON * packetSendTime
        toff = pOFF * packetSendTime
        print(ton,toff)

        for i in range(pON):
            print('Envia Pacote{}'.format(i+1))
            pass
        print('Tempo Ocioso: {}'.format(toff))

        valoresON.append(ton)
        valoresOFF.append(toff)
        ##print(valoresON)
        ##print(valoresOFF)

        time = time + toff + ton

        ##pass

    return (valoresON, valoresOFF)
    ##################PARETO######################

