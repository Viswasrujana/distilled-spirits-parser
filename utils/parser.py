def generate_free_label(brand, class_type, alcohol, net_contents, label_type="FRONT"):
    """Generates distinct, high-contrast mock labels based on the requested type."""
    label_type = label_type.upper()
    
    if label_type == "FRONT":
        # Classic vertical front-of-bottle label
        img = Image.new('RGB', (400, 500), color='white')
        d = ImageDraw.Draw(img)
        
        # Outer Border
        d.rectangle([(10, 10), (390, 490)], outline="black", width=3)
        
        # Content
        d.text((40, 60), "PREMIUM SELECTION", fill='gray')
        d.text((40, 120), f"BRAND: {brand.upper()}", fill='black')
        d.text((40, 200), f"PRODUCT: {class_type.upper()}", fill='black')
        d.text((40, 380), f"ALC. {alcohol} BY VOL.", fill='black')
        d.text((40, 420), f"NET CONTENTS: {net_contents}", fill='black')
        
    elif label_type == "BACK":
        # Wider back label dedicated to compliance and warning text
        img = Image.new('RGB', (500, 450), color='white')
        d = ImageDraw.Draw(img)
        
        # Outer Border
        d.rectangle([(10, 10), (490, 440)], outline="black", width=2)
        
        # Content
        d.text((30, 30), f"{brand.upper()} - {class_type.upper()}", fill='black')
        d.text((30, 70), f"Distributed safely • {net_contents} • {alcohol}", fill='gray')
        
        # Divider Line
        d.line([(30, 110), (470, 110)], fill="black", width=1)
        
        # Warning Section
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
        # Short, wide band that wraps around the neck of a bottle
        img = Image.new('RGB', (500, 120), color='white')
        d = ImageDraw.Draw(img)
        
        # Top and Bottom Border Lines
        d.line([(0, 10), (500, 10)], fill="black", width=2)
        d.line([(0, 110), (500, 110)], fill="black", width=2)
        
        # Centered style content
        d.text((40, 35), f"★  {brand.upper()}  ★", fill='black')
        d.text((40, 70), f"ESTABLISHED 2026  |  {alcohol}", fill='gray')
        
    else:
        # Fallback to a basic template if type doesn't match
        img = Image.new('RGB', (500, 300), color='white')
        d = ImageDraw.Draw(img)
        d.text((30, 30), f"{brand} - {class_type}", fill='black')

    return img
