# 🥃 Spirits Label Compliance Scanner

A 100% free tool built entirely via Command Prompt (`cmd.exe`) and Python. It dynamically generates mock compliance label variants (Front, Back, and Neck Strips) and runs them through a computer vision (CV) and OCR parsing pipeline to extract structured TTB data fields.

---

## 🚀 Windows Quick Start (Command Prompt & Text Editor)

Follow these exact steps to initialize, write, and run the entire application using native Windows tools.

### 1. Project Directory Initialization
Open Windows **Command Prompt** (type `cmd` in Start Menu) and execute the following commands to create project architecture under Documents folder:

```cmd
cd %USERPROFILE%\Documents
mkdir distilled-spirits-parser
cd distilled-spirits-parser
mkdir utils
```

### 2. File Creation via Cmd
Generate all essential system and configuration files directly from terminal:

```cmd
type nul > app.py
echo tesseract-ocr > packages.txt

(
echo streamlit
echo pytesseract
echo opencv-python-headless
echo numpy
echo Pillow
) > requirements.txt

cd utils
type nul > __init__.py
type nul > parser.py
cd ..
```

### 3. Writing the Code (Using Text Editor)
preferred **Text Editor** (such as Notepad, VS Code, or Notepad++) and paste the respective source code blocks into the files just generated:

*   **`utils/parser.py`**: Paste the layout engine code containing `generate_free_label` and `free_parse_text`.
*   **`app.py`**: Paste the frontend Streamlit dashboard tab logic.

### 4. Setup Python Environment & Run App Locally
Back in Command Prompt workspace (inside the `distilled-spirits-parser` folder), run these commands to build sandbox environment and launch the interface:

```cmd
rem Create a Python virtual sandbox
python -m venv venv

rem Activate the virtual environment
call venv\Scripts\activate.bat

rem Install required dependencies 
pip install -r requirements.txt

rem Boot up the local web engine
streamlit run app.py
```
 web browser will automatically load the app lat at `http://localhost:8501`.

---

## 📂 Project Tree Structure

```text
distilled-spirits-parser/
├── app.py                 # Main Streamlit user interface & layout tabs
├── requirements.txt       # Python packaging dependencies
├── packages.txt           # Critical Linux core dependency instructions for the cloud
└── utils/
    ├── __init__.py        # Empty file declaring a local python module package
    └── parser.py          # Label graphics construction and regex parser algorithms
```

---

## 🛠️ Feature Workflows

### Tab 1: Generate Free Test Label
*   Fill in text properties for **Brand Name**, **Class/Type**, **Alcohol Content**, and **Net Contents**.
*   Use the drop-down selector to configure the visual label layout formatting (**Front Label**, **Back Label**, or **Neck Strip**).
*   Click **Generate & Store Label Image** to render the mock graphic canvas into temporary memory cache.

### Tab 2: Run OCR & Parser Pipeline
*   Toggle image source between using freshly generated mock label or pulling a real `.jpg`/`.png` file from device.
*   Click **Run Text Analysis Pipeline** to kickstart image processing and extract structured JSON properties.

---

## ☁️ Deploying to Streamlit Cloud (Admin OAuth)

application is pre-configured to run perfectly in the cloud out of the box using Streamlit's automated platform.

### 1. Initialize and Push to GitHub
Use Git directly from Command Prompt to establish  remote storage repository:

```cmd
git init
git add .
git commit -m "Initial commit of command-line built parser application"
```
*(Link  repository to GitHub using `git remote add origin <-url>` and run `git push -u origin main`)*

### 2. Authenticate Workspace Admin Cloud
1. Open web browser and go to the **[Streamlit Community Cloud Dashboard](https://streamlit.io)**.
2. Select **Continue with GitHub** to login securely through the third-party OAuth app permissions gateway.
3. Click the **New app** admin button in the upper-right corner.
4. Pick  `distilled-spirits-parser` repository from workspace drop-down menu.
5. Set the Main file path parameter text box to `app.py`.
6. Click **Deploy!** The cloud platform reads `packages.txt`, auto-installs `tesseract-ocr`, builds your environment, and generates public application link.
