from tgff_op import tsk_analyze
from application_gen import createFile
import itertools
import random


def ind_nodes(ind_index, mat_dep):
    for i in ind_index:
        dep_index = tsk_analyze.dep_indexes(i, mat_dep)
        createFile.Envio(i, len(mat_dep[i]), dep_index)


def dep_nodes(mat_dep_send, mat_dep_receive):
    iterations = len(mat_dep_send)

    for i in range(iterations):
        in_n = mat_dep_receive[i]
        out_n = mat_dep_send[i]
        while len(in_n)>0:
            t_in, t_out = rules_create(in_n, out_n)
            print('Task{}'.format(i))
            for j in range(len(t_in)):
                print('Receive of {}'.format(t_in[j]))
                in_n.remove(t_in[j])
            for k in range(len(t_out)):
                print('Send to {}'.format(t_out[k]))
                out_n.remove(t_out[k])


def rules_create(n_in, m_out):
    combinations_in = []
    combinations_o = []

    for i in range(1, len(n_in) + 1):
        for combination in itertools.combinations(n_in, i):
            combinations_in.append(combination)

    for i in range(1, len(m_out) + 1):
        for combination in itertools.combinations(m_out, i):
            combinations_o.append(combination)

    if len(n_in) != 1:
        t_in = random.choice(combinations_in)
        while len(t_in) == len(n_in):
            t_in = random.choice(combinations_in)

        if len(m_out) > 1:
            t_out = random.choice(combinations_o)
            while len(t_out) == len(m_out):
                t_out = random.choice(combinations_o)
        elif len(m_out) == 1:
            t_in = combinations_in.pop()
            t_out = combinations_o.pop()
        else:
            t_out = ()

    else:
        t_in = combinations_in.pop()

        if len(m_out) == 0:
            t_out = ()
        else:
            t_out = combinations_o.pop()

    return t_in, t_out