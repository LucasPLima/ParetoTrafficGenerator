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
        self.init_rules(len(self.tasks), self.receive_mat, self.send_mat)

        while actual_time < self.time:
            actual_task = self.tasks[i]

            if not actual_task.self.independent:
                if actual_task.self.is_empty(actual_task.self.inBuffer):
                    if actual_task.self.is_empty(actual_task.self.outBuffer):
                        i = self.select_task(i)
                    else:
                        actual_task.self.send_packets(self.tasks)
                        i = self.select_task(i)
                else:
                    rule = self.find_rules(actual_task.self.inBuffer, self.filter_rules(i))
                    while len(rule) > 0:
                        for package in actual_task.self.inBuffer:
                            if package[0] in rule[1]:
                                actual_task.self.inBuffer.remove(package)
                        for receiver in rule[2]:
                            actual_task.self.fill_buffer(receiver)
                        rule = self.find_rules(actual_task.self.inBuffer, self.filter_rules(i))
                    actual_task.self.send_packets(self.tasks)
                    i = self.select_task(i)
            else:
                if actual_task.self.is_empty(actual_task.self.outBuffer):
                    #TODO
                    print()

    #def run_Activity(self):
    def select_task(self, index):
        if index < len(self.tasks)-1:
            return index+1
        return 0

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
