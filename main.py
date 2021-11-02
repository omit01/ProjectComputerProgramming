def arrival_service_uniform(N, Arrival, Service):
    arrivalTime = []
    serviceTime = []
    for x in range(N):
        arrivalTime.append(1 / Arrival)
        serviceTime.append(1 / Service)
    restult = (arrivalTime, serviceTime)
    return restult

print(arrival_service_uniform(3, 4, 2))

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

print(arrival_service_exponential(2, 4, 2))

def Total_system_time(arrivaltimes, service_finish):
    waiting_time = []
    for x in range(len(arrivaltimes)):
        waiting_time.append(service_finish[x] - arrivaltimes[x])
    return (waiting_time, sum(waiting_time))

