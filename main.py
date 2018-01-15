import re

from application_gen import createFile
from tgff_op import tsk_analyze


def main():
    x = (int(input('Select the graph number:')))
    tgff = open("tgff_files/creds1.tgff", "r")
    tgff_n = tgff.readlines()
    send_matrix = open('outputMatrixes/SendMatrixGraph{}'.format(x), 'w')
    receive_matrix = open('outputMatrixes/ReceiveMatrixGraph{}'.format(x), 'w')
    inf = []  # Lista que irá armazenar as informações do grafo selecionado.
    tasks, ind_tasks= [], []  # tasks:lista que irá armazenar o número de tasks encontradas em inf[]|indTasks = lista de tasks independentes.|
    ind_index, dep_index= [],[] #indIndex=Vetor que armazena os índices de tasks independentes. | #depIndex=Vetor que armazena os índices de tasks dependentes
    dep = []  # Lista de dependências de tasks.

    t = re.compile('TASK t\d+_\d+')  # Operador de expressões regulares usado para encontrar as tasks.
    d = re.compile('FROM t\d+_\d+  TO  t\d+_\d+')  # Operador de expressões regulares usado para encontrar dependências.

    for i in range(len(tgff_n)):
        tgff_n[i] = tgff_n[i].splitlines()[0]  # Operação de retirada de \n das linhas do arquivo.

    inf = tsk_analyze.graph_select(tgff_n, inf, x)
    tasks, dep = tsk_analyze.inf_extract(inf, tasks, dep, t, d)
    mat_dep_send, mat_dep_receive = tsk_analyze.matrix_create(len(tasks)), tsk_analyze.matrix_create(len(tasks))
    mat_dep_send = tsk_analyze.dest_list(tasks, dep, mat_dep_send)
    mat_dep_receive = tsk_analyze.recv_list(mat_dep_send,mat_dep_receive,tasks,x)
    ind_tasks = tsk_analyze.extract_ind(tasks, mat_dep_send, ind_tasks)
    ind_index = tsk_analyze.ind_indexes(ind_tasks)

    tsk_analyze.output_matrix(mat_dep_send, tasks, send_matrix)
    tsk_analyze.output_matrix(mat_dep_receive, tasks, receive_matrix)

    ##Pareto.paretoCalculate()

    for i in ind_index:
        dep_index = tsk_analyze.dep_indexes(i, mat_dep_send)
        createFile.Envio(i, len(mat_dep_send[i]), dep_index)

    print('Indexes of IT:{}'.format(ind_index))
    print('Number of dependent tasks of task{}: {}'.format(ind_index[0], len(mat_dep_send[ind_index[0]])))
    print('Dependents of task{}:{}'.format(ind_index[0], dep_index))
    print(tasks)

    tgff.close()
    send_matrix.close()
    receive_matrix.close()


if __name__ == '__main__':
    main()