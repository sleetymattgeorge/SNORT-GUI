import os
import re
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from collections import Counter

# === Parsing Function ===
def parse_alerts(file_path):
    alert_data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        match = re.match(r'^(\d+/\d+-\d+:\d+:\d+\.\d+)\s+\[\*\*\]\s+\[(\d+):(\d+):(\d+)\]\s+(.*?)\s+\[\*\*\]\s+\[Priority: (\d+)\]\s+\{(.*?)\}\s+(.*?)\s+->\s+(.*?)$', line)
        if match:
            alert_data.append({
                'timestamp': match.group(1),
                'gid': match.group(2),
                'sid': match.group(3),
                'rev': match.group(4),
                'message': match.group(5),
                'priority': int(match.group(6)),
                'protocol': match.group(7),
                'src': match.group(8),
                'dst': match.group(9)
            })
    return alert_data

# === Filter Function ===
def filter_alerts(alerts, src_filter, dst_filter):
    return [a for a in alerts if
            (src_filter in a['src'] if src_filter else True) and
            (dst_filter in a['dst'] if dst_filter else True)]

# === CSV Export ===
def export_to_csv(alerts, output_path):
    with open(output_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=alerts[0].keys())
        writer.writeheader()
        writer.writerows(alerts)

# === Pie Chart ===
def show_protocol_pie(alerts, container):
    protocol_counts = Counter([a['protocol'] for a in alerts])
    fig, ax = plt.subplots()
    ax.pie(protocol_counts.values(), labels=protocol_counts.keys(), autopct='%1.1f%%')
    ax.set_title('Protocol Distribution')
    
    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

# === Main App ===
class SnortLogAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Snort Log Analyzer")
        self.root.geometry("1000x700")

        self.alerts = []
        self.filtered_alerts = []

        self.setup_widgets()

    def setup_widgets(self):
        # File and Filters Frame
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        tk.Button(top_frame, text="Load Log File", command=self.load_file).grid(row=0, column=0, padx=5)
        tk.Label(top_frame, text="Filter Src:").grid(row=0, column=1)
        self.src_filter_entry = tk.Entry(top_frame, width=15)
        self.src_filter_entry.grid(row=0, column=2, padx=5)

        tk.Label(top_frame, text="Filter Dst:").grid(row=0, column=3)
        self.dst_filter_entry = tk.Entry(top_frame, width=15)
        self.dst_filter_entry.grid(row=0, column=4, padx=5)

        tk.Button(top_frame, text="Apply Filters", command=self.apply_filters).grid(row=0, column=5, padx=5)
        tk.Button(top_frame, text="Export CSV", command=self.export_csv).grid(row=0, column=6, padx=5)
        tk.Button(top_frame, text="Show Pie Chart", command=self.show_pie).grid(row=0, column=7, padx=5)

        # Alerts Table
        self.tree = ttk.Treeview(self.root, columns=('timestamp', 'priority', 'protocol', 'src', 'dst', 'message'), show='headings')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(fill='both', expand=True, pady=10)

        # Pie chart container
        self.chart_frame = tk.Frame(self.root)
        self.chart_frame.pack(fill='both', expand=True)

    def load_file(self):
        path = filedialog.askopenfilename(title='Select Snort Log File')
        if not path:
            return
        try:
            self.alerts = parse_alerts(path)
            self.filtered_alerts = self.alerts.copy()
            self.update_table()
            messagebox.showinfo("Loaded", f"{len(self.alerts)} alerts loaded.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_table(self):
        self.tree.delete(*self.tree.get_children())
        for alert in self.filtered_alerts:
            self.tree.insert('', 'end', values=(alert['timestamp'], alert['priority'], alert['protocol'], alert['src'], alert['dst'], alert['message']))

    def apply_filters(self):
        src = self.src_filter_entry.get().strip()
        dst = self.dst_filter_entry.get().strip()
        self.filtered_alerts = filter_alerts(self.alerts, src, dst)
        self.update_table()

    def export_csv(self):
        if not self.filtered_alerts:
            messagebox.showwarning("No Data", "No filtered data to export.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if path:
            export_to_csv(self.filtered_alerts, path)
            messagebox.showinfo("Exported", f"Data exported to {path}")

    def show_pie(self):
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
        show_protocol_pie(self.filtered_alerts, self.chart_frame)

# === Main Execution ===
if __name__ == '__main__':
    root = tk.Tk()
    app = SnortLogAnalyzer(root)
    root.mainloop()
