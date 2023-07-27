import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a Label widget to display the time
clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
clock_label.pack(padx=20, pady=20)

# Start updating the time
update_time()

# Run the main event loop
root.mainloop()
