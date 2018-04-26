from application_gen import node_create
from shutil import copy2
import os
import errno


def dir_creation(local, i, ind_index, mat_dep_send, files, f_version):
    for j in range(1, 33):
        try:
            o_version = os.path.dirname('{}/app{}_{}/'.format(local, i, j))
            os.makedirs(o_version)

        except OSError as e:
            o_version = os.path.dirname('{}/app{}_{}/'.format(local, i, j))
            if e.errno != errno.EEXIST:
                raise

        for k in files:
            if 'cfg' not in k:
                src = '{}/{}'.format(f_version, k)
                copy2(src, o_version)
        node_create.ind_nodes(ind_index, mat_dep_send, o_version)


def create_versions(ind_index, mat_dep_send, mat_dep_receive, local, i):
    try:
        os.makedirs(local)
        f_version = os.path.dirname('{}/app{}_0/'.format(local, i))
        os.makedirs(f_version)

    except OSError as er:
        f_version = os.path.dirname('{}/app{}_0/'.format(local, i))

        if er.errno != errno.EEXIST:
            raise

    node_create.ind_nodes(ind_index, mat_dep_send, f_version)
    node_create.dep_nodes(mat_dep_send, mat_dep_receive, ind_index, f_version)

    files = next(os.walk(f_version))[2]

    dir_creation(local, i, ind_index, mat_dep_send, files, f_version)

    os.rename('{}/app.cfg'.format(f_version), '{}/app.cfg'.format(local))


