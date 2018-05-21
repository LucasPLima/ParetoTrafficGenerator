from random import choice
from string import ascii_letters
from application_gen import paretoGen


class Task(object):

    def __init__(self, task_n, independent=False, latency=0):
        self.task_n = task_n
        self.independent = independent
        self.latency = latency
        self.inBuffer = []
        self.outBuffer = []

        if self.independent:
            self.pareto = list(paretoGen.paretoCalculate())
            self.pareto_periods = [None, None]
            self.start_periods()

    def is_empty(self, buffer):
        if len(buffer) != 0:
            return False
        return True

    def fill_buffer(self, destination_task):
        package = list([None, None])
        package[0].append(destination_task)
        package[1].append(self.random_char(8))
        self.outBuffer.append(package)

    def send_packets(self, tasks):
        #TODO
        traces = []
        while not self.is_empty(self.outBuffer):
            s = self.outBuffer.pop()
            for i in tasks:
                if i.self.task_n == s[0]:
                    s[0] = self.task_n
                    i.self.inBuffer.append(s)

    def pareto_on_periods(self, pareto):
        for i in range(len(pareto[0])):
            yield self.pareto[0][i]

    def pareto_off_periods(self, pareto):
        for i in range(len(pareto[1])):
            yield self.pareto[1][i]

    def start_periods(self):
        self.pareto_periods[0] = self.pareto_on_periods(self.pareto)
        self.pareto_periods[1] = self.pareto_off_periods(self.pareto)

    def random_char(self, y):
        return ''.join(choice(ascii_letters) for x in range(y))

    def get_task_n(self):
        return self.task_n

    def get_in_buffer(self):
        return self.inBuffer

    def get_out_buffer(self):
        return self.outBuffer
