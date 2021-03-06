import random


def paretoCalculate(simulation_time):
    packetSendTime = random.uniform(0.01, 0.08)
    eton = 0.2
    etoff = 0.05
    h = random.uniform(0.90, 0.99)
    simulationTime = simulation_time
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

        if pON > 255:
            pON = 255

        if pOFF> 255:
            pOFF = 255

        valoresON.append(pON)
        valoresOFF.append(pOFF)

        time = time + toff + ton

    return valoresON, valoresOFF


if __name__ == '__main__':
    print(list(paretoCalculate(10000)))