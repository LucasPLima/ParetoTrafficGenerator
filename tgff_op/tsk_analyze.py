def matrix_create(nl):
    matrix = []
    for i in range(nl):
        l = []
        matrix.append(l)
    return matrix


def graph_select(file_list, graph_list, graph_n):
    for i in range(len(file_list)):
        if file_list[i] == '@TASK_GRAPH {}'.format(graph_n) + ' {':
            while file_list[i] != '}':
                graph_list.append(file_list[i])  # Anexo das informações do grafo selecionado.
                i += 1
            else:
                break
    return graph_list


def inf_extract(graph_list, task_list, dep_list, task_pattern, dep_pattern):
    for i in graph_list:
        if len(task_pattern.findall(i)) == 1:
            task_list.append(task_pattern.findall(i)[0].split('TASK ')[1])  # Extrai as tasks existentes em inf.
        if len(dep_pattern.findall(i)) == 1:
            dep_list.append(
                dep_pattern.findall(i)[0].split('FROM ')[1].split('  TO  '))  # Extrai as dependências das tasks em inf.
    return task_list, dep_list


def dest_list(task_list, dep_list, mat_dep):
    for i in range(len(task_list)):
        for j in range(len(dep_list)):
            if task_list[i] == dep_list[j][0]:  # compara as tarefas ao índice de dependências para criar uma lista de destinatários, com base nas tarefas relacionadas.
                mat_dep[i].append(dep_list[j][1])  # indexa ao índice correspondente a tarefa, seus destinatários.
    return mat_dep


def recv_list(mat_dep_send, mat_dep_receive, task_list, graph_ind):
    for i in range(len(task_list)):
        for j in range(len(mat_dep_send)):
            for k in range(len(mat_dep_send[j])):
                if(task_list[i]==mat_dep_send[j][k]):
                    mat_dep_receive[i].append('t{}_{}'.format(graph_ind, j))
    return mat_dep_receive


def extract_ind(task_list, mat_dep, ind_list):
    for i in range(len(task_list)):
        ocorrencies = 0  # variável que conta o número de repetições de um elemento i de taskList na matriz de dependências.
        for j in range(len(mat_dep)):
            for k in range(len(mat_dep[j])):
                if task_list[i] == mat_dep[j][k]:  # compara os elementos de taskList com cada elemento da matriz.
                    ocorrencies += 1
        if ocorrencies == 0:
            ind_list.append(task_list[i])
    return ind_list


def output_matrix(mat_dep, tasks, arq):
    for i in range(len(mat_dep)):
        if len(mat_dep[i]) > 0:
            for j in range(len(mat_dep[i])):
                inf = '{}\t'.format(mat_dep[i][j])
                arq.write(inf)
            for z in range((len(tasks) - 1) - len(mat_dep[i])):
                inf = '0\t\t'
                arq.write(inf)
        else:
            for j in range(len(tasks) - 1):
                inf = '0\t\t'
                arq.write(inf)
        arq.write('\n')


def indexes_of(*args):
    if len(args)==1:
        indexes = []
        for i in range(len(args[0])):
            indexes.append(int(args[0][i].split('_')[1]))
        return indexes
    else:
        dep = []
        for i in range(len(args[1][args[0]])):
            dep.append(int((args[1][args[0]][i]).split('_')[1]))
        return dep