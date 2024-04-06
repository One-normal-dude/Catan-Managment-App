import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import threading
import time

def show_loading_bar():
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading")
    loading_label = tk.Label(loading_window, text="Loading...")
    loading_label.pack()
    loading_bar = Progressbar(loading_window, mode='indeterminate')
    loading_bar.pack()
    loading_bar.start(100)
    loading_window.grab_set()  # Make the loading window modal
    loading_window.after(10000, loading_window.destroy)  # Close after 10 seconds
    loading_window.mainloop()

def analyze_number():
    try:
        number = int(entry.get())
        loading_thread = threading.Thread(target=show_loading_bar)
        loading_thread.start()

        if number % 2 == 0:
            result = f"{number} is an even number."
        else:
            result = f"{number} is an odd number."

        time.sleep(2)  # Simulate some processing time (faster)
        messagebox.showinfo("Analysis", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Number Analyzer")

# Create a label and entry for the number input
label = tk.Label(root, text="Enter a number:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to analyze the number
analyze_button = tk.Button(root, text="Analyze", command=analyze_number)
analyze_button.pack()

# Run the main event loop
root.mainloop()


