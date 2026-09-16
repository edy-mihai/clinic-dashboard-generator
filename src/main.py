import customtkinter as ctk
from customtkinter import CTk
from tkinter import filedialog, messagebox
import os
import shutil
from transform import execute_pipeline
from PIL import Image
import sys

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

ui_font = ("Segoe UI", 20)
bold_font = ("Segoe UI", 20, "bold")
title_font = ("Segoe UI", 40, "bold")

def get_asset_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = ctk.CTk()
root.update_idletasks()
root.title("Clinic Dashboard Generator")
root.iconbitmap(get_asset_path("assets/app_icon.ico"))

def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/2)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

root.geometry(CenterWindowToDisplay(root, 1200, 720, root._get_window_scaling()))

root.config(padx=20, pady=20)

ctk.CTkLabel(root, text="Clinic Dashboard Generator", font=title_font).pack(pady=(20, 50))

main_frame = ctk.CTkFrame(root)
main_frame.pack(expand=False)

inner_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
inner_frame.pack(padx=40, pady=40)

row0_frame = ctk.CTkFrame(inner_frame, fg_color="transparent")
row0_frame.pack(pady=10, fill="x")

row1_frame = ctk.CTkFrame(inner_frame, fg_color="transparent")
row1_frame.pack(pady=10, fill="x")

row2_frame = ctk.CTkFrame(inner_frame, fg_color="transparent")
row2_frame.pack(pady=10, fill="x")

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
        download_btn.pack_forget()

def run_generator():
    c_path = curr_path_var.get()
    p_path = prev_path_var.get()
    l_path = last_path_var.get()

    if not c_path or not p_path or not l_path:
        messagebox.showerror("Error", "Please select all three files!")
        return

    if not os.path.exists(get_output_path("data/output/")):
        os.makedirs(get_output_path("data/output/"))

    try:
        execute_pipeline(c_path, p_path, l_path, get_output_path("data/output/Dashboard_Generated.xlsx"), root)
        os.startfile(get_output_path("data/output/Dashboard_Generated.xlsx"))

    except PermissionError:
        messagebox.showerror("Error", "Please close the dashboard file before generating!")

    download_btn.pack(pady=10, ipadx=5, ipady=5)

def save_dashboard():
    file_destination = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])

    if file_destination:
        shutil.copy(get_output_path("data/output/Dashboard_Generated.xlsx"), file_destination)
        messagebox.showinfo("Success", "Dashboard saved successfully!")

def create_file_row(parent_frame, row_title, path_variable, name_variable):
    ctk.CTkLabel(parent_frame, text=row_title, font=bold_font, width=210, anchor="w").pack(side="left", padx=0)
    ctk.CTkLabel(parent_frame, textvariable=name_variable, text_color="gray", font=bold_font).pack(side="left", padx=(5, 0))
    ctk.CTkButton(parent_frame, text="", command=lambda: select_file(path_variable, name_variable), image=upload_icon, width=20, height=30).pack(side="left", padx=15)

def get_output_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

upload_icon = ctk.CTkImage(light_image=Image.open(get_asset_path("assets/file-up.png")))

create_file_row(row0_frame, "Current Month Data:", curr_path_var, curr_name_var)
create_file_row(row1_frame, "Previous Month Data:", prev_path_var, prev_name_var)
create_file_row(row2_frame, "Last Year Month Data:", last_path_var, last_name_var)

ctk.CTkButton(inner_frame, text="Generate Dashboard", command=run_generator, fg_color="green", text_color="white", font=bold_font).pack(pady=(30, 10), ipadx=10, ipady=5)

download_btn = ctk.CTkButton(inner_frame, text="Save Dashboard As...", command=save_dashboard, font=("Segoe UI", 13, "bold"))

root.mainloop()