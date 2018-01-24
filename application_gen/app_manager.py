from application_gen import node_create
import os,errno


def create_versions(ind_index,mat_dep_send,mat_dep_receive, local,i):

    try:
        os.makedirs(local)
        new_local = os.path.dirname('{}/app{}_0/'.format(local, i))
        os.makedirs(new_local)

        node_create.ind_nodes(ind_index, mat_dep_send, new_local)
        node_create.dep_nodes(mat_dep_send, mat_dep_receive, ind_index, new_local)
    except OSError as e:
        new_local = os.path.dirname('{}/app{}_0/'.format(local, i))
        node_create.ind_nodes(ind_index, mat_dep_send, new_local)
        node_create.dep_nodes(mat_dep_send, mat_dep_receive, ind_index, new_local)
        if e.errno != errno.EEXIST:
            raise
