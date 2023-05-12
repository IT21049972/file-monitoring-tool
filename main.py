import ttkbootstrap as tb
from tkinter import filedialog, messagebox
import os
import hashlib
import time

root = tb.Window(themename="superhero")
root.title("Integrity Checker")

mydir =''

def calculate_file_hash(directory, filepath):
    try:
        with open(os.path.join(directory, filepath), 'rb') as fh:
            hasher = hashlib.sha512()
            hasher.update(fh.read())
            hash_value = hasher.hexdigest()
        return hash_value
    except PermissionError:
            print(f"Error: Permission denied for file {filepath}")
            return None


def addPath():
    global mydir
    mydir = filedialog.askdirectory()
    with open('dir_selection.txt', 'w') as f:
        f.write(mydir)
   # print(mydir)
    files = os.listdir(mydir)

    baseline_file = 'baseline.txt'
    if os.path.exists(baseline_file):
        os.remove(baseline_file)

    with open(baseline_file, 'a') as f:
        for file in files:
            hash_value = calculate_file_hash(mydir, file)
            if hash_value:
                f.write(f"{file}|{hash_value}\n")
            else:
                f.write(f"{file}|ERROR\n")
            #print(hash_value)


def monitor():
    try:
        root.iconify()
        file_hash_dict = {}
        # Load file|hash from baseline.txt and store them in a dictionary
        with open('baseline.txt', 'r') as f:
            file_paths_and_hashes = f.readlines()

        for f in file_paths_and_hashes:
            file_path, file_hash = f.strip().split('|')
            file_hash_dict[file_path] = file_hash

        while True:
            time.sleep(1)
            files = os.listdir(mydir)
            for file in files:
                hash_value = calculate_file_hash(mydir, file)
                file_path = os.path.join(mydir, file)
                if hash_value not in file_hash_dict.values():
                    print(f"{file_path} file created or edited ")

            for key in file_hash_dict.keys():
                if key not in files:
                    print(f"{key} has been deleted!")

            #file_path = os.path.join(mydir, file)
                #baseline_file_still_exists = file_path.exists(key)
                #if key not in baseline_file_still_exists:












    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Select a folder then begin monitoring ")


def firstScreen():
    root.geometry("300x200")
    btn = tb.Button(root,bootstyle="success", text="Add new Path", width=20, command=addPath)
    btn.pack(pady=20)

    btn = tb.Button(root,bootstyle="success", text="Begin Monitoring", width=20, command=monitor)
    btn.pack(pady=10)


firstScreen()

root.mainloop()