import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sv_ttk #pip install sv_ttk
import os

# Private functions
def accessFiles(path_to_files, format):
    # Make sure directory is valid and path exists
    if path_exists(path_to_files):
        # Get all files in directory and place them in list "files"
        files = os.listdir(path_to_files)

        # Sort the files alphabetically
        sorted_files = sorted(files)

        # Find the file type of the video files
        # We make 2 assumptions:
            # 1. All video files can either be mp4 or mkv only
            # 2. There will never be mp4 video files and mkv video files in the same directory
        file_type = ".mp4"
        for file in sorted_files:
            if file.endswith(".mkv"):
                file_type = ".mkv"
                break

        # Check if there are any subtitle files
        has_subtitles = False
        for file in sorted_files:
            if file.endswith(".srt"):
                has_subtitles = True
                break

        # Rename the video files
        renameFiles(path_to_files, format, sorted_files, file_type, False)

        # Show success message
        if has_subtitles:
            # Rename subtitle files first
            renameFiles(path_to_files, format, sorted_files, ".srt", True)
            messagebox.showinfo("Success", "All video and subtitle files have been renamed successfully")
        else:
            messagebox.showinfo("Success", "All video files have been renamed successfully")
    else:
        messagebox.showerror("Invalid path", "The directory path you provided is invalid")

def renameFiles(path_to_files, format, sorted_files, file_type, are_subtitles):
    start_sequence = 1

    for file in sorted_files:
        if file.endswith(file_type):
            # To have a consistent format, ex: E01, E02, ..., E10, etc.
            if start_sequence < 10:
                replace_with = "0" + str(start_sequence)
            else:
                replace_with = str(start_sequence)
            
            try:
                # Renaming using absolute paths to be extra sure
                if not are_subtitles:
                    os.rename(path_to_files + "\\" + file, path_to_files + "\\" + format.replace("%xx%", replace_with) + file_type)
                else:
                    # Add .eng pre-extension as most subtitles are english in my case
                    os.rename(path_to_files + "\\" + file, path_to_files + "\\" + format.replace("%xx%", replace_with) + ".eng" + file_type)
                print("File renamed successfully: " + file) # For debugging
            except FileNotFoundError:
                messagebox.showerror("File Not Found", "The file does not exist")
                break
            except PermissionError:
                messagebox.showerror("Permission Error", "You do not have permission to rename this file")
                break
            except OSError as e:
                messagebox.showerror("OS Error", "An error occurred while renaming the file: " + str(e))
                break

            # Increment sequence by 1
            start_sequence += 1
        else:
            continue


# User functions
def on_submit():
    user_dir = dir_entry.get()
    user_format = format_entry.get()

    if not validate_required_fields(user_dir, user_format):
        messagebox.showerror("Invalid Input", "Please fill out all required fields")
    else:
        user_sort = sort_dropdown.get() # Redundant, remove next
        user_sequence = seq_entry.get() # Redundant, remove next

        accessFiles(user_dir, user_format)

def validate_required_fields(dir_field, format_field):
    if dir_field and format_field:
        return True
    return False

def path_exists(dir_path):
    if os.path.exists(dir_path):
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