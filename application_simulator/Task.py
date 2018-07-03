from random import choice
from string import ascii_letters
from application_gen import paretoGen


class Task(object):

    def __init__(self, task_n, independent=False, p_time=0):
        self.task_n = task_n
        self.independent = independent
        self.p_time = p_time
        self.packets_to_process = []
        self.inBuffer = []
        self.outBuffer = []
        self.paretos = []
        self.pareto_periods = []

    def is_empty(self, buffer):
        if len(buffer) != 0:
            return False
        return True

    def generate_paretos(self, receivers, simulation_time):
        self.paretos = []
        self.pareto_periods = []
        for i in range(receivers):
            self.paretos.append(list(paretoGen.paretoCalculate(simulation_time)))
            self.pareto_periods.append([None, None])
        for i in range(len(self.paretos)):
            self.start_periods(self.paretos[i], self.pareto_periods[i])
    #TODO
    def fill_buffer(self, destination_task):
        package = list([])
        package.append(self.task_n)
        package.append(destination_task)
        package.append(self.random_char(9))
        self.outBuffer.append(package)
    #TODO
    def send_packets(self, tasks):
        traces = []
        trace = []
        while not self.is_empty(self.outBuffer):
            s = self.outBuffer.pop()
            trace.append(s[1])
            for i in tasks:
                if i.task_n == s[1]:
                    trace.append(s[0])
                    i.inBuffer.append(s)
                    traces.append(trace)
                    trace = []
        return traces
    #TODO
    def process_packets(self):
        processed_packets=[]
        for refference in self.packets_to_process:
            if refference[1] > 0:
                refference[1] -= 1
                if refference[1] == 0:
                    processed_packets.append(refference)
        for refference in processed_packets:
            if refference in self.packets_to_process:
                self.packets_to_process.remove(refference)
                self.fill_buffer(refference[0])

    def pareto_on_periods(self, pareto):
        for i in range(len(pareto[0])):
            yield pareto[0][i]

    def pareto_off_periods(self, pareto):
        for i in range(len(pareto[1])):
            yield pareto[1][i]

    def start_periods(self, pareto, pareto_periods):
        pareto_periods[0] = self.pareto_on_periods(pareto)
        pareto_periods[1] = self.pareto_off_periods(pareto)

    def random_char(self, y):
        return ''.join(choice(ascii_letters) for x in range(y))

    def to_string(self):
        print('Task {}:\n\tIndependent? {}\n\tProcess time = {}'.format(self.task_n, self.independent, self.p_time))
