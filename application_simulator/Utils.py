import os


def acumulated_traffic(file, time, n, period):
    traces = open(file, 'r')
    local = create_dirs('/home/lucas/accumulated_traffic_{}_{}/'.format(time,period))
    accumulated_traces = open('{}/accumulated_traffic_{}_{}_{}.txt'.format(local, time, period, n), 'w')

    limit = period
    packets = 0

    trace = traces.readline()

    while len(trace) > 0:
        timestamp = int(trace.split('\t')[0])
        if timestamp <= limit:
            packets += 1
            trace = traces.readline()
            if len(trace) == 0:
                accumulated_traces.write('{period}    {packets_send}\n'.format(period=limit, packets_send=packets))
        else:
            accumulated_traces.write('{period}    {packets_send}\n'.format(period=limit, packets_send=packets))
            limit += period
            packets = 1
            trace = traces.readline()

    accumulated_traces.close()
    traces.close()


def create_dirs(local):

    local = os.path.dirname(local)

    try:
        os.makedirs(local)
        return local

    except OSError:
        return local


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length  + '-' * (length - filled_length)
    print('\r{} |{}| {} {}'.format(prefix, bar, percent, suffix), end='\r')
