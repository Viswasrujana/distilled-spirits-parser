import re
from PIL import Image, ImageDraw

def generate_free_label(brand, class_type, alcohol, net_contents, label_type="FRONT"):
    """Generates distinct, high-contrast mock labels based on the requested type."""
    label_type = label_type.upper()
    
    if label_type == "FRONT":
        img = Image.new('RGB', (400, 500), color='white')
        d = ImageDraw.Draw(img)
        d.rectangle([(10, 10), (390, 490)], outline="black", width=3)
        d.text((40, 60), "PREMIUM SELECTION", fill='gray')
        d.text((40, 120), f"BRAND: {brand.upper()}", fill='black')
        d.text((40, 200), f"PRODUCT: {class_type.upper()}", fill='black')
        d.text((40, 380), f"ALC. {alcohol} BY VOL.", fill='black')
        d.text((40, 420), f"NET CONTENTS: {net_contents}", fill='black')
        
    elif label_type == "BACK":
        img = Image.new('RGB', (500, 450), color='white')
        d = ImageDraw.Draw(img)
        d.rectangle([(10, 10), (490, 440)], outline="black", width=2)
        d.text((30, 30), f"{brand.upper()} - {class_type.upper()}", fill='black')
        d.text((30, 70), f"Distributed safely • {net_contents} • {alcohol}", fill='gray')
        d.line([(30, 110), (470, 110)], fill="black", width=1)
        d.text((30, 130), "GOVERNMENT WARNING:", fill='black')
        warning_text = (
            "(1) According to the Surgeon General, women should not\n"
            "drink alcoholic beverages during pregnancy because of the\n"
            "risk of birth defects. (2) Consumption of alcoholic\n"
            "beverages impairs your ability to drive a car or operate\n"
            "machinery, and may cause health problems."
        )
        d.text((30, 160), warning_text, fill='gray')
        
    elif label_type == "NECK":
        img = Image.new('RGB', (500, 120), color='white')
        d = ImageDraw.Draw(img)
        d.line([(0, 10), (500, 10)], fill="black", width=2)
        d.line([(0, 110), (500, 110)], fill="black", width=2)
        d.text((40, 35), f"★  {brand.upper()}  ★", fill='black')
        d.text((40, 70), f"ESTABLISHED 2026  |  {alcohol}", fill='gray')
        
    else:
        img = Image.new('RGB', (500, 300), color='white')
        d = ImageDraw.Draw(img)
        d.text((30, 30), f"{brand} - {class_type}", fill='black')

    return img

def free_parse_text(raw_text):
    """Uses robust string isolation and regex to parse TTB compliance label targets."""
    parsed = {
        "brand_name": "Not Found",
        "class_type": "Not Found",
        "alcohol_content": "Not Found",
        "net_contents": "Not Found",
        "government_warning": "Not Found"
    }
    lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
    for line in lines:
        lower_line = line.lower()
        if "brand" in lower_line:
            parsed["brand_name"] = re.sub(r'(?i)brand\s*name\s*:\s*', '', line).strip()
        elif parsed["brand_name"] == "Not Found" and len(line) > 4 and ":" not in line:
            parsed["brand_name"] = line.strip()
            
        if any(keyword in lower_line for keyword in ["whiskey", "bourbon", "gin", "vodka", "rum", "tequila", "class"]):
            parsed["class_type"] = re.sub(r'(?i)class\s*/\s*type\s*:\s*', '', line).strip()
            
        if "%" in lower_line or "proof" in lower_line or "alc" in lower_line:
            parsed["alcohol_content"] = re.sub(r'(?i)alcohol\s*content\s*:\s*', '', line).strip()
            
        if any(keyword in lower_line for keyword in ["ml", "cl", "750", "liter", "contents"]):
            parsed["net_contents"] = re.sub(r'(?i)net\s*contents\s*:\s*', '', line).strip()
            
        if "warning" in lower_line or "surgeon" in lower_line or "general" in lower_line:
            parsed["government_warning"] = "HEALTH WARNING DETECTED: Standard TTB compliance text present."
            
    return parsed
