# 🥃 Spirits Label Compliance Scanner

A 100% free tool designed to dynamically generate mock compliance labels (Front, Back, and Neck Strips) and process them through a computer vision (CV) and OCR parsing pipeline to extract essential TTB information fields.

---

## 🚀 Quick Start (Local Setup)

Follow these steps to run the complete web application on your local machine.

### 1. Prerequisites

Before installing Python dependencies, your operating system needs **Tesseract OCR** installed to power the text recognition engine.

*   **macOS** (via Homebrew):
    ```bash
    brew install tesseract
    ```
*   **Windows**:
    1. Download the installer from [UB Mannheim Tesseract Git](https://github.com).
    2. Run the `.exe` installer.
    3. Add the installation folder (usually `C:\Program Files\Tesseract-OCR`) to your system's **Environment PATH Variables**.
*   **Linux (Ubuntu/Debian)**:
    ```bash
    sudo apt-get update
    sudo apt-get install tesseract-ocr libtesseract-dev
    ```

### 2. Clone the Repository
Navigate to your desired directory in your terminal and clone the repository:
```bash
git clone https://github.com
cd distilled-spirits-parser
```

### 3. Create a Virtual Environment
It is highly recommended to isolate your project dependencies:
```bash
# Create the environment
python -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
Install all required libraries using the package manager:
```bash
pip install -r requirements.txt
```

*Note: Ensure your `requirements.txt` includes: `streamlit`, `pytesseract`, `opencv-python-headless`, `numpy`, and `Pillow`.*

### 5. Launch the App
Run the local development server:
```bash
streamlit run app.py
```
Your browser should open automatically to `http://localhost:8501`.

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

## ☁️ Deploying to Streamlit Cloud

To host this live on the web for free via Streamlit Community Cloud:

1. Push your updated code structure to a public repository on GitHub.
2. Ensure you have a `packages.txt` file at your root directory containing exactly this line so the cloud server installs the system-level OCR engine:
   ```text
   tesseract-ocr
   ```
3. Go to [share.streamlit.io](https://streamlit.io) and log in with your GitHub account.
4. Click **New app**, select your `distilled-spirits-parser` repository, the branch, and set your main file path to `app.py`.
5. Click **Deploy!**
