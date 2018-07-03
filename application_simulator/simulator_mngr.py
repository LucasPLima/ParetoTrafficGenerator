import application_simulator.Simulator as Sm
import application_simulator.Task as Tsk
import application_simulator.Utils as Utls
from random import randint


def init_simulation(n_tasks , independent_tasks, receive_mat, send_mat):
    tasks = []

    for i in range(n_tasks):
        if i in independent_tasks:
            tasks.append(Tsk.Task(i, True, randint(1, 3)))
            continue
        tasks.append(Tsk.Task(i, False, randint(1, 3)))

    for i in tasks:
        i.to_string()

    simulation = Sm.Simulator(tasks, time=0, receive_mat= receive_mat, send_mat=send_mat)
    #1000, 5000, 10000,50000,
    times = [100000, 500000]

    for time in times:
        simulation.time = time
        local = Utls.create_dirs('traces_{}/'.format(simulation.time))
        for i in range(33):
            simulation.run_simulation(local, i)

    for time in times:
        print('Processing traces for time: {}'.format(time))
        for i in range(32):
            Utls.acumulated_traffic('traces_{}/traces_{}_{}.txt'.format(time, time, i), time, i, 10)
            Utls.acumulated_traffic('traces_{}/traces_{}_{}.txt'.format(time, time, i), time, i, 20)
            print('Time:{} | {} of 32'.format(time, i + 1))

    print()
