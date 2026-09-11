import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
import customtkinter as ctk
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

def get_live_euro_rate():
    try:
        request = urllib.request.Request(url, headers=header)

        with urllib.request.urlopen(request) as response:
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

# fix app window and error pop up to appear in the middle of the screen whe opened
# delete the files in the input and output folders