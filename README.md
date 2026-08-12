# 🥃 Spirits Label Compliance Scanner

A 100% free tool built entirely via Command Prompt (`cmd.exe`) and Python. It dynamically generates mock compliance label variants (Front, Back, and Neck Strips) and runs them through a computer vision (CV) and OCR parsing pipeline to extract structured TTB data fields.

---

## 🚀 Windows Quick Start (Command Prompt & Text Editor)

Follow these exact steps to initialize, write, and run the entire application using native Windows tools.

### 1. Project Directory Initialization
Open your Windows **Command Prompt** (type `cmd` in your Start Menu) and execute the following commands to create your project architecture under your Documents folder:

```cmd
cd %USERPROFILE%\Documents
mkdir distilled-spirits-parser
cd distilled-spirits-parser
mkdir utils
```

### 2. File Creation via Cmd
Generate all essential system and configuration files directly from your terminal:

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

### 3. Writing the Code (Using Your Text Editor)
Open your preferred **Text Editor** (such as Notepad, VS Code, or Notepad++) and paste the respective source code blocks into the files you just generated:

*   **`utils/parser.py`**: Paste the layout engine code containing `generate_free_label` and `free_parse_text`.
*   **`app.py`**: Paste the frontend Streamlit dashboard tab logic.

### 4. Setup Python Environment & Run App Locally
Back in your Command Prompt workspace (inside the `distilled-spirits-parser` folder), run these commands to build your sandbox environment and launch the interface:

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
Your web browser will automatically load the app layout at `http://localhost:8501`.

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
*   Toggle your image source between using your freshly generated mock label or pulling a real `.jpg`/`.png` file from your device.
*   Click **Run Text Analysis Pipeline** to kickstart image processing and extract your structured JSON properties.

---

## ☁️ Deploying to Streamlit Cloud (Admin OAuth)

Since you did not download a local Tesseract executable setup, local OCR runs will hit an exception path. However, the application is pre-configured to run perfectly in the cloud out of the box using Streamlit's automated platform.

### 1. Initialize and Push to GitHub
Use Git directly from your Command Prompt to establish your remote storage repository:

```cmd
git init
git add .
git commit -m "Initial commit of command-line built parser application"
```
*(Link your repository to GitHub using `git remote add origin <your-url>` and run `git push -u origin main`)*

### 2. Authenticate Workspace Admin Cloud
1. Open your web browser and go to the **[Streamlit Community Cloud Dashboard](https://streamlit.io)**.
2. Select **Continue with GitHub** to login securely through the third-party OAuth app permissions gateway.
3. Click the **New app** admin button in the upper-right corner.
4. Pick your `distilled-spirits-parser` repository from your workspace drop-down menu.
5. Set the Main file path parameter text box to `app.py`.
6. Click **Deploy!** The cloud platform reads `packages.txt`, auto-installs `tesseract-ocr`, builds your environment, and generates your public application link.
