#2022847 Phil Chiang
#2039152 Armin Ebrahimihardoroodi
#2087505 Timo Klabbers
#2036313 Dahli Koskamp
#2025574 Madelieve Pigmans

def arrival_service_uniform(N, Arrival, Service):
    return ([1/Arrival for n in [1]*N], [1/Service for n in [1]*N])

#print(str(arrival_service_uniform(3, 4, 2)) == str(([0.25, 0.25, 0.25], [0.5, 0.5, 0.5]))) # if true 1 points 

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

#print(str(calculate_arrival_service_per_C([0.25, 0.25, 0.25], [0.5, 0.5, 0.5]))==str(([0.25, 0.5, 0.75], [0.25, 0.75, 1.25], [0.75, 1.25, 1.75]))) # 3 points if true

def arrival_service_exponential(N, Arrival, Service):
    import numpy as np
    np.random.seed(1)
    arrival_time = []
    service_time = []
    for x in range(N):
        arrival_time.append(np.random.exponential(1 / Arrival))
        service_time.append(np.random.exponential(1 / Service))
    return (arrival_time, service_time)

#print(str(arrival_service_exponential(2, 4, 2)) == str(([0.13490145931479636, 2.859533966077148e-05], [0.6370626265066521, 0.1800063774269595]))) #1 points if true 

def Total_system_time(arrivaltimes, service_finish):
    waiting_time = []
    for x in range(len(arrivaltimes)):
        waiting_time.append(service_finish[x] - arrivaltimes[x])
    return (waiting_time, sum(waiting_time))

#print(str(Total_system_time([0.25, 0.33, 0.59], [0.49, 0.53, 1.25]))==str(([0.24, 0.2, 0.66], 1.1))) # if true 1 point

def Total_queue_time(arrivaltimes, service_start):
    queue_time = []
    for n in range(len(arrivaltimes)):
        queue_time.append(service_start[n] - arrivaltimes[n])
    return (queue_time, sum(queue_time))

#print(str(Total_queue_time([0.25, 0.5, 0.75, 1.0, 1.25], [0.25, 0.5833333333333333, 0.9166666666666665, 1.2499999999999998, 1.583333333333333]))==str(([0.0, 0.08333333333333326, 0.16666666666666652, 0.24999999999999978, 0.33333333333333304], 0.8333333333333326))) # if true 1 point

def Total_system_time_CSV(file):
    import csv
    from pandas import pandas as pd
    
    tableDF=pd.read_csv(file, header=0)

    waiting_time=[]
    for index, row in tableDF.iterrows():
        waiting_time.append(row[1] - row[0])
    return(waiting_time, sum(waiting_time))
    
#print(str(Total_system_time_CSV("File.csv")) == str(([0.04999999999999999, 0.08330000000000004, 0.16659999999999997, 0.09600000000000009, 0.33329999999999993], 0.7292000000000001))) # 5 points if true

def Queue_length_someone_joins(arrivaltimes, service_finish):
    result = []
    for n in range(len(arrivaltimes)):
        result.append(n - sum(f < arrivaltimes[n] for f in service_finish))
    return result

#print(str(Queue_length_someone_joins([0.25, 0.34, 0.39, 0.51, 0.59, 0.77], [0.31, 0.41, 1.2, 1.5, 1.6, 1.9]))==str([0, 0, 1, 1, 2, 3])) # if true 5 points

def Queueremains (queuelength, C, Q):
    bounced = sum(n > Q for n in queuelength)
    return (bounced, "$" + str(C * bounced))

#print(str(Queueremains([0, 1, 2, 3, 1, 1],50, 2))==str((1, '$50'))) # 3 points if true

def QueueLeaves(arrivalrates, servicerates, C, Q):
    import numpy as np
    arrival_times = np.cumsum(np.array(arrivalrates))

    c_in_queue = []
    end_time = 0
    start_service=0
    queue = []

    for n in range(len(arrivalrates)):
        if arrival_times[n] >= end_time:
            start_service = arrival_times[n]
        else:
            queue.append(n)
        if len(queue) > Q:
            servicerates[n] = 0
            queue.remove(n)
        c_in_queue.append(len(queue))
        end_time = start_service + servicerates[n]
    bounced = sum(service_time == 0 for service_time in servicerates)

    return (c_in_queue, bounced, str("$" + str(bounced * C)))

#print(str(QueueLeaves([0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 50, 2)) == str(([0, 1, 1, 2, 2, 2, 2], 1, '$50'))) # 5 points if true