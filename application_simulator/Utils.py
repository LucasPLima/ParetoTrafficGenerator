def acumulated_traffic(file, period):
    traces = open(file, 'r')
    accumulated_traces = open('/home/lucas/accumulated_traffic.txt', 'w')

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

