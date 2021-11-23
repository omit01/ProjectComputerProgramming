#2022847 Phil Chiang
#2039152 Armin Ebrahimihardoroodi
#2087505 Timo Klabbers
#2036313 Dahli Koskamp
#2025574 Madelieve Pigmans

def arrival_service_uniform(N, Arrival, Service):
    data = [1]*N
    arrival_time = [1/Arrival for n in data]
    service_time = [1/Service for n in data]
    result = (arrival_time, service_time)
    return result


def calculate_arrival_service_per_C(arrivalrates, servicerates):
    last_arrival = 0
    last_service_start = 0
    last_service_end = 0

    arrival_times = []
    service_start = []
    service_finish = []

    for n in range(len(arrivalrates)):
        arrival_time = arrivalrates[n] + last_arrival
        last_arrival = arrival_time
        arrival_times.append(arrival_time)
        if last_service_end <= last_arrival:
            last_service_start = last_arrival
        else:
            last_service_start = last_service_end
        last_service_end = last_service_start + servicerates[n]
        service_start.append(last_service_start)
        service_finish.append(last_service_end)
    return (arrival_times, service_start, service_finish)


def arrival_service_exponential(N, Arrival, Service):
    import numpy as np
    np.random.seed(1)
    arrival_time = []
    service_time = []
    for x in range(N):
        arrival_time.append(np.random.exponential(1 / Arrival))
        service_time.append(np.random.exponential(1 / Service))
    restult = (arrival_time, service_time)
    return restult


def Total_system_time(arrivaltimes, service_finish):
    waiting_time = []
    for x in range(len(arrivaltimes)):
        waiting_time.append(service_finish[x] - arrivaltimes[x])
    return (waiting_time, sum(waiting_time))


def Total_queue_time(arrivaltimes, service_start):
    queue_time = []
    for n in range(len(arrivaltimes)):
        queue_time.append(service_start[n] - arrivaltimes[n])
    return queue_time, sum(queue_time)


def Total_system_time_CSV(file):
    import csv
    from pandas import pandas as pd

    tableDF = r"File1.csv"
    tableDF=pd.read_csv("File1.csv", header=0)

    waiting_time=[]
    for index, row in tableDF.iterrows():
        waiting_time.append(row[1] - row[0])
    return(waiting_time, sum(waiting_time))
    


def Queue_length_someone_joins(arrivaltimes, service_finish):
    result = []
    for n in range(len(arrivaltimes)):
        result.append(n - sum(f < arrivaltimes[n] for f in service_finish))
    return result


def Queueremains (queuelength, C, Q):
    return Q * sum(n > Q for n in queuelength)


def QueueLeaves(arrivalrates, servicerates, C, Q):
    import numpy as np
    arrival_times = np.cumsum(np.array(arrivalrates))
    bounced_c = 0
    queue = []
    c_in_queue = []
    last_finish_time = 0

    for n in range(len(arrivalrates)):
        c_in_queue.append[len(queue)] #Error: Object is not subscriptable
        if arrival_times[n] < last_finish_time:
            if len(queue) >= Q:
                bounced_c += 1
                servicerates[n] = 0
            else:
                queue.append[n]
        
        while arrival_times[n] >= last_finish_time:
            if queue.clear:
                break
            else:
                removed = queue.pop(0)
                last_finish_time += servicerates[removed]
    return (c_in_queue, bounced_c, bounced_c * C)
