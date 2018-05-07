from application_gen import node_create as utils


class Simulator(object):
    tasks = []

    def __init__(self, tasks, time=100000, receive_mat=None, send_mat=None):
        self.tasks = tasks
        self.time = time
        self.depTable = []

        self.init_rules(len(tasks), receive_mat, send_mat)

    def init_rules(self, n_tasks, rcv_m, snd_m):
        for i in range(n_tasks):
            in_tasks = rcv_m[i]
            out_tasks = snd_m[i]

            while len(in_tasks) > 0:
                t_in, t_out = utils.rules_create(in_tasks, out_tasks)
                dep = tuple([i, t_in, t_out])
                self.depTable.append(dep)

                for t in t_in:
                    in_tasks.remove(t)
                for t in t_out:
                    out_tasks.remove(t)

    #def run_Simulation(self):
    #def run_Activity(self):