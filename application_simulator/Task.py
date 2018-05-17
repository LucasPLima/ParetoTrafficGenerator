from random import choice
from string import ascii_letters
from application_gen import paretoGen


class Task(object):

    def __init__(self, task_n, independent=False, latency=0):
        self.task_n = task_n
        self.independent = independent
        self.latency = latency
        self.pareto = []
        self.inBuffer = []
        self.outBuffer = []

        if self.independent:
            self.pareto = list(paretoGen.paretoCalculate())

    def is_empty(self, buffer):
        if len(buffer) != 0:
            return False
        return True

    def fill_buffer(self, destination_task):
        package = list([None, None])
        package[0].append(destination_task)
        package[1].append(self.random_char(8))
        self.outBuffer.append(package)
        return

    def send_packets(self, tasks):
        while not self.is_empty(self.outBuffer):
            s = self.outBuffer.pop()
            for i in tasks:
                if i.self.task_n == s[0]:
                    s[0] = self.task_n
                    i.self.inBuffer.append(s)
        return

    def pareto_periods(self):
        for i in range(len(self.pareto[0])):
            yield self.pareto[0][i], self.pareto[1][i]

    def random_char(self, y):
        return ''.join(choice(ascii_letters) for x in range(y))

    def get_task_n(self):
        return self.task_n

    def get_in_buffer(self):
        return self.inBuffer

    def get_out_buffer(self):
        return self.outBuffer
