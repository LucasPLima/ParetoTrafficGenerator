from application_gen import node_create as utils
from tgff_op import tsk_analyze
from itertools import combinations


class Simulator(object):

    def __init__(self, tasks, time=100, receive_mat=None, send_mat=None):
        self.tasks = tasks
        self.time = time
        self.receive_mat = list(map(tsk_analyze.indexes_of, receive_mat))
        self.send_mat = list(map(tsk_analyze.indexes_of, send_mat))
        self.depTable = []
        self.control_periods = [0] * len(self.tasks)
        self.traces_file = None

        for task in self.tasks:
            if task.independent:
                self.control_periods[task.task_n] = [None, None]

    def run_simulation(self):
        actual_time = 1
        i = 0
        periods = [0, 0]
        self.init_rules(len(self.tasks), self.receive_mat, self.send_mat)
        self.traces_file = open('application_simulator/traces.txt', 'w')

        while actual_time <= self.time:
            actual_task = self.tasks[i]

            if not actual_task.independent:
                self.run_dependent_task(actual_task, actual_time)
                i = self.next_task(i)
            else:
                self.run_independent_task(actual_task, periods, actual_time)
                i = self.next_task(i)
            actual_time += 1
        self.traces_file.close()
        print('Simulation finished.')

    def init_rules(self, n_tasks, rcv_m, snd_m):
        for i in range(n_tasks):
            in_tasks = rcv_m[i][:]
            out_tasks = snd_m[i][:]

            while len(in_tasks) > 0 and len(out_tasks) > 0:
                t_in, t_out = utils.rules_create(in_tasks, out_tasks)
                dependencie = tuple([i, t_in, t_out])
                self.depTable.append(dependencie)

                for t in t_in:
                    in_tasks.remove(t)
                for t in t_out:
                    out_tasks.remove(t)

    def run_dependent_task(self, task, actual_time):
        if task.is_empty(task.inBuffer):
            if task.is_empty(task.outBuffer):
                return
            else:
                traces = task.self.send_packets(self.tasks)
                self.register_trace(traces, actual_time)
        else:
            rule = self.find_rules(task.inBuffer, self.filter_rules(task.task_n))
            while len(rule) > 0:
                #TODO
                in_packages = []
                for package in task.inBuffer:
                    if package[0] in rule[1]:
                        in_packages.append(package)

                for package in in_packages:
                    task.inBuffer.remove(package)

                for receiver in rule[2]:
                    task.fill_buffer(receiver)
                rule = self.find_rules(task.inBuffer, self.filter_rules(task.task_n))
            traces = task.send_packets(self.tasks)
            self.register_trace(traces, actual_time)

    def run_independent_task(self, task, periods, actual_time):
        self.verify_periods(task)
        if periods[0] < self.control_periods[task.task_n][0]:
            periods[0] += 1
            for receiver in self.send_mat[task.task_n]:
                task.fill_buffer(receiver)
            traces = task.send_packets(self.tasks)
            self.register_trace(traces, actual_time)
        elif periods[1] < self.control_periods[task.task_n][1]:
            periods[1] += 1
        else:
            periods[0] = 0
            periods[1] = 0
            self.change_periods(task)

    def register_trace(self, traces, actual_time):
        for trace in traces:
            trace.append(actual_time)
            trace.reverse()
            self.traces_file.write('{timestamp}\t{tx}\t{rx}\n'.format(timestamp=trace[0], tx=trace[1], rx=trace[2]))

    def verify_periods(self, task):
        if self.control_periods[task.task_n] == [None, None]:
            self.control_periods[task.task_n][0] = next(task.pareto_periods[0])
            self.control_periods[task.task_n][1] = next(task.pareto_periods[1])

    def change_periods(self, task):
        try:
            self.control_periods[task.task_n][0] = next(task.pareto_periods[0])
            self.control_periods[task.task_n][1] = next(task.pareto_periods[1])
        except StopIteration:
            task.start_periods()
            self.change_periods(task)

    def next_task(self, index):
        if index < len(self.tasks)-1:
            return index+1
        return 0

    def find_rules(self, in_buffer, rules):
        sources = []

        for package in in_buffer:
            sources.append(package[0])

        sources_cmb = self.create_combinations(sources)

        for subset in sources_cmb:
            for rule in rules:
                subset = tuple(sorted(subset))
                aux = tuple(sorted(rule[1]))
                if subset == aux:
                    return rule
        return []

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
