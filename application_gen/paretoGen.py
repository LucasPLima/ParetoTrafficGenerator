import random


###############INICIALIZAÇÃO##################
def paretoCalculate():
    packetSendTime = 30
    eton = 50 * (10 ** (-6))
    etoff = 60 * (10 ** (-6))
    h = 0.75
    simulationTime = 100000 ## É PRECISO CRIAR UM LIMITE, QUE SEJA DE TAMANHO IGUAL AO SYNTHETIC INTERATIONS
    time = 0

    valoresON = []
    valoresOFF = []

    alphaON = 3 - 2 * h
    ro = eton / (eton + etoff)
    alphaOFF = ((1 - ro) * alphaON) / (((1 - ro) * alphaON) - (ro * (alphaON - 1)))

    while time < simulationTime:
        u = random.uniform(0,1)
        pON = round(u ** (-1 / alphaON))
        pOFF = round(u ** (-1 / alphaOFF))

        ton = pON * packetSendTime
        toff = pOFF * packetSendTime

        print('Tempo de envio:{}\tTempo ocioso:{}'.format(pON,pOFF))

        for i in range(pON):

            pass


        valoresON.append(pON)
        valoresOFF.append(pOFF)

        time = time + toff + ton
    print(len(valoresON), len(valoresOFF))

    return (valoresON, valoresOFF)
    ##################PARETO######################

if __name__ == '__main__':
    paretoCalculate()