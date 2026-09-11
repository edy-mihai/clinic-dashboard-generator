import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
import customtkinter as ctk
from tkinter import messagebox

def get_template_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

url = "https://www.bnr.ro/nbrfxrates.xml"

def get_live_euro_rate():
    try:
        with urllib.request.urlopen(url) as response:
            tree = ET.parse(response)
            root = tree.getroot()

            for elem in root.iter():
                if elem.attrib.get('currency') == 'EUR':
                    return float(elem.text)

    except Exception:
        while True:
            user_input = ctk.CTkInputDialog(text="Network error. Couldn't get the EURO rate. Please enter manually:").get_input()

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
EURO_RATE = get_live_euro_rate()

# make the euro rate update automatically from an offical website