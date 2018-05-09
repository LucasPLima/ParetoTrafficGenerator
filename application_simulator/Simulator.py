from application_gen import node_create as utils
from tgff_op import tsk_analyze
from itertools import combinations


class Simulator(object):

    def __init__(self, tasks, time=100000, receive_mat=None, send_mat=None):
        self.tasks = tasks
        self.time = time
        self.receive_mat = list(map(tsk_analyze.indexes_of, receive_mat))
        self.send_mat = list(map(tsk_analyze.indexes_of, send_mat))
        self.depTable = []

        self.init_rules(len(tasks), self.receive_mat, self.send_mat)

    def init_rules(self, n_tasks, rcv_m, snd_m):
        for i in range(n_tasks):
            in_tasks = rcv_m[i]
            out_tasks = snd_m[i]

            while len(in_tasks) > 0 or len(out_tasks) > 0:
                t_in, t_out = utils.rules_create(in_tasks, out_tasks)
                dependencie = tuple([i, t_in, t_out])
                self.depTable.append(dependencie)

                for t in t_in:
                    in_tasks.remove(t)
                for t in t_out:
                    out_tasks.remove(t)

    def run_Simulation(self):
        actual_time = 0
        i = 0

        while actual_time < self.time:
            actual_task = self.tasks[i]

            if actual_task.self.independent:
                print()


    #def run_Activity(self):

    def find_rules(self, in_buffer, rules):
        sources = []

        for package in in_buffer:
            sources += package[0]

        sources_cmb = self.create_combinations(sources)

        for subset in sources_cmb:
            for rule in rules:
                subset = tuple(sorted(subset))
                rule[1] = tuple(sorted(rule[1]))
                if subset == rule[1]:
                    return rule
        return None

    def filter_rules(self, task_n):
        rules = []
        for dependencie in self.depTable:
            if task_n == dependencie[0]:
                rules.append(dependencie)
        return rules

    def create_combinations(self, elements):
        comb = []

        for i in range(1, len(elements) + 1):
            for combination in combinations(elements, i):
                comb.append(combination)

        return comb
