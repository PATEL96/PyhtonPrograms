List = [(1,3),(2,4),(1,2),(4,4)]

def sjf(processes):
    n = len(processes)
    burst_time = [processes[i][1] for i in range(n)]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    completion_time = [0] * n
    remaining_time = burst_time.copy()
    current_time = 0
    
    while True:
        completed = True
        shortest_job = None
        shortest_job_index = None
        for i in range(n):
            if remaining_time[i] > 0 and (shortest_job is None or remaining_time[i] < shortest_job):
                completed = False
                shortest_job = remaining_time[i]
                shortest_job_index = i
        if completed:
            break
        waiting_time[shortest_job_index] = current_time - processes[shortest_job_index][0]
        total_waiting_time += waiting_time[shortest_job_index]
        current_time += burst_time[shortest_job_index]
        turnaround_time[shortest_job_index] = current_time - processes[shortest_job_index][0]
        total_turnaround_time += turnaround_time[shortest_job_index]
        completion_time[shortest_job_index] = current_time
        remaining_time[shortest_job_index] = 0
    
    return(waiting_time, turnaround_time, (total_waiting_time/n), (total_turnaround_time/n));

# List = [(0,2),(1,2),(5,3),(6,4)]

def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0
    
    for i in range(n):
        if current_time < processes[i][0]:
            current_time = processes[i][0]
        waiting_time[i] = current_time - processes[i][0]
        
        total_waiting_time += waiting_time[i]
        current_time += processes[i][1]
        turnaround_time[i] = current_time - processes[i][0]
        total_turnaround_time += turnaround_time[i]
        
    return(waiting_time, turnaround_time, total_waiting_time, total_turnaround_time);

print(sjf(List))
# sjf(List) 