class Process:
    """Represents a process in the CPU scheduler"""
    
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival_time = arrival
        self.burst_time = burst
        self.priority = priority

        self.remaining_time = burst
        self.start_time = None
        self.completion_time = None
        self.waiting_time = 0
        self.turnaround_time = 0

    def __repr__(self):
        return f"Process(pid={self.pid}, arrival={self.arrival_time}, burst={self.burst_time})"