import tkinter as tk
from tkinter import messagebox
from process import Process
from schedulers import fcfs_scheduler, intelligent_scheduler, average_metrics
from visualization import show_gantt


class SchedulerUI:
    """GUI for the CPU Scheduler application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Intelligent CPU Scheduler")
        self.root.configure(bg="white")
        self.processes = []
        self.build_ui()

    def build_ui(self):
        """Build the user interface"""
        # Title
        tk.Label(
            self.root,
            text="Intelligent CPU Scheduler",
            font=("Segoe UI", 20, "bold"),
            bg="white",
            fg="black"
        ).pack(pady=20)

        # Input form
        form = tk.Frame(self.root, bg="white")
        form.pack()

        self.pid_entry = self.create_entry(form, "Process ID")
        self.arrival_entry = self.create_entry(form, "Arrival Time")
        self.burst_entry = self.create_entry(form, "Burst Time")
        self.priority_entry = self.create_entry(form, "Priority")

        # Add process button
        tk.Button(
            self.root,
            text="Add Process",
            command=self.add_process,
            bg="black",
            fg="white",
            width=20,
            font=("Segoe UI", 10)
        ).pack(pady=10)

        # Output display
        output_frame = tk.Frame(self.root, bg="white")
        output_frame.pack(pady=10)

        self.output = tk.Text(
            output_frame,
            height=14,
            width=80,
            bg="white",
            fg="black",
            font=("Consolas", 10),
            wrap="word",
            relief="solid",
            bd=1
        )
        self.output.pack(side="left")

        scrollbar = tk.Scrollbar(output_frame, command=self.output.yview)
        scrollbar.pack(side="right", fill="y")
        self.output.config(yscrollcommand=scrollbar.set)

        # Action buttons
        btn_frame = tk.Frame(self.root, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Run FCFS",
            command=self.run_fcfs,
            bg="black",
            fg="white",
            width=18,
            font=("Segoe UI", 10)
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame,
            text="Run Intelligent Scheduler",
            command=self.run_intelligent,
            bg="black",
            fg="white",
            width=25,
            font=("Segoe UI", 10)
        ).grid(row=0, column=1, padx=10)

        # Reset button
        tk.Button(
            self.root,
            text="Reset",
            command=self.reset,
            bg="white",
            fg="black",
            relief="solid",
            width=10,
            font=("Segoe UI", 10)
        ).pack(pady=10)

    def create_entry(self, parent, label):
        """Create a labeled entry field"""
        frame = tk.Frame(parent, bg="white")
        frame.pack(pady=4)
        tk.Label(
            frame, 
            text=label, 
            width=15, 
            anchor="w", 
            bg="white",
            font=("Segoe UI", 10)
        ).pack(side="left")
        entry = tk.Entry(frame, width=20, font=("Segoe UI", 10))
        entry.pack(side="left")
        return entry

    def add_process(self):
        """Add a new process to the list"""
        try:
            p = Process(
                self.pid_entry.get(),
                int(self.arrival_entry.get()),
                int(self.burst_entry.get()),
                int(self.priority_entry.get())
            )
        except ValueError:
            messagebox.showerror(
                "Invalid Input", 
                "Arrival, Burst and Priority must be integers"
            )
            return

        self.processes.append(p)
        self.output.insert(tk.END, f"✓ Process added: {p.pid} (A:{p.arrival_time}, B:{p.burst_time}, P:{p.priority})\n")
        
        # Clear input fields
        self.pid_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def run_fcfs(self):
        """Run FCFS scheduling algorithm"""
        if not self.processes:
            messagebox.showwarning("No Processes", "Please add processes first!")
            return
            
        proc_copy = [
            Process(p.pid, p.arrival_time, p.burst_time, p.priority) 
            for p in self.processes
        ]
        gantt = fcfs_scheduler(proc_copy)
        avg_wt, avg_tat = average_metrics(proc_copy)

        self.output.insert(tk.END, "\n" + "="*70 + "\n")
        self.output.insert(tk.END, "FCFS Results\n")
        self.output.insert(tk.END, "="*70 + "\n")
        self.output.insert(tk.END, f"Average Waiting Time: {avg_wt:.2f}\n")
        self.output.insert(tk.END, f"Average Turnaround Time: {avg_tat:.2f}\n")
        self.output.insert(tk.END, "="*70 + "\n")

        show_gantt(gantt, "FCFS Gantt Chart")

    def run_intelligent(self):
        """Run intelligent scheduling algorithm"""
        if not self.processes:
            messagebox.showwarning("No Processes", "Please add processes first!")
            return
            
        proc_copy = [
            Process(p.pid, p.arrival_time, p.burst_time, p.priority) 
            for p in self.processes
        ]
        gantt = intelligent_scheduler(proc_copy)
        avg_wt, avg_tat = average_metrics(proc_copy)

        self.output.insert(tk.END, "\n" + "="*70 + "\n")
        self.output.insert(tk.END, "Intelligent Scheduler Results\n")
        self.output.insert(tk.END, "="*70 + "\n")
        self.output.insert(tk.END, f"Average Waiting Time: {avg_wt:.2f}\n")
        self.output.insert(tk.END, f"Average Turnaround Time: {avg_tat:.2f}\n")
        self.output.insert(tk.END, "="*70 + "\n")

        show_gantt(gantt, "Intelligent Scheduler Gantt Chart")

    def reset(self):
        """Reset all processes and output"""
        self.processes.clear()
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "All processes cleared.\n")


def main():
    """Launch the application"""
    root = tk.Tk()
    app = SchedulerUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()