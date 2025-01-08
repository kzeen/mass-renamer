import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sv_ttk #pip install sv_ttk

# User functions
def on_submit():
    user_dir = dir_entry.get()
    user_format = format_entry.get()
    if not validate_required_fields(user_dir, user_format):
        messagebox.showerror("Invalid Input", "Please fill out all required fields")
    else:
        pass

def validate_required_fields(dir_field, format_field):
    if dir_field and format_field:
        return True
    return False

def getDir():
    user_dir = tk.filedialog.askdirectory() # Open dialog box and get directory
    dir_entry.delete(0, tk.END) # Delete any previous text found in entry
    dir_entry.insert(0, user_dir) # Insert new selected directory in entry

# Initialize root window
root = tk.Tk()
root.title("Mass Renamer Tool")
root.resizable(False, False)

#Initialize frames
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

#Configure widgets

#Directory section
dir_label = ttk.Label(frame, text="Directory: *")
dir_label.grid(row=0, column=0, sticky="w", padx=5, pady=(5, 0))

dir_entry = ttk.Entry(frame)
dir_entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

dir_btn = ttk.Button(frame, text="Browse", command=getDir)
dir_btn.grid(row=1, column=1, sticky="w", padx=5, pady=5)

spacer = ttk.Frame(frame, width=300)
spacer.grid(row=2, column=0)

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

format_label1 = ttk.Label(format_frame, text="Set the naming format to follow: *")
format_label2 = ttk.Label(format_frame, text="(Place %xx% where you want sequence to start)", font=("Helvetica", 8, "italic"))
format_label1.grid(row=0, column=0, sticky="w")
format_label2.grid(row=1, column=0, sticky="w")

format_entry = ttk.Entry(format_frame)
format_entry.grid(row=2, column=0, sticky="w", pady=(5, 0))

#Start sequence section
seq_label1 = ttk.Label(frame, text="Start of sequence:")
seq_label2 = ttk.Label(frame, text="(Default is 01)", font=("Helvetica", 8, "italic"))
seq_label1.grid(row=4, column=0, sticky="w", padx=5, pady=(15, 0))
seq_label2.grid(row=5, column=0, sticky="w", padx=5, pady=(0, 5))

seq_entry = ttk.Entry(frame)
seq_entry.grid(row=6, column=0, sticky="w", padx=5)

#Done button
done_frame = ttk.Frame(root)
done_frame.grid(row=1, column=0, pady=(20, 5))

done_btn = ttk.Button(done_frame, text="Done", command=on_submit)
done_btn.grid(row=0, column=0)

#Required field
req_msg_frame = ttk.Frame(root)
req_msg_frame.grid(row=2, column=0, sticky="w", pady=(0, 15))

req_msg_label = ttk.Label(req_msg_frame, text="'*' designates required fields", font=("Helvetica", 8, "bold italic"))
req_msg_label.grid(row=0, column=0, sticky="w")

# Set dark theme
sv_ttk.set_theme("dark")

#Keep root window open and listening for events
root.mainloop()