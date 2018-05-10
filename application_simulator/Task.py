from random import choice
from string import ascii_letters


class Task(object):

    def __init__(self, task_n, independent=False, latency=0):
        self.task_n = task_n
        self.independent = independent
        self.latency = latency
        self.inBuffer = []
        self.outBuffer = []

    def is_empty(buffer):
        if len(buffer) != 0:
            return False
        return True

    def fill_buffer(self, destination_task):
        package = list([None, None])
        package[0].append(destination_task)
        package[1].append(self.random_char(8))
        self.outBuffer.append(package)

    def send_packets(self, tasks):
        while not self.is_empty(self.outBuffer):
            s = self.outBuffer.pop()
            for i in tasks:
                if i.self.task_n == s[0]:
                    s[0] = self.task_n
                    i.self.inBuffer.append(s)

    def random_char(self, y):
        return ''.join(choice(ascii_letters) for x in range(y))

    def get_task_n(self):
        return self.task_n

    def get_in_buffer(self):
        return self.inBuffer

    def get_out_buffer(self):
        return self.outBuffer
