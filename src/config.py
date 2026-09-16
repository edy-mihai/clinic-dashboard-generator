import os
import sys
import ssl
import urllib.request
import xml.etree.ElementTree as ET
import customtkinter as ctk
from customtkinter import CTk
from tkinter import messagebox

url = "https://curs.bnr.ro/nbrfxrates.xml"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/xml, text/xml, */*"
}

def get_template_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/2)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

def network_error_popup(app_window):
    custom_popup = ctk.CTkToplevel(master=app_window)
    custom_popup.title("Network Error")
    custom_popup.transient(app_window)

    custom_popup.geometry(CenterWindowToDisplay(app_window, 400, 160, app_window._get_window_scaling()))

    user_input = ctk.StringVar()

    def get_user_input(entry):
        user_input.set(entry.get())
        custom_popup.destroy()

    ctk.CTkLabel(custom_popup, text="Network error. Couldn't get the EURO rate. Please enter manually:", font=("Segoe UI", 14, "bold"), wraplength=350).pack(padx=20, pady=10)
    user_entry = ctk.CTkEntry(custom_popup, justify="right")
    user_entry.pack(padx=20, pady=5)
    ctk.CTkButton(custom_popup, text="Submit", font=("Segoe UI", 20, "bold"), command=lambda: get_user_input(user_entry)).pack(padx=20, pady=15, ipady=5)

    user_entry.focus_force()
    custom_popup.grab_set()
    custom_popup.wait_window()

    return user_input.get()

def get_live_euro_rate(app_window):
    try:
        request = urllib.request.Request(url, headers=header)
        bypass = ssl._create_unverified_context()

        with urllib.request.urlopen(request, context=bypass) as response:
            tree = ET.parse(response)
            root = tree.getroot()

            for elem in root.iter():
                if elem.attrib.get('currency') == 'EUR':
                    return float(elem.text)

    except Exception:
        while True:
            user_input = network_error_popup(app_window)

            if user_input:
                user_input = user_input.replace(',', '.')
                try:
                    return float(user_input)

                except ValueError:
                    messagebox.showerror("Error", "Please enter a number!")

            else:
                messagebox.showerror("Error", "A valid exchange rate is required!")

TEMPLATE_PATH = get_template_path("data/templates/DASHBOARD.xlsx")
SHEET_NAME = "Foaie 1"

# treat percentage edgecase
# delete input and output files