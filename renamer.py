import tkinter.filedialog as filedialog
import tkinter as tk
from tkinter import ttk
import sv_ttk

# Initialize root window
root = tk.Tk()
root.title("Mass Renamer Tool")
root.resizable(False, False)

#Initialize frames
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

#Configure widgets

#Directory section
dir_label = ttk.Label(frame, text="Directory:")
dir_label.grid(row=0, column=0, sticky="w", padx=5, pady=(5, 0))

dir_entry = ttk.Entry(frame)
dir_entry.grid(row=1, column=0, padx=5, pady=5)

dir_btn = ttk.Button(frame, text="Browse")
dir_btn.grid(row=1, column=1, sticky="w", padx=5, pady=5)

#Sorting section
sort_frame = ttk.Frame(frame)
sort_frame.grid(row=2, column=0, sticky="w", padx=5, pady=(15, 5))

sort_label = ttk.Label(sort_frame, text="Sort by:")
sort_label.grid(row=0, column=0, sticky="w")

sort_dropdown = ttk.Combobox(sort_frame, state="readonly", values=["Name", "Date", "Size"], width=5)
sort_dropdown.set("Name") #Selected by default
sort_dropdown.grid(row=0, column=1, sticky="w", padx=5)

#Format section
format_frame = ttk.Frame(frame)
format_frame.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=(15, 5))

format_label1 = ttk.Label(format_frame, text="Set the naming format to follow:")
format_label2 = ttk.Label(format_frame, text="(Place %xx% where you want sequence to start)", font=("Helvetica", 8, "italic"))
format_label1.grid(row=0, column=0, sticky="w")
format_label2.grid(row=1, column=0, sticky="w")

format_entry = ttk.Entry(format_frame)
format_entry.grid(row=2, column=0, sticky="w", pady=(5, 0))

#Start sequence section
seq_label = ttk.Label(frame, text="Start of sequence:")
seq_label.grid(row=4, column=0, sticky="w", padx=5, pady=(15, 5))

seq_entry = ttk.Entry(frame)
seq_entry.grid(row=5, column=0, sticky="w", padx=5)

#Done button
done_frame = ttk.Frame(root)
done_frame.grid(row=1, column=0, pady=20)

done_btn = ttk.Button(done_frame, text="Done")
done_btn.grid(row=0, column=0)

# Set dark theme
sv_ttk.set_theme("dark")

#Keep root window open and listening for events
root.mainloop()