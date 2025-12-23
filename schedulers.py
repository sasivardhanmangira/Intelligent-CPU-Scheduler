from process import Process


def fcfs_scheduler(processes):
    """First Come First Serve scheduling algorithm"""
    time = 0
    gantt = []
    processes.sort(key=lambda p: p.arrival_time)

    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time

        p.start_time = time
        time += p.burst_time
        p.completion_time = time

        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        gantt.append((p.pid, p.start_time, p.completion_time))

    return gantt


def intelligent_scheduler(processes):
    """
    Intelligent scheduling algorithm based on priority, burst time, and waiting time
    Score formula: (2 * priority) + (3 / burst_time) + waiting_time
    """
    time = 0
    completed = 0
    gantt = []
    ready = []

    while completed < len(processes):
        # Add arrived processes to ready queue
        for p in processes:
            if p.arrival_time <= time and p.remaining_time > 0 and p not in ready:
                ready.append(p)

        if not ready:
            time += 1
            continue

        # Calculate scores for all ready processes
        scores = {}
        for p in ready:
            wait = time - p.arrival_time
            score = (2 * p.priority) + (3 / p.burst_time) + wait
            scores[p] = score

        # Select process with highest score
        current = max(scores, key=scores.get)

        if current.start_time is None:
            current.start_time = time

        time += current.remaining_time
        current.remaining_time = 0
        current.completion_time = time

        current.turnaround_time = current.completion_time - current.arrival_time
        current.waiting_time = current.turnaround_time - current.burst_time

        gantt.append((current.pid, current.start_time, current.completion_time))

        ready.remove(current)
        completed += 1

    return gantt


def average_metrics(processes):
    """Calculate average waiting time and turnaround time"""
    avg_wt = sum(p.waiting_time for p in processes) / len(processes)
    avg_tat = sum(p.turnaround_time for p in processes) / len(processes)

    return avg_wt, avg_tat
