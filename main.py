def arrival_service_uniform(N, Arrival, Service):
    data = [1]*N
    arrival_time = [1/Arrival for n in data]
    service_time = [1/Service for n in data]
    result = (arrival_time, service_time)
    return result


def calculate_arrival_service_per_C(arrivalrates, servicerates):
    lastArrival = 0
    lastServiceStart = 0
    lastServiceEnd = 0

    arrivalTimes = []
    service_start = []
    service_finish = []

    for n in range(len(arrivalrates)):
        arrivalTime = arrivalrates[n] + lastArrival
        lastArrival = arrivalTime
        arrivalTimes.append(arrivalTime)
        if lastServiceEnd <= lastArrival:
            lastServiceStart = lastArrival
        else:
            lastServiceStart = lastServiceEnd
        lastServiceEnd = lastServiceStart + servicerates[n]
        service_start.append(lastServiceStart)
        service_finish.append(lastServiceEnd)
    return (arrivalTimes, service_start, service_finish)


def arrival_service_exponential(N, Arrival, Service):
    import numpy as np
    np.random.seed(1)
    arrivalTime = []
    serviceTime = []
    for x in range(N):
        arrivalTime.append(np.random.exponential(1 / Arrival))
        serviceTime.append(np.random.exponential(1 / Service))
    restult = (arrivalTime, serviceTime)
    return restult


def Total_system_time(arrivaltimes, service_finish):
    waiting_time = []
    for x in range(len(arrivaltimes)):
        waiting_time.append(service_finish[x] - arrivaltimes[x])
    return (waiting_time, sum(waiting_time))


def Total_queue_time(arrivaltimes, service_start):
    queue_time = []
    for n in range(len(arrivaltimes)):
        print(n)
        queue_time.append(service_start[n] - arrivaltimes[n])
    return queue_time, sum(queue_time)


def Total_system_time_CSV(file):
    from pandas import pandas as pd
    """Still some work to do..."""
    pass


def Queue_length_someone_joins(arrivaltimes, service_finish):
    result = []
    for n in range(len(arrivaltimes)):
        result.append(n - sum(f < arrivaltimes[n] for f in service_finish))
    return result


def Queueremains (queuelength, C, Q):
    return Q * sum(n > Q for n in queuelength)


def QueueLeaves(arrivalrates, servicerates, C, Q):
    """Still some work to do..."""
    pass