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
            t_in, t_out = rule_create(len(in_n), len(out_n))



def rule_create(n_in, m_out):
    in_l = list(range(0, n_in))
    o_l = list(range(0, m_out))
    combinations_in = []
    combinations_o = []

    for i in range(1, len(in_l) + 1):
        for combination in itertools.combinations(in_l, i):
            combinations_in.append(combination)

    for i in range(1, len(o_l) + 1):
        for combination in itertools.combinations(o_l, i):
            combinations_o.append(combination)

    if n_in != 1:
        t_in = random.choice(combinations_in)
        while len(t_in) == n_in:
            t_in = random.choice(combinations_in)

        if m_out > 1:
            t_out = random.choice(combinations_o)
            while len(t_out) == m_out:
                t_out = random.choice(combinations_o)
        elif m_out == 1:
            t_out = combinations_o.pop()
        else:
            t_out = ()

    else:
        t_in = combinations_in.pop()

        if m_out == 0:
            t_out = ()
        else:
            t_out = combinations_o.pop()

    return t_in, t_out