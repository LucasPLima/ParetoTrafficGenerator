from application_gen import paretoGen


# Quais os nós dependentes?
# Quantos nós dependentes?

##TaskA = Task0 ; TaskB = Task1 ...

def Envio(noIndependente, numberDependentes, dependentPosition, local):
    valoresON, valoresOFF = paretoGen.paretoCalculate()
    aux = create_ctr(len(valoresON), numberDependentes)

    StrinON = '{' + ','.join(str(e) for e in valoresON) + '}'
    StrinOFF = '{' + ','.join(str(e) for e in valoresOFF) + '}'
    ctr = '{' + ','.join(str(e) for e in aux) + '}'

    syn = open('{}/syn_std.h'.format(local), 'w')
    create_syn_std(syn, len(valoresON), numberDependentes)

    arquivo = open('{}/task{}.c'.format(local, noIndependente), 'w')
    arquivo.write('#include <api.h>\n')
    arquivo.write('#include <stdlib.h>\n')
    arquivo.write('#include "syn_std.h"\n')
    arquivo.write('Message msg;\n')
    arquivo.write('const unsigned char valoresON[SYNTHETIC_ITERATIONS] = {};\n'.format(StrinON))
    arquivo.write('const unsigned char valoresOFF[SYNTHETIC_ITERATIONS] = {};\n'.format(StrinOFF))
    arquivo.write('const unsigned short int ctr[{}] = {}\n'.format(numberDependentes-1, ctr))
    arquivo.write('int main()\n')
    arquivo.write('{\n')
    arquivo.write('\tint i, j,k,t;\n')
    arquivo.write('\tEcho("synthetic task {} started.");\n'.format(noIndependente))
    arquivo.write('\tEcho(itoa(GetTick()));\n')
    arquivo.write('\tfor(i=0;i<SYNTHETIC_ITERATIONS;i++){\n')
    arquivo.write('\t\tmsg.length = 30;\n')
    arquivo.write('\t\tfor(j=0;j<30;j++) msg.msg[j]=i;\n')
    arquivo.write('\t\tfor(k=0;k<valoresON[i];k++){\n')
    arquivo.write('\t\t\tSend(&msg,task{});\n'.format(dependentPosition[0]))
    arquivo.write('\t\t\tfor(t=0;t<valoresOFF[i]*100;t++){\n')
    arquivo.write('\t\t\t}\n')
    arquivo.write('\t\t}\n')

    for i in range(len(aux)):
        arquivo.write('\t\tfor(j=0;j<30;j++) msg.msg[j]=i;\n')
        arquivo.write('\t\tfor(k=0;k<valoresON[i+ctr[{}]];k++){a}\n'.format(i, a='{'))
        arquivo.write('\t\t\tSend(&msg,task{});\n'.format(dependentPosition[i+1]))
        arquivo.write('\t\t\tfor(t=0;t<valoresOFF[i+ctr[{}]]*100;t++){a}\n'.format(i, a='{'))
        arquivo.write('\t\t\t}\n')
        arquivo.write('\t\t}\n')
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


def create_syn_std(file, iterations, n_dep):
    file.write('#ifndef SYN_STD_H_\n')
    file.write('#define SYN_STD_H_\n\n\n')
    file.write('#define SYNTHETIC_ITERATIONS\t{}\n\n'.format(round(iterations/n_dep)))
    file.write('#endif')


def create_ctr(a_size, n_dep):
    aux = []
    a = round(a_size/n_dep)
    aux.append(a)
    for i in range(2,n_dep):
        aux.append(a*i)

    if a_size % n_dep == n_dep-1 or a_size % n_dep == n_dep-2:
        for i in range(len(aux)):
            aux[i] = aux[i] - (n_dep-(a_size % n_dep))

    return aux




