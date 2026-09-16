### 🏥 Clinic Revenue Dashboard Generator

**A Python desktop application built to automate financial analysis, track patient growth metrics, and generate ready-to-print Excel reports for medical clinics.**

#### 📖 Overview
Medical clinics handle massive amounts of monthly financial and patient data. Previously, calculating month-over-month revenue growth, identifying unique returning patients was a highly manual process. 

I built this application to completely automate that pipeline. The user simply uploads their raw Excel data, and the application cleans the data, fetches live currency conversion rates from the bank's official website, and generates a cleanly formatted, professional dashboard in seconds. 

#### ✨ Key Features
*   **Live Currency Conversion:** Automatically connects to the National Bank of Romania (BNR) API to pull live EUR to RON exchange rates, with an offline manual-entry fallback.
*   **Automated Data Cleaning:** Native Pandas logic that automatically detects, filters, and balances financial reversals.
*   **Zero-Baseline Growth Tracking:** Custom logic to identify "NEW" patient statuses and accurately calculate growth metrics when previous month data is zero.
*   **Standalone Executable:** Fully compiled into a single `.exe` file using PyInstaller for a seamless, zero-setup user experience. No Python installation required by the end-user. 
*   **Self-Cleaning Environment:** Utilizes the `sys._MEIPASS` temporary directory to build files invisibly, preventing clutter on the user's desktop.

#### 🛠️ Technology Stack
*   **Language:** Python
*   **Data Processing:** Pandas, Openpyxl
*   **User Interface:** CustomTkinter (Modern Dark Mode UI)
*   **Network & XML:** `urllib`, `xml.etree.ElementTree`, `ssl`
*   **Deployment:** PyInstaller

<img width="1202" height="615" alt="image" src="https://github.com/user-attachments/assets/d8cf4f69-b43c-4b7f-b1bd-57c8e76d5850" />
<img width="1741" height="690" alt="image" src="https://github.com/user-attachments/assets/90d38951-a4fc-460c-9a79-cacc3370068e" />
