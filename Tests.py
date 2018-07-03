from os import walk
from application_simulator import Task, Simulator, Utils
from random import randint
'''

def main():
    times = [1000, 5000, 10000, 50000, 100000, 500000]

    for time in times:
        print('Processing traces for time: {}'.format(time))
        for i in range(32):
            Utils.acumulated_traffic('traces_{}/traces_{}_{}.txt'.format(time, time, i), time, i, 10)
            Utils.acumulated_traffic('traces_{}/traces_{}_{}.txt'.format(time, time, i), time, i, 20)
            print('Time:{} | {} of 32'.format(time, i+1))
'''


def main():
    '''
    f = []
    for (dirpath, dirnames, filenames) in walk('tgff_files'):
        f.extend(filenames)
        break
    print(f)
    '''
    tasks = []

    for i in range(5):
        if i == 0:
            tasks.append(Task.Task(i, True, 0))
            continue
        tasks.append(Task.Task(i, False, randint(1, 2)))

    for i in tasks:
        i.to_string()

    rec_mat = [[], ['t1_0'], ['t1_0'], ['t1_1', 't1_2'], ['t1_3']]
    sen_mat = [['t1_1', 't1_2'], ['t1_3'], ['t1_3'], ['t1_4'], []]

    test_sim = Simulator.Simulator(tasks=tasks, time=100, receive_mat=rec_mat, send_mat=sen_mat)

    test_sim.run_simulation('test_traces', 1)


if __name__ == '__main__':
    main()