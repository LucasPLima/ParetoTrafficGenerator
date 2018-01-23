import string

from application_gen import paretoGen


##Quais os nós dependentes?
##Quantos nós dependentes?

##TaskA = Task0 ; TaskB = Task1 ...

def Envio(noIndependente, numberDependentes, dependentPosition, local):
    valoresON, valoresOFF = paretoGen.paretoCalculate()
    StrinON = '{' + ','.join(str(e) for e in valoresON) + '}'
    StrinOFF = '{' + ','.join(str(e) for e in valoresOFF) + '}'
    a = list(string.ascii_uppercase)
    print(a)
    b = list(string.ascii_uppercase)
    arquivo = open('{}/task{}.c'.format(local, noIndependente), 'w') ## -1 POIS O VETOR COMEÇA NA POSIÇÃO 0
    arquivo.write('#include <api.h>\n')
    arquivo.write('#include <stdlib.h>\n')
    arquivo.write('#include "syn_std.h"\n')
    arquivo.write('Message msg;\n')
    arquivo.write('int main()\n')
    arquivo.write('{\n')
    arquivo.write(' int i, j,t,b;\n')
    arquivo.write(' int valoresON[SYNTHETIC_ITERATIONS] = {};\n'.format(StrinON))
    arquivo.write(' int valoresOFF[SYNTHETIC_ITERATIONS] = {};\n'.format(StrinOFF))
    arquivo.write(' Echo("synthetic task {} started.");\n'.format(noIndependente))
    arquivo.write(' Echo(itoa(GetTick()));\n')

    for i in range(numberDependentes):
            arquivo.write(' for(i=0;i<SYNTHETIC_ITERATIONS;i++){\n')
            arquivo.write('     for(t=0;t<valoresOFF[i];t++){\n')
            arquivo.write('     }\n')
            arquivo.write('     msg.length = 30;\n')
            arquivo.write('     for(j=0;j<30;j++) msg.msg[j]=i;\n')
            arquivo.write('     for(b=0;b<valoresON[i];b++){\n')
            arquivo.write('         Send(&msg,task{});\n'.format(dependentPosition[i])) ##Como pegar a posição para o dependente?
            arquivo.write('     }\n')
            arquivo.write('}\n')
            pass

    arquivo.write('Echo(itoa(GetTick()));\n')
    arquivo.write('Echo("synthetic task {} finished.");\n'.format(noIndependente))
    arquivo.write('exit();\n')
    arquivo.write('}\n')

pass


def create_top(file,i):
    file.write('#include <api.h>\n')
    file.write('#include <stdlib.h>\n')
    file.write('#include "syn_std.h"\n')
    file.write('Message msg;\n')
    file.write('int main()\n')
    file.write('{\n')
    file.write('	int i, j,t;\n')
    file.write('	Echo("synthetic task {} started.");\n'.format(i))  ####
    file.write('	Echo(itoa(GetTick()));\n')
    file.write('for(i=0;i<SYNTHETIC_ITERATIONS;i++)\n')
    file.write('{\n')
    file.write('	msg.length = 30;\n')
    file.write('	for(j=0;j<30;j++) msg.msg[j]=i;\n')


def create_bottom(file,i):
    file.write('}\n')
    file.write('    Echo(itoa(GetTick()));\n')
    file.write('    Echo("synthetic task {} finished.");\n'.format(i))  ####
    file.write('	exit();\n')
    file.write('}\n')


