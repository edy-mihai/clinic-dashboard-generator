import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
from transform import execute_pipeline

root = tk.Tk()
root.title("Dashboard Generator")
root.geometry("600x450")
root.config(padx=20, pady=20)

main_frame = tk.Frame(root)
main_frame.pack(expand=True)


curr_path_var = tk.StringVar()
prev_path_var = tk.StringVar()
last_path_var = tk.StringVar()

curr_name_var = tk.StringVar()
prev_name_var = tk.StringVar()
last_name_var = tk.StringVar()

def select_file(path_var, name_var):
    filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

    if filepath:
        path_var.set(filepath)
        file_name = os.path.basename(filepath)
        name_var.set(file_name)

def run_generator():
    c_path = curr_path_var.get()
    p_path = prev_path_var.get()
    l_path = last_path_var.get()

    if not c_path or not p_path or not l_path:
        messagebox.showerror("Error", "Please select all three files!")
        return
    
    execute_pipeline(c_path, p_path, l_path)

    os.startfile(os.path.abspath("data/output/Dashboard_Generated.xlsx"))

    download_btn.grid(row=5, column=0, columnspan=3, pady=10)

def save_dashboard():
    file_destination = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])

    if file_destination:
        shutil.copy("data/output/Dashboard_Generated.xlsx", file_destination)
        messagebox.showinfo("Success", "Dashboard saved successfully!")

tk.Label(main_frame, text="Current Month Data:").grid(row=0, column=0, sticky="w", pady=10)
tk.Button(main_frame, text="Browse", command=lambda: select_file(curr_path_var, curr_name_var)).grid(row=0, column=1, padx=10)
tk.Label(main_frame, textvariable=curr_name_var, fg="gray").grid(row=0, column=2, sticky="w")


tk.Label(main_frame, text="Previous Month Data:").grid(row=1, column=0, sticky="w", pady=10)
tk.Button(main_frame, text="Browse", command=lambda: select_file(prev_path_var, prev_name_var)).grid(row=1, column=1, padx=10)
tk.Label(main_frame, textvariable=prev_name_var, fg="gray").grid(row=1, column=2, sticky="w")

tk.Label(main_frame, text="Last Year Data:").grid(row=2, column=0, sticky="w", pady=10)
tk.Button(main_frame, text="Browse", command=lambda: select_file(last_path_var, last_name_var)).grid(row=2, column=1, padx=10)
tk.Label(main_frame, textvariable=last_name_var, fg="gray").grid(row=2, column=2, sticky="w")

tk.Label(main_frame, text="").grid(row=3, column=0, pady=10)

tk.Button(main_frame, text="Generate Dashboard", command=run_generator, bg="green", fg="white", font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=3, pady=20, ipadx=10, ipady=5)

download_btn = tk.Button(main_frame, text="Save Dashboard As...", command=save_dashboard)

root.mainloop()