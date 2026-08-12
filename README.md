# 🥃 Spirits Label Compliance Scanner

A 100% free tool designed to dynamically generate mock compliance labels (Front, Back, and Neck Strips) and process them through a computer vision (CV) and OCR parsing pipeline to extract essential TTB information fields.

---

## 🚀 Quick Start (Windows Setup via Cmd)

Follow these exact steps to set up and run the complete web application on Windows using native Command Prompt (`cmd.exe`).

### 1. Prerequisites (Free Tools Only)

Before installing Python dependencies, your system needs **Tesseract OCR** installed to power the text recognition engine.

1. Download the free Windows installer from [UB Mannheim Tesseract Git](https://github.com).
2. Run the `.exe` installer. Note the installation path (usually `C:\Program Files\Tesseract-OCR`).
3. Open **Command Prompt** as Admin and run this command to permanently add Tesseract to your Windows system Environment PATH variable:
   ```cmd
   setx /M PATH "%PATH%;C:\Program Files\Tesseract-OCR"
   ```
4. Restart your Command Prompt for the path variable changes to take effect.

### 2. Clone the Repository via Git
Open your Command Prompt, navigate to your working directory, and use Git to pull down the source code from GitHub:
```cmd
git clone https://github.com
cd distilled-spirits-parser
```

### 3. Create & Activate a Python Virtual Environment
Keep your workspace clean by isolating dependencies directly through `Cmd`:
```cmd
rem Create the environment
python -m venv venv

rem Activate the environment on Windows
call venv\Scripts\activate.bat
```

### 4. Install Dependencies
Install all required libraries using the Python package manager:
```cmd
pip install -r requirements.txt
```

### 5. Launch the App Locally
Run the local Streamlit development server:
```cmd
streamlit run app.py
```
Your default web browser should open automatically to `http://localhost:8501`.

---

## 📂 Project Architecture

```text
distilled-spirits-parser/
├── app.py                 # Core Streamlit app UI, layouts, and Tab logic
├── requirements.txt       # Python package list
├── packages.txt           # Required for Streamlit Cloud linux dependencies
└── utils/
    ├── __init__.py        # Empty file marking 'utils' as an importable module
    └── parser.py          # Label generator layout engine and regex parsing logic
```

---

## 🛠️ App Workflows

### Tab 1: Generate Free Test Label
1. Modify input fields for **Brand Name**, **Class/Type**, **Alcohol**, and **Net Contents**.
2. Select your desired layout configuration from the **Select Label Style to Generate** dropdown:
   * **Front Label**: Clean, structural vertical layout with solid padding lines.
   * **Back Label**: Wider panel featuring standard TTB Surgeon General health warning language.
   * **Neck Strip**: High-contrast ribbon pattern meant to seal bottle neck openings.
3. Click **Generate & Store Label Image** to view the graphic layout and sync it into memory.

### Tab 2: Run OCR & Parser Pipeline
1. Choose an image origin source:
   * **Use Generated Label from Tab 1** (Scans the dataset layout you just built).
   * **Upload a Real Label Image File** (Accepts custom local `.jpg` or `.png` files).
2. Click **Run Text Analysis Pipeline**.
3. Watch the app convert arrays to grayscale and extract structured JSON compliant fields.

---

## ☁️ Deploying to Streamlit Cloud (OAuth Workspace)

To host this app live on the web using Streamlit's free cloud environment and third-party GitHub OAuth integration:

### 1. Configure Cloud Dependencies
Because the live app runs on a Linux cloud server, you must ensure a file named `packages.txt` exists at your root directory. It must contain exactly this single line to trigger the automatic installation of the cloud OCR engine:
```text
tesseract-ocr
```

### 2. Push Changes via Git
Commit and sync your local updates to your GitHub repository:
```cmd
git add .
git commit -m "Configure dropdown labels and windows setup documentation"
git push origin main
```

### 3. Connect via Streamlit Dashboard Admin Portal
1. Navigate to the [Streamlit Community Cloud Admin Console](https://streamlit.io).
2. Log in using the **Continue with GitHub** OAuth application authentication workflow.
3. Once authenticated as the Workspace Admin, click **New app** in the upper-right corner.
4. Select your `distilled-spirits-parser` repository from the dropdown menu.
5. Set the Main file path text box field to `app.py`.
6. Click **Deploy!** The dashboard environment will spin up a container and open your public project link.
