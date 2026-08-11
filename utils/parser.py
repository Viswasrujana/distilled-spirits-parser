import re
from PIL import Image, ImageDraw

def generate_free_label(brand, class_type, alcohol, net_contents):
    """Generates a high-contrast mock label entirely offline and for free."""
    img = Image.new('RGB', (500, 500), color='white')
    d = ImageDraw.Draw(img)

    d.text((30, 40), f"BRAND NAME: {brand.upper()}", fill='black')
    d.text((30, 100), f"CLASS/TYPE: {class_type}", fill='black')
    d.text((30, 160), f"ALCOHOL CONTENT: {alcohol}", fill='black')
    d.text((30, 220), f"NET CONTENTS: {net_contents}", fill='black')

    d.text((30, 300), "GOVERNMENT WARNING:", fill='black')
    warning_text = (
        "(1) According to the Surgeon General, women should not\n"
        "drink alcoholic beverages during pregnancy because of the\n"
        "risk of birth defects. (2) Consumption of alcoholic\n"
        "beverages impairs your ability to drive a car or operate\n"
        "machinery, and may cause health problems."
    )
    d.text((30, 330), warning_text, fill='gray')
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
