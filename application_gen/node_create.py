from tgff_op import tsk_analyze
from application_gen import createFile
import itertools
import random


def ind_nodes(ind_index, mat_dep, local):
    for i in ind_index:
        dep_index = tsk_analyze.indexes_of(i, mat_dep)
        createFile.Envio(i, len(mat_dep[i]), dep_index, local)


def dep_nodes(mat_dep_send, mat_dep_receive, ind_index, local):
    iterations = len(mat_dep_send)
    cfg = open('{}/app.cfg'.format(local), 'w')
    for i in range(iterations):
        in_n = mat_dep_receive[i]
        out_n = mat_dep_send[i]
        if i in ind_index:
            cfg.write('Independent: task{} \n'.format(i))
            cfg.write('Send to: ')
            for j in mat_dep_send[i]:
                cfg.write('{}\t'.format(j))
            cfg.write('\n')
            pass
        else:
            file = open('{}/task{}.c'.format(local, i), 'w')
            createFile.create_top(file, i)

            while len(in_n)>0:
                t_in, t_out = rules_create(in_n, out_n)
                cfg.write('task{}\n'.format(i))
                cfg.write('Receive of:')
                for j in t_in:
                    file.write('Receive(&msg,task{});\n'.format(tsk_analyze.indexes_of([j])[0]))
                    cfg.write('{}\t'.format(j))
                    in_n.remove(j)
                cfg.write('\n')
                cfg.write('Send to:')
                for k in t_out:
                    file.write('	for(t=0;t<1000;t++)\n')
                    file.write('	{\n')
                    file.write('	}\n')
                    file.write('	Send(&msg,task{});\n'.format(tsk_analyze.indexes_of([k])[0]))
                    cfg.write('{}\t'.format(k))
                    out_n.remove(k)
                cfg.write('\n')
            createFile.create_bottom(file, i)
            cfg.write('\n')
            file.close()
    cfg.close()


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
