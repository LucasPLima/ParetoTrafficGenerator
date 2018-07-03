import re
import os
from application_gen import node_create, app_manager
from tgff_op import tsk_analyze
from application_simulator import simulator_mngr as smm
import time


def main():
    graph = 1
    tgff = open("tgff_files/simple_9_2_g1.tgff", "r")
    tgff_n = tgff.readlines()
    send_matrix = open('outputMatrixes/SendMatrixGraph{}'.format(graph), 'w')
    receive_matrix = open('outputMatrixes/ReceiveMatrixGraph{}'.format(graph), 'w')
    inf = []  # Lista que irá armazenar as informações do grafo selecionado.
    tasks, ind_tasks= [], []  # tasks:lista que irá armazenar o número de tasks encontradas em inf[]|indTasks = lista de tasks independentes.|
    dep = []  # Lista de dependências de tasks.

    t = re.compile('TASK t\d+_\d+')  # Operador de expressões regulares usado para encontrar as tasks.
    d = re.compile('FROM t\d+_\d+  TO  t\d+_\d+')  # Operador de expressões regulares usado para encontrar dependências.

    for i in range(len(tgff_n)):
        tgff_n[i] = tgff_n[i].splitlines()[0]  # Operação de retirada de \n das linhas do arquivo.

    inf = tsk_analyze.graph_select(tgff_n, inf, graph)
    tasks, dep = tsk_analyze.inf_extract(inf, tasks, dep, t, d)
    mat_dep_send, mat_dep_receive = tsk_analyze.matrix_create(len(tasks)), tsk_analyze.matrix_create(len(tasks))
    mat_dep_send = tsk_analyze.dest_list(tasks, dep, mat_dep_send)
    mat_dep_receive = tsk_analyze.recv_list(tasks, dep, mat_dep_receive)

    ind_tasks = tsk_analyze.extract_ind(tasks, mat_dep_send, ind_tasks)
    ind_index = tsk_analyze.indexes_of(ind_tasks)

    tsk_analyze.output_matrix(mat_dep_send, tasks, send_matrix)
    tsk_analyze.output_matrix(mat_dep_receive, tasks, receive_matrix)

    start_time = time.time()
    smm.init_simulation(len(tasks), ind_index, mat_dep_receive, mat_dep_send)
    #app_manager.create_versions(ind_index, mat_dep_send,mat_dep_receive, local, graph)

    print('Aplicação gerada.')
    tgff.close()
    send_matrix.close()
    receive_matrix.close()
    print('Time of processing:{} seconds'.format(round(time.time() - start_time)))


if __name__ == '__main__':
    main()