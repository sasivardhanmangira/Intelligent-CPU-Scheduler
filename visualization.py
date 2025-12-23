import matplotlib.pyplot as plt


def show_gantt(gantt, title):
    """Display Gantt chart for process scheduling"""
    plt.figure(figsize=(10, 4))
    
    colors = plt.cm.Set3.colors
    color_map = {}
    
    for idx, (pid, start, end) in enumerate(gantt):
        if pid not in color_map:
            color_map[pid] = colors[len(color_map) % len(colors)]
        
        plt.barh(0, end - start, left=start, height=0.5, 
                color=color_map[pid], edgecolor='black', linewidth=1)
        
        # Add process ID label in the center of the bar
        plt.text((start + end) / 2, 0, pid, 
                ha='center', va='center', fontweight='bold')
    
    plt.xlabel("Time", fontsize=12)
    plt.ylabel("CPU", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.yticks([])
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.show()