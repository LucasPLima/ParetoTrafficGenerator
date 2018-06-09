from application_simulator import Task, Simulator, Utils
from random import randint


def main():
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

    test_sim = Simulator.Simulator(tasks=tasks, time= 100, receive_mat=rec_mat, send_mat=sen_mat)
    test_sim.run_simulation()
    Utils.acumulated_traffic('application_simulator/traces.txt', 20)


if __name__ == '__main__':
    main()