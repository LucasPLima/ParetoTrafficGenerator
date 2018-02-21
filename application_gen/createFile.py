from application_gen import paretoGen


# Quais os nós dependentes?
# Quantos nós dependentes?

##TaskA = Task0 ; TaskB = Task1 ...

def Envio(noIndependente, numberDependentes, dependentPosition, local):
    valoresON, valoresOFF = paretoGen.paretoCalculate()
    aux = create_ctr(len(valoresON),numberDependentes)

    StrinON = '{' + ','.join(str(e) for e in valoresON) + '}'
    StrinOFF = '{' + ','.join(str(e) for e in valoresOFF) + '}'
    syn = open('{}/syn_std.h'.format(local), 'w')
    create_syn_std(syn, len(valoresON))

    arquivo = open('{}/task{}.c'.format(local, noIndependente), 'w')
    arquivo.write('#include <api.h>\n')
    arquivo.write('#include <stdlib.h>\n')
    arquivo.write('#include "syn_std.h"\n')
    arquivo.write('Message msg;\n')
    arquivo.write('const unsigned char valoresON[SYNTHETIC_ITERATIONS] = {};\n'.format(StrinON))
    arquivo.write('const unsigned char valoresOFF[SYNTHETIC_ITERATIONS] = {};\n'.format(StrinOFF))
    arquivo.write('int main()\n')
    arquivo.write('{\n')
    arquivo.write('\tint i, j,t,b;\n')
    arquivo.write('\tEcho("synthetic task {} started.");\n'.format(noIndependente))
    arquivo.write('\tEcho(itoa(GetTick()));\n')

    for i in range(numberDependentes):
            arquivo.write('\tfor(i=0;i<SYNTHETIC_ITERATIONS;i++){\n')
            arquivo.write('\t\tfor(t=0;t<valoresOFF[i];t++){\n')
            arquivo.write('\t\t}\n')
            arquivo.write('\t\tmsg.length = 30;\n')
            arquivo.write('\t\tfor(j=0;j<30;j++) msg.msg[j]=i;\n')
            arquivo.write('\t\tfor(b=0;b<valoresON[i];b++){\n')
            arquivo.write('\t\t\t\tSend(&msg,task{});\n'.format(dependentPosition[i])) # Como pegar a posição para o dependente?
            arquivo.write('\t\t\t}\n')
            arquivo.write('\t}\n')
            pass

    arquivo.write('\tEcho(itoa(GetTick()));\n')
    arquivo.write('\tEcho("synthetic task {} finished.");\n'.format(noIndependente))
    arquivo.write('\texit();\n')
    arquivo.write('}\n')

    arquivo.close()
    syn.close()

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


def create_syn_std(file, iterations):
    file.write('#ifndef SYN_STD_H_\n')
    file.write('#define SYN_STD_H_\n\n\n')
    file.write('#define SYNTHETIC_ITERATIONS\t{}\n\n'.format(iterations))
    file.write('#endif')


def create_ctr(a_size, n_dep):
    aux = []
    a = round(a_size/n_dep)
    aux.append(a)
    for i in range(2,n_dep+1):
        aux.append(a*i)

    if j % 5 == 4 or j % 5 == 3:
        aux[-1] = aux[-1]-1

    return aux




