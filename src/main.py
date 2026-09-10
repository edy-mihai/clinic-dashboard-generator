import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import shutil
from transform import execute_pipeline

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

ui_font = ("Segoe UI", 20)
bold_font = ("Segoe UI", 20, "bold")
title_font = ("Segoe UI", 40, "bold")

root = ctk.CTk()
root.title("Dashboard Generator")
root.geometry("1280x720")
root.config(padx=20, pady=20)

ctk.CTkLabel(root, text="Clinic Dashboard Generator", font=title_font).pack(pady=(20, 50))

main_frame = ctk.CTkFrame(root)
main_frame.pack(expand=False)

inner_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
inner_frame.pack(padx=40, pady=40)

curr_path_var = ctk.StringVar()
prev_path_var = ctk.StringVar()
last_path_var = ctk.StringVar()

curr_name_var = ctk.StringVar()
prev_name_var = ctk.StringVar()
last_name_var = ctk.StringVar()

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

    if not os.path.exists("data/output/"):
        os.makedirs("data/output/")
    
    execute_pipeline(c_path, p_path, l_path)

    os.startfile(os.path.abspath("data/output/Dashboard_Generated.xlsx"))

    download_btn.grid(row=5, column=0, columnspan=3, pady=10, ipadx=5, ipady=5)

def save_dashboard():
    file_destination = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])

    if file_destination:
        shutil.copy("data/output/Dashboard_Generated.xlsx", file_destination)
        messagebox.showinfo("Success", "Dashboard saved successfully!")

ctk.CTkLabel(inner_frame, text="Current Month Data:", font=bold_font).grid(row=0, column=0, sticky="w", pady=10)
ctk.CTkButton(inner_frame, text="Browse", command=lambda: select_file(curr_path_var, curr_name_var), font=bold_font).grid(row=0, column=1, padx=20)
ctk.CTkLabel(inner_frame, textvariable=curr_name_var, text_color="gray", font=bold_font).grid(row=0, column=2, sticky="w")


ctk.CTkLabel(inner_frame, text="Previous Month Data:", font=bold_font).grid(row=1, column=0, sticky="w", pady=10)
ctk.CTkButton(inner_frame, text="Browse", command=lambda: select_file(prev_path_var, prev_name_var), font=bold_font).grid(row=1, column=1, padx=20)
ctk.CTkLabel(inner_frame, textvariable=prev_name_var, text_color="gray", font=bold_font).grid(row=1, column=2, sticky="w")

ctk.CTkLabel(inner_frame, text="Last Year Month Data:", font=bold_font).grid(row=2, column=0, sticky="w", pady=10)
ctk.CTkButton(inner_frame, text="Browse", command=lambda: select_file(last_path_var, last_name_var), font=bold_font).grid(row=2, column=1, padx=20)
ctk.CTkLabel(inner_frame, textvariable=last_name_var, text_color="gray", font=bold_font).grid(row=2, column=2, sticky="w")

ctk.CTkLabel(inner_frame, text="").grid(row=3, column=0, pady=10)

ctk.CTkButton(inner_frame, text="Generate Dashboard", command=run_generator, fg_color="green", text_color="white", font=bold_font).grid(row=4, column=0, columnspan=3, pady=20, ipadx=10, ipady=5)

download_btn = ctk.CTkButton(inner_frame, text="Save Dashboard As...", command=save_dashboard, font=("Segoe UI", 13, "bold"))

root.mainloop()

# EDGE CASES:
# - the generated excel file is already open and gives a permission error
# - after selecting a different file in one of the 3 categories, the save as button should disappear until a new file with the new inputs is generated

# change browse buttons to small upload ones:

#                   /\
#                |  ||  |
#                |  ||  |
#                |______|        